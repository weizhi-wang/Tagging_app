import sys
import tag
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from maincode import MainCode

if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())
