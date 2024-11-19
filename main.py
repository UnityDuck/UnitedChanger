import sys
import sqlite3
from templates import *
import requests
import validate_email
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
from PyQt6.QtWidgets import QCheckBox, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from PyQt6 import uic
import io
from PyQt6.QtGui import QPixmap, QMovie
from PyQt6 import QtCore, QtTest
from concurrent.futures import ThreadPoolExecutor
import csv
from PyQt6.QtWidgets import (QApplication, QDialog, QSplashScreen, QMessageBox,
                             QGraphicsScene, QVBoxLayout, QWidget)

USERNAME = ""


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
    with open("logs/logs.txt", mode="a", encoding="UTF-8") as file:
        file.write(f"{datetime.now()}; Error-code: {ErrorStatus}. Exception: {ErrorMessage}.\n")


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


class NoAvailableAccounts(Exception):
    def __init__(self):
        self.errorStatus = "4"
        self.errorMessage = "NoAccountsAreAvailable"
        logsSaver(self.errorStatus, self.errorMessage)


class AccountAlreadyExistsError(Exception):
    def __init__(self):
        self.errorStatus = "5"
        self.errorMessage = "AccountAlreadyExists"
        logsSaver(self.errorStatus, self.errorMessage)


class ProgressBarWindow(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        file = io.StringIO(ProgressBarWindowTemplate)
        uic.loadUi(file, self)
        self.time_for_sleep = 0
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setDisabled(True)
        self.pixmapBackground = QPixmap("images/splashGradient2.png")
        self.setPixmap(self.pixmapBackground)
        self.pixmapLogo = QPixmap("images/splashLogo.png")
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
        file = io.StringIO(LoginWindowTemplate)
        uic.loadUi(file, self)
        self.registrationProcess = None
        self.runRememberingProcess = None
        self.mainUnitedChanger = None
        self.setWindowTitle("LoginWindow")
        self.setFixedSize(387, 506)
        self.pixmapLogo = QPixmap("images/LoginWindowLogo.png")
        self.LabelLogo.setPixmap(self.pixmapLogo)
        self.RegistrationButton.clicked.connect(self.runRegisterWindow)
        self.ForgotPasswordButton.clicked.connect(self.runForgotPasswordWindow)
        self.EnterButton.clicked.connect(self.loginProcess)

    def runRegisterWindow(self):
        self.registrationProcess = RegisterWindow()
        self.registrationProcess.show()
        self.close()

    def runForgotPasswordWindow(self):
        QMessageBox.information(self, "InformationBeforeUsing", "This Window is not fully programmed. "
                                                                "Use it for your own scare and risk.")
        QMessageBox.information(self, "InformationBeforeUsing", "Also, if you have questions with using,"
                                                                "look for TechnicalTask.")
        self.runRememberingProcess = ForgotPasswordWindow()
        self.runRememberingProcess.show()
        self.close()

    def zeroMaker(self):
        self.LoginLine.setText("")
        self.PasswordLine.setText("")

    def loginProcess(self):
        try:
            conn = sqlite3.connect("databases/users.sqlite")
            cursor = conn.cursor()
            cursor.execute(f"SELECT id FROM users_table DISC")
            last_id = cursor.fetchall()
            conn.commit()
            conn.close()
            if last_id[-1] == 0:
                raise NoAvailableAccounts
            if not all([self.LoginLine.text(), self.PasswordLine.text()]):
                raise FieldsAreNotFilled
            conn = sqlite3.connect("databases/users.sqlite")
            cursor = conn.cursor()
            cursor.execute(f"SELECT login FROM users_table")
            logins_loaded = cursor.fetchall()
            conn.commit()
            conn.close()
            logins = []
            for el in logins_loaded:
                logins.append(el[0])
            login = self.LoginLine.text()
            password_entered = self.PasswordLine.text()
            if not validate_email.validate_email(login):
                raise NotValidEmail
            if login not in logins:
                raise IncorrectData
            conn = sqlite3.connect("databases/users.sqlite")
            cursor = conn.cursor()
            cursor.execute(f"SELECT password FROM users_table WHERE login='{self.LoginLine.text()}'")
            password = cursor.fetchall()[0]
            conn.commit()
            conn.close()
            if password_entered != password[0]:
                raise IncorrectData
            with open("logs/logs.txt", mode="a", encoding="UTF-8") as file:
                file.write(f"{datetime.now()}; {login} entered.\n")
            self.loginSuccess()
        except FieldsAreNotFilled:
            self.criticalLoginWindowCaller("Empty data", "You must fill in all the windows.")
        except IncorrectData:
            self.criticalLoginWindowCaller("Invalid login/password", "Your login/password is incorrect.")
        except NotValidEmail:
            self.criticalLoginWindowCaller("Invalid email", "Email is not valid.")
        except NoAvailableAccounts:
            self.criticalLoginWindowCaller("No accounts", "No accounts are available.")

    def criticalLoginWindowCaller(self, title, text):
        QMessageBox.critical(self, title, text)
        self.zeroMaker()

    def loginSuccess(self):
        global USERNAME
        USERNAME = self.LoginLine.text()
        self.mainUnitedChanger = UnitedChangerMainWindow()
        self.mainUnitedChanger.show()
        self.close()


class RegisterWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        file = io.StringIO(RegisterWindowTemplate)
        uic.loadUi(file, self)
        self.LoginWindowReopener = None
        self.CriticalError = "CriticalError"
        self.setWindowTitle("RegisterWindow")
        self.setFixedSize(389, 506)
        self.pixmapLogo = QPixmap("images/LoginWindowLogo.png")
        self.LabelLogo.setPixmap(self.pixmapLogo)
        self.RegisterButton.clicked.connect(self.registration)

    @staticmethod
    def lastIdReturner(name):
        connection = sqlite3.connect('databases/users.sqlite')
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT {name} FROM users_table ORDER BY {name} DESC LIMIT 1")
            last_id = cursor.fetchone()
            if last_id is not None:
                last_id_value = int(last_id[0])
            else:
                print("Таблица пуста, нет элементов.")
                return
        finally:
            cursor.close()
            connection.close()
        return last_id_value + 1

    def zeroMaker(self):
        self.PasswordEntery.setText("")
        self.PasswordEnteryAgain.setText("")
        self.LoginEntery.setText("")

    def registration(self):
        try:
            connChecker = sqlite3.connect("databases/users.sqlite")
            cursorChecker = connChecker.cursor()
            logins = cursorChecker.execute("""SELECT login FROM users_table""").fetchall()
            connChecker.commit()
            connChecker.close()
            if not all([self.PasswordEntery.text(), self.PasswordEnteryAgain.text(), self.LoginEntery.text()]):
                raise FieldsAreNotFilled
            if not validate_email.validate_email(self.LoginEntery.text()):
                raise NotValidEmail
            if not self.PasswordEntery.text() == self.PasswordEnteryAgain.text():
                raise DifferentPasswords
            conn = sqlite3.connect("databases/users.sqlite")
            cursor = conn.cursor()
            login = self.LoginEntery.text()
            if login in [el[0] for el in logins]:
                raise AccountAlreadyExistsError
            password = self.PasswordEntery.text()
            id_now = self.lastIdReturner("id")
            cursor.execute("INSERT INTO users_table (id, login, password) VALUES (?, ?, ?)",
                           (id_now, login, password))
            with open("logs/logs.txt", mode="a", encoding="UTF-8") as file:
                file.write(f"{datetime.now()}; {login} registered.\n")
            conn.commit()
            conn.close()
            connFavoriteId = sqlite3.connect("databases/users.sqlite")
            cursorFavoriteId = connFavoriteId.cursor()
            cursorFavoriteId.execute("INSERT INTO favorite_values_table (id, favoriteValues) VALUES (?, ?)",
                                     (id_now, ""))
            connFavoriteId.commit()
            connFavoriteId.close()
            QMessageBox.about(self, "RegistrationEnding", "Registration is completed!")
            self.zeroMaker()
        except FieldsAreNotFilled:
            self.criticalRegisterWindowCaller("Empty data", "You must fill in all the windows.")
        except DifferentPasswords:
            self.criticalRegisterWindowCaller("DifferentPasswords", "Your passwords are different.")
        except NotValidEmail:
            self.criticalRegisterWindowCaller("Invalid data", "Email is not valid.")
        except AccountAlreadyExistsError:
            self.criticalRegisterWindowCaller("Account error", "Account already exists.")

    def criticalRegisterWindowCaller(self, title, text):
        QMessageBox.critical(self, title, text)
        self.zeroMaker()

    def closeEvent(self, event):
        self.LoginWindowReopener = LoginWindow()
        self.LoginWindowReopener.show()


class ForgotPasswordWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        file = io.StringIO(ForgotPasswordWindowTemplate)
        uic.loadUi(file, self)
        self.LoginWindowReopener = None
        self.setWindowTitle("ForgotPasswordWindow")
        self.setFixedSize(460, 195)
        self.pixmapLogo = QPixmap("images/ForgotPasswordLogo.png")
        self.label.setPixmap(self.pixmapLogo)
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
        global USERNAME
        super(QDialog, self).__init__()
        file = io.StringIO(UnitedChangerMainWindowTemplate)
        uic.loadUi(file, self)
        self.value2Logo = None
        self.viewOpener = None
        self.loadingOpener = None
        self.setWindowTitle("UnitedChanger")
        self.setFixedSize(1147, 636)
        self.pixmapLogo = QPixmap("images/MainWindowLogo.png")
        self.LogotypeLabel.setPixmap(self.pixmapLogo)
        self.viewButton.clicked.connect(self.viewRunner)
        conn = sqlite3.connect('databases/users.sqlite')
        cursor = conn.cursor()
        cursor.execute(f"""SELECT id FROM users_table WHERE login='{USERNAME}'""")
        self.id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        conn = sqlite3.connect('databases/users.sqlite')
        cursor = conn.cursor()
        cursor.execute(f"""SELECT favoriteValues FROM favorite_values_table WHERE id={self.id}""")
        self.liked_values = cursor.fetchall()[0][0].split(", ")
        conn.commit()
        conn.close()
        self.list_of_values = ["JPY (Japan)", "AUD (Australia)", "UAH (Ukraine)",
                               "CAD (Canada)", "BYN (Belarussia)", "ILS (Israel)",
                               "AED (UAE)", "RSD (Serbia)", "GBP (Britain)",
                               "RUB (Russia)", "EUR (Europe)", "USD (USA)", "KZT (Kazakhstan)"]
        self.Value1ComboBox.addItems(self.list_of_values)
        self.list_values_combobox2 = []
        self.reverseCounter = 1
        self.checkerForAbilityValues()
        self.Value2ComboBox.addItems(self.list_values_combobox2)
        self.value1Logo = QPixmap(f"flags/{self.Value1ComboBox.currentText().split()[0]}.png")
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
            if el in self.liked_values:
                checkbox.setChecked(True)
            self.checkbox_layout.addWidget(checkbox)
        self.scrollArea.setWidget(self.checkbox_container)
        self.Converter1ComboBox.addItems(self.list_of_values)
        self.Converter2ComboBox.addItems(self.list_of_values)
        self.update_combobox_labels()
        self.ConvertButton.clicked.connect(self.globalConverter)
        self.ConvertationResult.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LikedInCsvButton.clicked.connect(self.csvLikedSaver)
        self.settingsButton.clicked.connect(self.settingsRunner)

    def settingsRunner(self):
        QMessageBox.information(self, "Information", "This Window is not ready yet. Check up TechTask"
                                                     " for more information.")

    def csvLikedSaver(self):
        try:
            if not self.FilenameLine.text():
                raise FieldsAreNotFilled
            currencies = [el.split()[0] for el in self.liked_values]

            def get_exchange_rate(base, target):
                url = f"https://api.coinbase.com/v2/prices/{base}-{target}/spot"
                response = requests.get(url)
                if response.status_code == 200:
                    return base, target, float(response.json()['data']['amount'])
                else:
                    print(f"Error fetching data for {base}-{target}")
                    return base, target, None

            data = {base: {target: None for target in currencies} for base in currencies}
            with ThreadPoolExecutor(max_workers=10) as executor:
                tasks = []
                for base in currencies:
                    for target in currencies:
                        if base != target:
                            tasks.append((base, target))
                for base, target, rate in executor.map(lambda args: get_exchange_rate(*args), tasks):
                    data[base][target] = rate
            for base in currencies:
                data[base][base] = 1.0
            filename = self.FilenameLine.text().replace(" ", "")
            if filename[-4::] != ".csv":
                filename += ".csv"
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow(["Value"] + currencies)
                for base in currencies:
                    row = [base]
                    for target in currencies:
                        rate = data[base][target]
                        if rate is not None:
                            row.append(round(rate, 6))
                        else:
                            row.append('N/A')
                    writer.writerow(row)
            QMessageBox.about(self, "Completing", "Process completed!")
        except FieldsAreNotFilled:
            QMessageBox.critical(self, "Error", "You should fill Filename label!")

    def update_selected_options(self):
        if self.sender().isChecked() and self.sender().text() not in self.liked_values:
            self.liked_values.append(self.sender().text())
        elif not self.sender().isChecked():
            self.liked_values.remove(self.sender().text())
        conn = sqlite3.connect('databases/users.sqlite')
        cursor = conn.cursor()
        if "null" in self.liked_values:
            self.liked_values.remove("null")
        if "" in self.liked_values:
            self.liked_values.remove("")
        new_text = ", ".join(self.liked_values)
        cursor.execute(f"""
                    INSERT INTO favorite_values_table (id, favoriteValues) VALUES ({self.id}, ?) 
                    ON CONFLICT(id) DO UPDATE SET favoriteValues = ?""", (new_text, new_text))
        conn.commit()
        conn.close()
        self.update_combobox_labels()

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
                                            XtoYconverter(self.Converter2ComboBox.currentText().split()[0],
                                                          self.DoubleSpinConverterBox.value())))

    def viewRunner(self):
        if self.FilenameLine.text():
            self.viewOpener = ViewWindow(self.FilenameLine.text())
            self.viewOpener.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "You should fill Filename label!")

    def checkerForAbilityValues(self):
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

    def ComboBox2ValuesChooser(self):
        if self.Value2ComboBox.currentText():
            self.loadingOpener = LoadingWindow()
            self.loadingOpener.show()
            self.hide()
            QtTest.QTest.qWait(2000)
            self.value1Logo = QPixmap(f"flags/{self.Value1ComboBox.currentText().split()[0]}.png")
            self.Value1Flag.setPixmap(self.value1Logo)
            self.Value2ComboBox.clear()
            self.checkerForAbilityValues()
            self.Value2ComboBox.addItems(self.list_values_combobox2)
            QtTest.QTest.qWait(2000)
            self.show()
            self.loadingOpener.close()

    def CurrencyTurner(self):
        if self.Value2ComboBox.currentText():
            self.value2Logo = QPixmap(f"flags/{self.Value2ComboBox.currentText().split()[0]}.png")
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
            ax.set_title(f'Graphics {pair}')
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


