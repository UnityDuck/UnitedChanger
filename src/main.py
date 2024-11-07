import sys
import sqlite3
import requests
import validate_email
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
from PyQt6.QtWidgets import QCheckBox, QLabel, QGraphicsBlurEffect
from PyQt6.QtCore import Qt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap, QMovie
from PyQt6 import QtCore, QtTest
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import (QApplication, QDialog, QSplashScreen, QMessageBox,
                             QGraphicsScene, QVBoxLayout, QWidget)


class CurrencyConverter:
    def __init__(self, value1):
        self.value1 = value1
        self.value1_rate = None

    def convertValues(self, value2):
        response = requests.get(f'https://api.coinbase.com/v2/prices/{self.value1}-{value2}/spot')
        data = response.json()
        self.value1_rate = data["data"]["amount"]
        return round(float(self.value1_rate), 5)

    def XtoYconverter(self, value2, x):
        response = requests.get(f'https://api.coinbase.com/v2/prices/{self.value1}-{value2}/spot')
        data = response.json()
        self.value1_rate = data["data"]["amount"]
        return round(float(self.value1_rate) * x, 5)


def logsSaver(ErrorStatus, ErrorMessage):
    with open("../logs/logs.txt", mode="w", encoding="UTF-8") as file:
        file.write(f"{datetime.now()}; Error-code: {ErrorStatus}. Exception: {ErrorMessage}.")


class DifferentPasswords(Exception):
    def __init__(self):
        self.errorStatus = "0"
        self.errorMessage = "DifferentPasswords"
        logsSaver(self.errorStatus, self.errorMessage)


class NotValidEmail(Exception):
    def __init__(self):
        self.errorStatus = "1"
        self.errorMessage = "InvalidInput"
        logsSaver(self.errorStatus, self.errorMessage)


class FieldsAreNotFilled(Exception):
    def __init__(self):
        self.errorStatus = "2"
        self.errorMessage = "EmptyInput"
        logsSaver(self.errorStatus, self.errorMessage)


class IncorrectData(Exception):
    def __init__(self):
        self.errorStatus = "3"
        self.errorMessage = "IncorrectInput"
        logsSaver(self.errorStatus, self.errorMessage)


