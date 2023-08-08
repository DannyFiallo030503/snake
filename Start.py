from Interface.Screens import main_screen
import sys
sys.path.append('Interface/Interface_Qt')
from Main_Screen import Ui_MainWindow
from PyQt5 import QtWidgets

#Class que crea la pantalla principal del juego con qt
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec_()

main_screen()  