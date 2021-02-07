from PyQt5 import QtWidgets, QtGui, QtCore

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        # Main Windows Config
        self.MainWindow = MainWindow
        self.MainWindow.setFixedSize(430, 500)
        self.MainWindow.setWindowTitle('Tic Tac Toe')
        self.centralWidget = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)

        title_label = QtWidgets.QLabel()
        title_label.setText("Tic Tac Toe")
        title_label
        self.verticalLayout.addWidget(title_label)



        self.MainWindow.setCentralWidget(self.centralWidget)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())