class ProgressBarWindow(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("../UserInterfaces/ProgressBarWindow.ui", self)
        self.time_for_sleep = 0
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setDisabled(True)
        self.pixmapBackground = QPixmap("../images/splashGradient2.png")
        self.setPixmap(self.pixmapBackground)
        self.pixmapLogo = QPixmap("../images/splashLogo.png")
        self.labelLogo.setPixmap(self.pixmapLogo)

    def progressBarChanger(self):
        for i in range(101):
            self.progressBar.setValue(i)
            if i <= 60:
                self.time_for_sleep = 10
            elif i < 90:
                self.time_for_sleep = 50
            else:
                self.time_for_sleep = 100
            QtTest.QTest.qWait(self.time_for_sleep)
        QtTest.QTest.qWait(200)


class LoginWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("../UserInterfaces/LoginWindow.ui", self)
        self.registrationProcess = None
        self.runRememberingProcess = None
        self.mainUnitedChanger = None
        self.setWindowTitle("Login to UnitedChanger")
        self.pixmapLogo = QPixmap("../images/LoginWindowLogo.png")
        self.LabelLogo.setPixmap(self.pixmapLogo)
        self.RegistrationButton.clicked.connect(self.runRegisterWindow)
        self.ForgotPasswordButton.clicked.connect(self.runForgotPasswordWindow)
        self.EnterButton.clicked.connect(self.loginProcess)

    def runRegisterWindow(self):
        self.registrationProcess = RegisterWindow()
        self.registrationProcess.show()
        self.close()

    def runForgotPasswordWindow(self):
        self.runRememberingProcess = ForgotPasswordWindow()
        self.runRememberingProcess.show()
        self.close()

    def zeroMaker(self):
        self.LoginLine.setText("")
        self.PasswordLine.setText("")

    def loginProcess(self):
        try:
            if not all([self.LoginLine.text(), self.PasswordLine.text()]):
                raise FieldsAreNotFilled
            conn = sqlite3.connect("../databases/users.sqlite")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users_table")
            data = cursor.fetchall()
            logins = [el[1] for el in data]
            passwords = [el[2] for el in data]
            conn.commit()
            conn.close()
            login = self.LoginLine.text()
            password = self.PasswordLine.text()
            if not validate_email.validate_email(login):
                raise NotValidEmail
            if login not in logins or password not in passwords or logins.index(login) != passwords.index(password):
                raise IncorrectData
            self.loginSuccess()
        except FieldsAreNotFilled:
            self.criticalLoginWindowCaller("Empty data", "You must fill in all the windows.")
        except IncorrectData:
            self.criticalLoginWindowCaller("Invalid login/password", "Your login/password is incorrect.")
        except NotValidEmail:
            self.criticalLoginWindowCaller("Invalid email", "Email is not valid.")

    def criticalLoginWindowCaller(self, title, text):
        QMessageBox.critical(self, title, text)
        self.zeroMaker()

    def loginSuccess(self):
        self.mainUnitedChanger = UnitedChangerMainWindow()
        self.mainUnitedChanger.show()
        self.close()


class RegisterWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("../UserInterfaces/RegisterWindow.ui", self)
        self.LoginWindowReopener = None
        self.id = 1
        self.CriticalError = "CriticalError"
        self.setWindowTitle("Registration")
        self.RegisterButton.clicked.connect(self.registration)

    def zeroMaker(self):
        self.PasswordEntery.setText("")
        self.PasswordEnteryAgain.setText("")
        self.LoginEntery.setText("")

    def registration(self):
        try:
            if not all([self.PasswordEntery.text(), self.PasswordEnteryAgain.text(), self.LoginEntery.text()]):
                raise FieldsAreNotFilled
            if not validate_email.validate_email(self.LoginEntery.text()):
                raise NotValidEmail
            if not self.PasswordEntery.text() == self.PasswordEnteryAgain.text():
                raise DifferentPasswords
            conn = sqlite3.connect("../databases/users.sqlite")
            cursor = conn.cursor()
            login = self.LoginEntery.text()
            password = self.PasswordEntery.text()
            cursor.execute("INSERT INTO users_table (id, login, password) VALUES (?, ?, ?)",
                           (self.id, login, password))
            conn.commit()
            conn.close()
            self.id += 1
            QMessageBox.about(self, "RegistrationEnding", "Registration is completed!")
            self.zeroMaker()
        except FieldsAreNotFilled:
            self.criticalRegisterWindowCaller("Empty data", "You must fill in all the windows.")
        except DifferentPasswords:
            self.criticalRegisterWindowCaller("DifferentPasswords", "Your passwords are different.")
        except NotValidEmail:
            self.criticalRegisterWindowCaller("Invalid data", "Email is not valid.")

    def criticalRegisterWindowCaller(self, title, text):
        QMessageBox.critical(self, title, text)
        self.zeroMaker()

    def closeEvent(self, event):
        self.LoginWindowReopener = LoginWindow()
        self.LoginWindowReopener.show()


class ForgotPasswordWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("../UserInterfaces/ForgotPasswordWindow.ui", self)
        self.LoginWindowReopener = None
        self.setWindowTitle("Don't forget you password again =)")
        self.TimeLabel.hide()
        self.rememberButton.clicked.connect(self.rememberProcess)

    def rememberProcess(self):
        try:
            if not self.EmailLine.text():
                raise FieldsAreNotFilled
            if not validate_email.validate_email(self.EmailLine.text()):
                raise NotValidEmail

            ### In developing...

            self.TimeLabel.show()
            self.rememberButton.setEnabled(False)
            for i in range(61):
                if 60 - i == 60:
                    self.TimeLabel.setText("Send password again in 1:00")
                elif 10 <= 60 - i < 60:
                    self.TimeLabel.setText("Send password again in 0:" + str(60 - i))
                else:
                    self.TimeLabel.setText("Send password again in 0:0" + str(60 - i))
                QtTest.QTest.qWait(1000)
            self.TimeLabel.hide()
            self.rememberButton.setEnabled(True)
        except FieldsAreNotFilled:
            self.criticalForgotPasswordWindowCaller("Empty Data", "You must fill the login field.")
        except NotValidEmail:
            self.criticalForgotPasswordWindowCaller("Invalid email", "Email is not valid.")

    def criticalForgotPasswordWindowCaller(self, title, text):
        QMessageBox.critical(self, title, text)
        self.EmailLine.setText("")

    def closeEvent(self, event):
        self.LoginWindowReopener = LoginWindow()
        self.LoginWindowReopener.show()


class UnitedChangerMainWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.loadingLabel = QLabel(self)
        self.loadingLabel.setGeometry(QtCore.QRect(25, 25, 200, 200))
        self.loadingLabel.setMinimumSize(QtCore.QSize(250, 250))
        self.loadingLabel.setMaximumSize(QtCore.QSize(250, 250))
        self.movie = QMovie("load-loading.gif")
        self.loadingLabel.setMovie(self.movie)
        self.loadingLabel.hide()
        self.value2Logo = None
        loadUi("../UserInterfaces/UnitedChangerMainWindow.ui", self)
        self.settingsOpener = None
        self.previewOpener = None
        self.pixmapLogo = QPixmap("../images/MainWindowLogo.png")
        self.LogotypeLabel.setPixmap(self.pixmapLogo)
        self.settingsButton.clicked.connect(self.settingsRunner)
        self.previewButton.clicked.connect(self.previewRunner)
        self.liked_values = []
        self.list_of_values = ["JPY (Japan)", "AUD (Australia)", "UAH (Ukraine)",
                                      "CAD (Canada)", "BYN (Belarussia)", "ILS (Israel)",
                                      "AED (UAE)", "RSD (Serbia)", "GBP (Britain)",
                                      "RUB (Russia)", "EUR (Europe)", "USD (USA)", "KZT (Kazakhstan)"]
        self.Value1ComboBox.addItems(self.list_of_values)
        self.list_values_combobox2 = []
        self.reverseCounter = 1
        self.checkerForAbilityValues()
        self.Value2ComboBox.addItems(self.list_values_combobox2)
        self.value1Logo = QPixmap(f"../flags/{self.Value1ComboBox.currentText().split()[0]}.png")
        self.Value1Flag.setPixmap(self.value1Logo)
        self.Value1Flag.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelValue1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelValue2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Value1ComboBox.currentIndexChanged.connect(self.ComboBox2ValuesChooser)
        self.Value2ComboBox.currentIndexChanged.connect(self.CurrencyTurner)
        self.CurrencyTurner()
        self.buttonEquality.clicked.connect(self.reverseValues)
        self.checkbox_container = QWidget()
        self.checkbox_layout = QVBoxLayout(self.checkbox_container)
        for el in self.list_of_values:
            checkbox = QCheckBox(el)
            checkbox.stateChanged.connect(self.update_selected_options)
            self.checkbox_layout.addWidget(checkbox)
        self.scrollArea.setWidget(self.checkbox_container)
        self.Converter1ComboBox.addItems(self.list_of_values)
        self.Converter2ComboBox.addItems(self.list_of_values)
        # self.converter2ComboBoxChanger()
        self.update_combobox_labels()
        self.ConvertButton.clicked.connect(self.globalConverter)
        self.ConvertationResult.setAlignment(Qt.AlignmentFlag.AlignCenter)
    #     self.Converter1ComboBox.itemChanged.connect(self.converter2ComboBoxChanger)
    #
    # def converter2ComboBoxChanger(self):
    #     self.Converter2ComboBox.clear()
    #     self.Converter2ComboBox.addItems([el for el in self.list_of_values if
    #                                       el != self.Converter1ComboBox.currentText()])

    def update_selected_options(self):
        if self.sender().isChecked():
            self.liked_values.append(self.sender().text())
        else:
            self.liked_values.remove(self.sender().text())
        self.update_combobox_labels()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()

    def update_combobox_labels(self):
        for i in range(self.Value1ComboBox.count()):
            item_text = self.list_of_values[i]
            if item_text in self.liked_values:
                self.Value1ComboBox.setItemText(i, f"{item_text} ★")
            else:
                self.Value1ComboBox.setItemText(i, item_text)
        for i in range(self.Value2ComboBox.count()):
            item_text = self.Value2ComboBox.itemText(i).split(' ★')[0]
            if item_text in self.liked_values:
                self.Value2ComboBox.setItemText(i, f"{item_text} ★")
            else:
                self.Value2ComboBox.setItemText(i, item_text)
        for i in range(self.Converter1ComboBox.count()):
            item_text = self.Converter1ComboBox.itemText(i).split(' ★')[0]
            if item_text in self.liked_values:
                self.Converter1ComboBox.setItemText(i, f"{item_text} ★")
            else:
                self.Converter1ComboBox.setItemText(i, item_text)
        for i in range(self.Converter2ComboBox.count()):
            item_text = self.Converter2ComboBox.itemText(i).split(' ★')[0]
            if item_text in self.liked_values:
                self.Converter2ComboBox.setItemText(i, f"{item_text} ★")
            else:
                self.Converter2ComboBox.setItemText(i, item_text)

    def globalConverter(self):
        self.ConvertationResult.setText(str(CurrencyConverter(self.Converter1ComboBox.currentText().split()[0]).
         XtoYconverter(self.Converter2ComboBox.currentText().split()[0], self.DoubleSpinConverterBox.value())))

    def settingsRunner(self):
        self.settingsOpener = SettingWindow()
        self.settingsOpener.show()
        self.close()

    def previewRunner(self):
        self.previewOpener = PreviewWindow()
        self.previewOpener.show()
        self.close()

    def checkerForAbilityValues(self):
        self.startAnimation()
        self.list_values_combobox2 = []
        for el in self.list_of_values:
            first_value = self.Value1ComboBox.currentText().split()[0]
            second_value = el.split()[0]
            if second_value != first_value:
                pair = first_value + second_value
                end_date = datetime.now()
                start_date = end_date - timedelta(days=365)
                start_date_str = start_date.strftime('%Y-%m-%d')
                end_date_str = end_date.strftime('%Y-%m-%d')
                aapl = yf.Ticker(pair + "=X")
                data = aapl.history(start=start_date_str, end=end_date_str)
                if data.empty:
                    continue
                else:
                    self.list_values_combobox2.append(el)
            else:
                continue
        self.stopAnimation()

    def ComboBox2ValuesChooser(self):
        if self.Value2ComboBox.currentText():
            self.value1Logo = QPixmap(f"../flags/{self.Value1ComboBox.currentText().split()[0]}.png")
            self.Value1Flag.setPixmap(self.value1Logo)
            self.Value2ComboBox.clear()
            self.checkerForAbilityValues()
            self.Value2ComboBox.addItems(self.list_values_combobox2)

    def CurrencyTurner(self):
        if self.Value2ComboBox.currentText():
            self.value2Logo = QPixmap(f"../flags/{self.Value2ComboBox.currentText().split()[0]}.png")
            self.Value2Flag.setPixmap(self.value2Logo)
            self.Value2Flag.setAlignment(Qt.AlignmentFlag.AlignCenter)
            scene = QGraphicsScene()
            self.graphicsView.setScene(scene)
            first_value = self.Value1ComboBox.currentText().split()[0]
            second_value = self.Value2ComboBox.currentText().split()[0]
            pair = first_value + second_value
            end_date = datetime.now()
            start_date = end_date - timedelta(days=365)
            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')
            aapl = yf.Ticker(pair + "=X")
            data = aapl.history(start=start_date_str, end=end_date_str)
            data.reset_index(inplace=True)
            data['Date'] = pd.to_datetime(data['Date'])
            data['Date'] = data['Date'].apply(mpl_dates.date2num)
            ohlc = data[['Date', 'Open', 'High', 'Low', 'Close']].copy()
            ohlc = ohlc.astype(float)
            fig, ax = plt.subplots(figsize=(6.0, 3.0))
            candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)
            ax.set_xlabel('Date')
            ax.set_ylabel('Price')
            ax.set_title(f'График курса {pair}')
            date_format = mpl_dates.DateFormatter('%d-%m-%Y')
            ax.xaxis.set_major_formatter(date_format)
            fig.autofmt_xdate()
            fig.tight_layout()
            plt.savefig("plot.png")
            plt.close()
            pixmap = QPixmap("plot.png")
            scene.addPixmap(pixmap)
            self.graphicsView.setScene(scene)
            self.reverseValues()

    def reverseValues(self):
        first_value = self.Value1ComboBox.currentText().split()[0]
        second_value = self.Value2ComboBox.currentText().split()[0]
        if self.reverseCounter < 0:
            self.labelValue1.setText(f"1 {second_value}")
            self.labelValue2.setText(f"{CurrencyConverter(second_value).convertValues(first_value)} {first_value}")
            self.reverseCounter *= -1
        else:
            self.labelValue1.setText(f"1 {first_value}")
            self.labelValue2.setText(f"{CurrencyConverter(first_value).convertValues(second_value)} {second_value}")
            self.reverseCounter *= -1
        self.loadingLabel.show()


class PreviewWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("../UserInterfaces/PreviewWindow.ui")
        self.UnitedMainReopener = None

    def closeEvent(self, event):
        self.UnitedMainReopener = UnitedChangerMainWindow()
        self.UnitedMainReopener.show()


class SettingWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("../UserInterfaces/SettingWindow.ui")
        self.UnitedMainReopener = None

    def closeEvent(self, event):
        self.UnitedMainReopener = UnitedChangerMainWindow()
        self.UnitedMainReopener.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ProgressWindow = ProgressBarWindow()
    ProgressWindow.show()
    ProgressWindow.progressBarChanger()
    LoginWindowApp = LoginWindow()
    LoginWindowApp.show()
    ProgressWindow.finish(LoginWindowApp)
    app.exec()