class ViewWindow(QDialog):
    def __init__(self, filename):
        try:
            super(QDialog, self).__init__()
            file = io.StringIO(ViewWindowTemplate)
            uic.loadUi(file, self)
            self.setWindowTitle("ViewWindow")
            self.setFixedSize(1060, 502)
            self.UnitedMainReopener = None
            if filename[-4::] != ".csv":
                filename += ".csv"
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                data = list(reader)
            self.UnitedMainReopener = None
            self.ViewTable.setColumnCount(
                len(data[0]))
            self.ViewTable.setRowCount(len(data))
            for row_index, row_data in enumerate(data):
                for col_index, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(cell_data)
                    self.ViewTable.setItem(row_index, col_index, item)
            header = self.ViewTable.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.ViewTable.resizeRowsToContents()
        except Exception as error:
            pass

    def closeEvent(self, event):
        self.UnitedMainReopener = UnitedChangerMainWindow()
        self.UnitedMainReopener.show()


class LoadingWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        file = io.StringIO(LoadingWindowTemplate)
        uic.loadUi(file, self)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setDisabled(True)
        self.movie = QMovie("load-loading.gif")
        self.loadingGifLabel.setMovie(self.movie)
        self.movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ProgressWindow = ProgressBarWindow()
    ProgressWindow.show()
    ProgressWindow.progressBarChanger()
    LoginWindowApp = LoginWindow()
    LoginWindowApp.show()
    ProgressWindow.finish(LoginWindowApp)
    app.exec()
