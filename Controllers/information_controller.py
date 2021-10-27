import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtGui

from Services.api_curp import verificationCURP

class WindowInformation(QWidget):

    def __init__(self, curp):
        super().__init__()
        uic.loadUi('Views/information_view.ui', self)
        self.curp = curp

        curp_API = verificationCURP(curp)

        self.button_close.clicked.connect(self.close)

        self.birthdate_label.setText(curp_API['birthdate'])
        self.curp_label.setText(curp_API['curp'])
        self.status_curp_label.setText(curp_API['status_curp'])
        self.name_label.setText(curp_API['names'])
        self.paternal_surname_label.setText(curp_API['paternal_surname'])
        self.mother_maiden_label.setText(curp_API['mothers_maiden_name'])
        self.sex_label.setText(curp_API['sex'])