from PyQt5 import QtWidgets, QtGui, QtCore
from win32api import GetSystemMetrics
import math, time, threading, sys


class Ui_MainWindow(object):
    def __init__(self, MainWindow, win_width, win_height):
        self.win_width = int(round(win_width*32)/100)
        self.win_height = int(round(win_height*70)/100)
        # Main Windows Config
        self.MainWindow = MainWindow
        self.MainWindow.setFixedSize(self.win_width, self.win_height)
        self.MainWindow.setWindowTitle('Tic Tac Toe')

        QtGui.QFontDatabase.addApplicationFont("./fonts/Poppins-Medium.ttf")

        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setStyleSheet("""
        QWidget {
            background-color: #303842;
        }
        QLabel {
            font-family: 'Poppins', sans-serif;
            font-size: 25px;
        }
        QPushButton {
            border-radius: 5px;
            background-color: #222730;
        }
        QPushButton:hover {
            background-color: #181E28;
        }
        QPushButton:pressed {
            background-color: transparent;
        }
        """)
        self.mainlay = QtWidgets.QVBoxLayout(self.centralWidget)

        def font_size_finder(per):
            return int((math.sqrt(self.win_width*self.win_height)*per)/100)

        title_label = QtWidgets.QLabel()
        title_label.setText("Tic Tac Toe")
        title_font = font_size_finder(9)
        title_label.setStyleSheet(f"font-size: {title_font}px")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mainlay.addWidget(title_label)

        def reset_clicked():
            self.tic_lst = []
            create_tic_box()
        
        self.reset_btn = QtWidgets.QPushButton()
        self.reset_btn.setText("Reset")
        self.reset_lay = QtWidgets.QHBoxLayout()
        self.reset_btn.setFixedSize(int(self.win_width/4), int(self.win_height/12))
        self.reset_btn.setStyleSheet("""
        QPushButton {
            background-color: #22252A;
            font-size: 17px;
        }
        QPushButton:hover {
            background-color: #1B2029;
        }
        QPushButton:pressed {
            background-color: #14181F;
        }
        """)
        self.reset_lay.addStretch(7)
        self.reset_lay.addWidget(self.reset_btn)
        self.reset_lay.addStretch(1)
        self.mainlay.addLayout(self.reset_lay)
        self.turn_label = QtWidgets.QLabel()
        self.turn_label.setText("Game Started")
        self.turn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mainlay.addWidget(self.turn_label)
        self.tic_lst = []
        def tic_btn_click(index):
            
            for i in self.tic_lst:
                if i[0] == index:
                    btn = i[1]
                    btn.setText("X")
                    btn.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        font-size: 30px;
                        font-family: 'Poppins', sans-serif;
                    }
                    QPushButton:hover {
                        background-color: transparent;
                    }
                    QPushButton:pressed {
                        background-color: transparent;
                    }  
                    """)
                    break

        self.tic_widget = QtWidgets.QWidget()
        def create_tic_box():
            self.tic_widget.deleteLater()
            self.tic_widget = QtWidgets.QWidget()
            vertical_lay = QtWidgets.QVBoxLayout(self.tic_widget)
            for i in range(1,4):
                horizontal_layout = QtWidgets.QHBoxLayout()
                #local_threads = []
                for j in range(1,4):
                    tic_box = QtWidgets.QPushButton()
                    tic_box.setFixedSize(int(self.win_width/4), int(self.win_height/6))
                    tic_box.clicked.connect(lambda checked, i=[i,j]:tic_btn_click(i))
                    horizontal_layout.addWidget(tic_box)
                    self.tic_lst.append([[i,j],tic_box])
                vertical_lay.addLayout(horizontal_layout)
            self.mainlay.addWidget(self.tic_widget)
            

        create_tic_box()
        def reset_clicked():
            self.tic_lst = []
            create_tic_box()
        self.reset_btn.clicked.connect(lambda: reset_clicked())
        
        self.MainWindow.setCentralWidget(self.centralWidget)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    resolution = app.desktop().screenGeometry()
    w = resolution.width()
    h = resolution.height()
    ui = Ui_MainWindow(MainWindow, w, h)
    
    MainWindow.show()
    sys.exit(app.exec_())