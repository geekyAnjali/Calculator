from Addion_calculator import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

class main_ui(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.Add_bttn.clicked.connect(self.cal_add)
        self.Clr_bttn.clicked.connect(self.clr_rslt)

    
    def cal_add(self):
        self.addition_ = int(self.Num1_input.text()) + int(self.Num2_input.text()) + int(self.Num3_input.text())
        self.rslt_bx.setText(str(self.addition_))
        print(self.addition_)
    def clr_rslt(self):
        self.rslt_bx.setText("")

            
if __name__ == '__main__':
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    obj = main_ui()
    obj.show()
    sys.exit(app.exec_())
        