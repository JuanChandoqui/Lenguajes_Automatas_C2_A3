import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/init.ui', self)
        self.photo_background.setPixmap(QtGui.QPixmap('./Resources/bandera_mexico.jpg'))
        self.button_search.clicked.connect(self.isClickedButtonSearch)
        self.button_exit.clicked.connect(self.close)
    
    
    def isClickedButtonSearch(self):
        text = self.textField_text.text()
        input_text = list(text)
        status = True

        if(status):
            self.label_status.setText('CURP VÁLIDA / CURP DISPONIBLE')
            self.label_status.setStyleSheet('background-color: green; color: white; font-size: 12px; font-weight: bold')
        else:
            self.label_status.setText('CURP INVÁLIDA!')
            self.label_status.setStyleSheet('background-color: red; color: white; font-size: 12px; font-weight: bold')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')