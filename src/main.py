import sys
import time
import validate_email
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtTest
from PyQt6.QtWidgets import QApplication, QDialog, QSplashScreen, QMessageBox


class DifferentPasswords(Exception):
    pass


class NotValidEmail(Exception):
    pass


class FieldsAreNotFilled(Exception):
    pass


class ProgressBarWindow(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("ProgressbarWindow.ui", self)
        self.time_for_sleep = 0
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.pixmapBackground = QPixmap("splashGradient.png")
        self.setPixmap(self.pixmapBackground)
        self.pixmapLogo = QPixmap("splashLogo.png")
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


class LoginWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("LoginWindow.ui", self)
        self.registrationProcess = None
        self.runRememberingProcess = None
        self.setWindowTitle("Login to UnitedChanger")
        self.pixmapLogo = QPixmap("LoginWindowLogo.png")
        self.LabelLogo.setPixmap(self.pixmapLogo)
        self.RegistrationButton.clicked.connect(self.runRegisterWindow)
        self.ForgotPasswordButton.clicked.connect(self.runForgotPasswordWindow)

    def runRegisterWindow(self):
        self.registrationProcess = RegisterWindow()
        self.registrationProcess.show()
        self.close()

    def runForgotPasswordWindow(self):
        self.runRememberingProcess = ForgotPasswordWindow()
        self.runRememberingProcess.show()
        self.close()


class RegisterWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("RegisterWindow.ui", self)
        self.LoginWindowReopener = None
        self.setWindowTitle("Registration")

        self.RegisterButton.clicked.connect(self.registration)

    def zeroMaker(self):
        self.PasswordEntery.setText("")
        self.PasswordEnteryAgain.setText("")
        self.LoginEntery.setText("")

    def registration(self):
        try:
            if not all([self.PasswordEntery.text(), self.PasswordEnteryAgain.text(), self.LoginEntery.text()]):
                print(1)
                raise FieldsAreNotFilled
            if not validate_email.validate_email(self.LoginEntery.text()):
                print(2)
                raise NotValidEmail
            if not self.PasswordEntery.text() == self.PasswordEnteryAgain.text():
                print(3)
                raise DifferentPasswords
        except FieldsAreNotFilled:
            #!!! Добавь предупреждения
            self.zeroMaker()
        except DifferentPasswords:
            # !!!
            self.zeroMaker()
        except NotValidEmail:
            # !!!
            self.zeroMaker()

    def closeEvent(self, event):
        self.LoginWindowReopener = LoginWindow()
        self.LoginWindowReopener.show()


class ForgotPasswordWindow(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("ForgotPasswordWindow.ui", self)
        self.LoginWindowReopener = None
        self.setWindowTitle("Don't forget you password again =)")

    def closeEvent(self, event):
        self.LoginWindowReopener = LoginWindow()
        self.LoginWindowReopener.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ProgressWindow = ProgressBarWindow()
    ProgressWindow.show()
    ProgressWindow.progressBarChanger()
    LoginWindowApp = LoginWindow()
    LoginWindowApp.show()
    ProgressWindow.finish(LoginWindowApp)
    app.exec()
