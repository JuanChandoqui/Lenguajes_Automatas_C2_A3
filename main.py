import sys
import os
import numpy as np
import img2pdf
import glob
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui
from Controllers.information_controller import WindowInformation
from Models.read_csv import readCSVCurps
from Models.write_csv import writeCSVFile
from matplotlib import pyplot

from Models.read_regex import readRegex

curp_text = ''
data_statics = readCSVCurps()
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/init.ui', self)
        self.button_show_information.hide()
        self.photo_background.setPixmap(QtGui.QPixmap('./Resources/Images/bandera_mexico.jpg'))
        self.button_search.clicked.connect(self.isClickedButtonSearch)
        self.button_exit.clicked.connect(self.close)
        self.button_show_information.clicked.connect(self.isClickedButtonShowInformation)
        self.button_meses_nacimientos.clicked.connect(self.barMonthWithMoreBirth)       
        self.button_entidad_registros.clicked.connect(self.barFederalEntitys)
        self.button_edad_personas.clicked.connect(self.pieAgePerson)
        self.button_sexo.clicked.connect(self.pieSex)
        self.button_open_PDF.clicked.connect(self.generatePDFReport)
        

    def isClickedButtonSearch(self):
        global curp_text
        text = self.textField_text.text()
        text = text.replace(' ', '')
        curp_text = text
        status = readRegex(text)

        writeCSVFile(status, curp_text)

        if(status):
            self.button_show_information.show()
            self.label_status.setText('CURP VÁLIDA / CURP DISPONIBLE')
            self.label_status.setStyleSheet('background-color: green; color: white; font-size: 12px; font-weight: bold')
        else:
            self.button_show_information.hide()
            self.label_status.setText('CURP INVÁLIDA!')
            self.label_status.setStyleSheet('background-color: red; color: white; font-size: 12px; font-weight: bold')
    
    def isClickedButtonShowInformation(self):
        global curp_text
        w = WindowInformation(curp_text)
        self.demo = w
        self.demo.show()

    #-------GRAPHICS---------------------------------------
    def barMonthWithMoreBirth(self):
        global data_statics

        x = data_statics[2].keys()
        y = data_statics[2].values()

        fig, ax = pyplot.subplots()    
        width = 0.75 
        ind = np.arange(len(y))  
        ax.barh(ind, y, width, color="black")
        ax.set_yticks(ind+width/2)
        ax.set_yticklabels(x, minor=False)
        for i, v in enumerate(y):
            ax.text(v + 3, i + .25, str(v), color='black')

        pyplot.title('Meses con mas nacimientos')
        pyplot.xlabel('Personas')     
        pyplot.show()
        pyplot.savefig(os.path.join('./Resources/Statistics/month_with_more_birth.png'), dpi=300, format='png', bbox_inches='tight') 

    
    def barFederalEntitys(self):
        global data_statics

        x = data_statics[1].keys()
        y = data_statics[1].values()

        fig, ax = pyplot.subplots()    
        width = 0.75 
        ind = np.arange(len(y))  
        ax.barh(ind, y, width, color="blue")
        ax.set_yticks(ind+width/2)
        ax.set_yticklabels(x, minor=False)
        for i, v in enumerate(y):
            ax.text(v + 3, i + .25, str(v), color='blue')

        pyplot.title('Entidades Federativas')
        pyplot.xlabel('Personas')     
        pyplot.show()
        pyplot.savefig(os.path.join('./Resources/Statistics/federal_entitys.png'), dpi=300, format='png', bbox_inches='tight') 

    
    def pieAgePerson(self):
        global data_statics

        x = data_statics[3].keys()
        y = data_statics[3].values()

        fig, ax = pyplot.subplots()    
        width = 0.75 
        ind = np.arange(len(y))  
        ax.barh(ind, y, width, color="green")
        ax.set_yticks(ind+width/2)
        ax.set_yticklabels(x, minor=False)
        for i, v in enumerate(y):
            ax.text(v + 3, i + .25, str(v), color='green')

        pyplot.title('Meses con mas nacimientos')
        pyplot.xlabel('Personas')     
        pyplot.show()
        pyplot.savefig(os.path.join('./Resources/Statistics/pie_age_person.png'), dpi=300, format='png', bbox_inches='tight')

    
    def pieSex(self):
        global data_statics

        value_1 = data_statics[0].values()
        value_2 = data_statics[0].keys()
        pyplot.pie(value_1, labels= value_2, autopct='%.2f %%')
        pyplot.show()
        pyplot.savefig(os.path.join('./Resources/Statistics/sex_statics.png'), dpi=300, format='png', bbox_inches='tight')

    
    def generatePDFReport(self):
        PATH = "report_statistics.pdf"
        with open(PATH,"wb") as f:
            f.write(img2pdf.convert(glob.glob("./Resources/Statistics/*.png")))
        os.system(PATH)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')