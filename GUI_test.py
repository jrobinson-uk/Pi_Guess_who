import sys
from PyQt4 import QtGui #imports

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        leftTop=QtGui.QFrame(self)
        leftTop.setFrameShape(QtGui.QFrame.StyledPanel)
        leftBottom=QtGui.QFrame(self)
        leftBottom.setFrameShape(QtGui.QFrame.StyledPanel)
        right=QtGui.QFrame(self)
        right.setFrameShape(QtGui.QFrame.StyledPanel)
        grid.addWidget(leftTop,1,1,5,6)
        grid.addWidget(leftBottom,6,1,1,6)
        grid.addWidget(right,1,7,6,2)
       
            
        self.setLayout(grid)
        self.setGeometry(30,30,1024,768)
        self.setWindowTitle('Pi Guess  Who')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show()

def main():
    app = QtGui.QApplication(sys.argv) # define app using system arguments

    ex = Example()
    sys.exit(app.exec())    #enter main loop for the app

if __name__ == '__main__':
    main()
