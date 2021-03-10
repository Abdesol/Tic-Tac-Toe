from PyQt5 import QtWidgets, QtGui, QtCore
import math, sys, random


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


        self.tic_tac_lst = [[None for i in range(3)] for j in range(3)]
        def who_won(data):
            pos_1 = [i[0] for i in data]
            pos_2 = [i[1] for i in data]
            pos_3 = [i[2] for i in data]
            pos_4 = data[0]
            pos_5 = data[1]
            pos_6 = data[2]
            pos_7 = []
            pos_8 = []
            i_ = 0
            j_ = 2
            for i in data:
                pos_7.append(i[i_])
                pos_8.append(i[j_])
                i_ += 1
                j_ -= 1
            all_pos = [pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8]
            for p in all_pos:
                if p[0] != None:
                    init = p[0]
                    init_lst = []
                    for i in p:
                        if i != init:
                            break
                        else:
                            init_lst.append(i)
                    if len(init_lst) == 3:
                        return [p, all_pos.index(p)+1]
            return False

        def comp_play(data):
            none_data = []
            for i in data:
                for j in i:
                    if j == None:
                        d = [data.index(i), i.index(j)]
                        none_data.append(d)
            try:
                rand = random.choice(none_data)
                return rand
            except:
                return None
            

        self.is_done = False
        def tic_btn_click(index):
            if self.is_done != True:
                if self.tic_tac_lst[index[0]][index[1]] == None:
                    btn = self.tic_lst[index[0]][index[1]]
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
                    self.tic_tac_lst[index[0]][index[1]] = 1
                    result = who_won(self.tic_tac_lst)
                    if result == False:
                        comp = comp_play(self.tic_tac_lst)
                        if comp != None:
                            self.tic_tac_lst[comp[0]][comp[1]] = 0
                            btn_comp = self.tic_lst[comp[0]][comp[1]]                          
                            btn_comp.setText("O")
                            btn_comp.setStyleSheet("""
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
                            result_again = who_won(self.tic_tac_lst)
                            if result_again == False:
                                pass
                            else:
                                self.turn_label.setText("Computer won")
                                self.turn_label.repaint()
                                self.is_done = True
                    else:
                        self.turn_label.setText("You won")
                        self.turn_label.repaint()
                        self.is_done = True

        self.tic_widget = QtWidgets.QWidget()
        def create_tic_box():
            self.tic_widget.deleteLater()
            self.tic_widget = QtWidgets.QWidget()
            vertical_lay = QtWidgets.QVBoxLayout(self.tic_widget)
            for i in range(3):
                horizontal_layout = QtWidgets.QHBoxLayout()
                local_lst = []
                for j in range(3):
                    tic_box = QtWidgets.QPushButton()
                    tic_box.setFixedSize(int(self.win_width/4), int(self.win_height/6))
                    tic_box.clicked.connect(lambda checked, i=[i,j]:tic_btn_click(i))
                    horizontal_layout.addWidget(tic_box)
                    local_lst.append(tic_box)
                self.tic_lst.append(local_lst)
                vertical_lay.addLayout(horizontal_layout)
            self.mainlay.addWidget(self.tic_widget)
            

        create_tic_box()
        def reset_clicked():
            self.is_done = False
            self.tic_lst = []
            self.tic_tac_lst = [[None for i in range(3)] for j in range(3)]
            self.turn_label.setText("Game Started")
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