from PassWin.PassWinUse import *
import sys

class Main:
    app = QtWidgets.QApplication(sys.argv)
    dialog = PassWin()
    dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
    dialog.show()
    app.exec()