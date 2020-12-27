from PyQt5.QtWidgets import QFileDialog, QToolTip
from PyQt5 import QtCore, QtGui, QtWidgets
import random
from main2 import Ui_MainWindow  # импорт нашего сгенерированного файла
from main import Main
import sys

try:
    class mywindow(QtWidgets.QMainWindow):
        def __init__(self):
            paswrds = []
            pasw_simv = ["a", "U", "J", "2", "!", "90", "lx", "t3", "rox", "joh54", "11", "!$", "f", "o", "py3", "itug", "F", "DHH", "E", "33EE", "KOLOT", "IUIHIH", "IHjhhiIO"]
            for i in range(10):
                paswrds.append(random.choice(pasw_simv))
            self.passw = "".join(paswrds)
            print(self.passw)
            self.fnames = []
            self.lnames = []
            self.emails = []
            self.ua = []
            self.proxys = []
        
            self.genders = ["Муж", "Жен"]
            super(mywindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.get_fname)
            self.ui.pushButton_2.clicked.connect(self.get_lname)
            self.ui.pushButton_3.clicked.connect(self.get_email)
            self.ui.pushButton_5.clicked.connect(self.start)
            self.ui.pushButton_6.clicked.connect(self.get_UA)
            self.ui.pushButton_4.clicked.connect(self.get_proxy)

        def get_fname(self):
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            print(fname)
            with open(fname, 'r') as file:
                for line in file.read().splitlines():
                    self.fnames.append(line)
                    if len(self.fnames) > 1:
                        self.fnames.pop(0)
    
        def get_lname(self):
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            print(fname)
            with open(fname, 'r') as file:
                for line in file.read().splitlines():
                    self.lnames.append(line)
                    if len(self.lnames) > 1:
                        self.lnames.pop(0)

        def get_email(self):
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            with open(fname, 'r') as file:
                user_attributes = [line for line in file.read().splitlines()]
                self.emails.append(user_attributes)
                if len(self.emails) > 1:
                    self.emails.pop(0)
        def get_UA(self):
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            with open(fname, 'r') as file:
                for line in file.read().splitlines():
                    self.ua.append(line)
                    if len(self.ua) > 1:
                        self.ua.pop(0)
        def get_proxy(self):
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            with open(fname, 'r') as file:
                for line in file.read().splitlines():
                    self.proxys.append(line)
                    if len(self.proxys) > 1:
                        self.proxys.pop(0)
        def start(self):
            email_ne = random.choice(self.emails)
            for gt in email_ne:
                self.email_new = gt
            #print(self.email_new.split(':')[1])
            main = Main(random.choice(self.fnames), random.choice(self.lnames), self.email_new.split(':')[0], self.email_new.split(':')[1], self.passw, 3, 4, 7, random.choice(self.genders), random.choice(self.ua))
        
       
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
 
    sys.exit(app.exec())

except IndexError:
    pass

'''random.choice(self.proxys)'''