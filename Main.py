from PyQt6 import QtWidgets
import Gui



if __name__ == '__main__':
    #hello
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    KeyCalc = QtWidgets.QMainWindow()
    ui = Gui.App()
    ui.setupUi(KeyCalc)
    KeyCalc.setFixedSize(KeyCalc.size())
    KeyCalc.show()
    sys.exit(app.exec())