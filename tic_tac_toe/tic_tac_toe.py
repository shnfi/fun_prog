import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(300, 300)
        
        self.setStyleSheet("""
            background-color: #2D336B;
        """)
        
        self.turn = "x"

        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
        
        # main window widgets
        
        self.main_widget = QWidget(self)
        self.main_layout = QVBoxLayout(self.main_widget)
        
        self.setCentralWidget(self.main_widget)
        
        # rows
        
        self.row_1_widget = QWidget()
        self.row_1_layout = QHBoxLayout(self.row_1_widget)
        self.row_1_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.row_1_widget)
        
        self.row_2_widget = QWidget()
        self.row_2_layout = QHBoxLayout(self.row_2_widget)
        self.row_2_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.row_2_widget)
        
        self.row_3_widget = QWidget()
        self.row_3_layout = QHBoxLayout(self.row_3_widget)
        self.row_3_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.row_3_widget)
        
        # cols
        
        self.col_1_1_button = QPushButton()
        self.col_1_1_button.setFixedHeight(90)

        self.col_1_2_button = QPushButton()
        self.col_1_2_button.setFixedHeight(90)

        self.col_1_3_button = QPushButton()
        self.col_1_3_button.setFixedHeight(90)

        self.col_2_1_button = QPushButton()
        self.col_2_1_button.setFixedHeight(90)

        self.col_2_2_button = QPushButton()
        self.col_2_2_button.setFixedHeight(90)

        self.col_2_3_button = QPushButton()
        self.col_2_3_button.setFixedHeight(90)

        self.col_3_1_button = QPushButton()
        self.col_3_1_button.setFixedHeight(90)

        self.col_3_2_button = QPushButton()
        self.col_3_2_button.setFixedHeight(90)

        self.col_3_3_button = QPushButton()
        self.col_3_3_button.setFixedHeight(90)

        self.row_1_layout.addWidget(self.col_1_1_button)
        self.row_1_layout.addWidget(self.col_1_2_button)
        self.row_1_layout.addWidget(self.col_1_3_button)
        
        self.row_2_layout.addWidget(self.col_2_1_button)
        self.row_2_layout.addWidget(self.col_2_2_button)
        self.row_2_layout.addWidget(self.col_2_3_button)
        
        self.row_3_layout.addWidget(self.col_3_1_button)
        self.row_3_layout.addWidget(self.col_3_2_button)
        self.row_3_layout.addWidget(self.col_3_3_button)
        
        # buttons connect
        
        self.col_1_1_button.clicked.connect(self.col_1_1_turnon)
        self.col_1_2_button.clicked.connect(self.col_1_2_turnon)
        self.col_1_3_button.clicked.connect(self.col_1_3_turnon)
        self.col_2_1_button.clicked.connect(self.col_2_1_turnon)
        self.col_2_2_button.clicked.connect(self.col_2_2_turnon)
        self.col_2_3_button.clicked.connect(self.col_2_3_turnon)
        self.col_3_1_button.clicked.connect(self.col_3_1_turnon)
        self.col_3_2_button.clicked.connect(self.col_3_2_turnon)
        self.col_3_3_button.clicked.connect(self.col_3_3_turnon)
        
        self.col_1_1_button.setStyleSheet("""
            QPushButton {
                color: #2D336B;
                background-color: #7886C7;
                font-size: 30px;
            }
        """)

        self.col_1_2_button.setStyleSheet("""
            QPushButton {
                color: #2D336B;
                background-color: #7886C7;
                font-size: 30px;
            }
        """)

        self.col_1_3_button.setStyleSheet("""
            QPushButton {
                color: #2D336B;
                background-color: #7886C7;
                font-size: 30px;
            }
        """)
        
        self.col_2_1_button.setStyleSheet("""
            QPushButton {
                color: #2D336B;
                background-color: #7886C7;
                font-size: 30px;
            }
        """)
        
        self.col_2_2_button.setStyleSheet("""
            QPushButton {
                color: #2D336B;
                background-color: #7886C7;
                font-size: 30px;
            }
        """)
        
        self.col_2_3_button.setStyleSheet("""
            QPushButton {
                color: #2D336B;
                background-color: #7886C7;
                font-size: 30px;
            }
        """)
        
        self.col_3_1_button.setStyleSheet("""
            QPushButton {
                color: #2D336B;
                background-color: #7886C7;
                font-size: 30px;
            }
        """)
        
        self.col_3_2_button.setStyleSheet("""
            QPushButton {
                color: #2D336B;
                background-color: #7886C7;
                font-size: 30px;
            }
        """)
        
        self.col_3_3_button.setStyleSheet("""
            QPushButton {
                color: #2D336B;
                background-color: #7886C7;
                font-size: 30px;
            }
        """)
        
        # end
        
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 1)
        self.main_layout.setStretch(2, 1)
        
        self.row_1_layout.setStretch(0, 1)
        self.row_1_layout.setStretch(1, 1)
        self.row_1_layout.setStretch(2, 1)
        
        self.row_2_layout.setStretch(0, 1)
        self.row_2_layout.setStretch(1, 1)
        self.row_2_layout.setStretch(2, 1)
        
        self.row_3_layout.setStretch(0, 1)
        self.row_3_layout.setStretch(1, 1)
        self.row_3_layout.setStretch(2, 1)
    
    def col_1_1_turnon(self) :
        if (self.turn == "x") :
            self.col_1_1_button.setText("X")
            self.board[0][0] = "x";
            self.turn = "o"
        else :
            self.col_1_1_button.setText("O")
            self.board[0][0] = "o";
            self.turn = "x"
        
        self.col_1_1_button.setEnabled(False)
        self.check_winner()

    def col_1_2_turnon(self) :
        if (self.turn == "x") :
            self.col_1_2_button.setText("X")
            self.board[0][1] = "x";
            self.turn = "o"
        else :
            self.col_1_2_button.setText("O")
            self.board[0][1] = "o";
            self.turn = "x"
        
        self.col_1_2_button.setEnabled(False)
        self.check_winner()

    def col_1_3_turnon(self) :
        if (self.turn == "x") :
            self.col_1_3_button.setText("X")
            self.board[0][2] = "x";
            self.turn = "o"
        else :
            self.col_1_3_button.setText("O")
            self.board[0][2] = "o";
            self.turn = "x"
        
        self.col_1_3_button.setEnabled(False)
        self.check_winner()

    def col_2_1_turnon(self) :
        if (self.turn == "x") :
            self.col_2_1_button.setText("X")
            self.board[1][0] = "x";
            self.turn = "o"
        else :
            self.col_2_1_button.setText("O")
            self.board[1][0] = "o";
            self.turn = "x"
        
        self.col_2_1_button.setEnabled(False)
        self.check_winner()

    def col_2_2_turnon(self) :
        if (self.turn == "x") :
            self.col_2_2_button.setText("X")
            self.board[1][1] = "x";
            self.turn = "o"
        else :
            self.col_2_2_button.setText("O")
            self.board[1][1] = "o";
            self.turn = "x"
        
        self.col_2_2_button.setEnabled(False)
        self.check_winner()

    def col_2_3_turnon(self) :
        if (self.turn == "x") :
            self.col_2_3_button.setText("X")
            self.board[1][2] = "x";
            self.turn = "o"
        else :
            self.col_2_3_button.setText("O")
            self.board[1][2] = "o";
            self.turn = "x"
        
        self.col_2_3_button.setEnabled(False)
        self.check_winner()

    def col_3_1_turnon(self) :
        if (self.turn == "x") :
            self.col_3_1_button.setText("X")
            self.board[2][0] = "x";
            self.turn = "o"
        else :
            self.col_3_1_button.setText("O")
            self.board[2][0] = "o";
            self.turn = "x"
        
        self.col_3_1_button.setEnabled(False)
        self.check_winner()

    def col_3_2_turnon(self) :
        if (self.turn == "x") :
            self.col_3_2_button.setText("X")
            self.board[2][1] = "x";
            self.turn = "o"
        else :
            self.col_3_2_button.setText("O")
            self.board[2][1] = "o";
            self.turn = "x"
        
        self.col_3_2_button.setEnabled(False)
        self.check_winner()

    def col_3_3_turnon(self) :
        if (self.turn == "x") :
            self.col_3_3_button.setText("X")
            self.board[2][2] = "x";
            self.turn = "o"
        else :
            self.col_3_3_button.setText("O")
            self.board[2][2] = "o";
            self.turn = "x"
        
        self.col_3_3_button.setEnabled(False)
        self.check_winner()
    
    def check_winner(self) :
        self.msgbx = QMessageBox()
        self.msgbx.setWindowTitle("Game is up!")
        self.msgbx.setText("Winner is...")
        self.msgbx.setIcon(QMessageBox.Icon.Information)

        if (self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]) :
            if (self.board[0][0] != "" and self.board[0][1] != "" and self.board[0][2] != "") :
                self.end_the_game(self.board[0][0])

        elif (self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2]) :
            if (self.board[1][0] != "" and self.board[1][1] != "" and self.board[1][2] != "") :
                self.end_the_game(self.board[1][0])

        elif (self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2]) :
            if (self.board[2][0] != "" and self.board[2][1] != "" and self.board[2][2] != "") :
                self.end_the_game(self.board[2][0])

        elif (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]) :
            if (self.board[0][0] != "" and self.board[1][1] != "" and self.board[2][2] != "") :
                self.end_the_game(self.board[0][0])
        
        elif (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]) :
            if (self.board[0][2] != "" and self.board[1][1] != "" and self.board[2][0] != "") :
                self.end_the_game(self.board[0][2])
        
        elif (self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0]) :
            if (self.board[0][0] != "" and self.board[1][0] != "" and self.board[2][0] != "") :
                self.end_the_game(self.board[2][0])

        elif (self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1]) :
            if (self.board[0][1] != "" and self.board[1][1] != "" and self.board[2][1] != "") :
                self.end_the_game(self.board[0][1])
        
        elif (self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]) :
            if (self.board[0][2] != "" and self.board[1][2] != "" and self.board[2][2] != "") :
                self.end_the_game(self.board[0][2])

        elif (self.is_draw()) :
            self.msgbx.setInformativeText(f"Tied, boring!")
            self.msgbx.show()
            self.lock_all()

    def is_draw(self) :
        if (self.board[0][0] != "" and self.board[0][1] != "" and self.board[0][2] != "" and
            self.board[1][0] != "" and self.board[1][1] != "" and self.board[1][2] != "" and
            self.board[2][0] != "" and self.board[2][1] != "" and self.board[2][2] != "") :
            return True
        else :
            return False

    def end_the_game(self, ex_h) :
        self.msgbx.setInformativeText(f"'{ex_h}' is winner!")
        self.msgbx.show()
        self.lock_all()

    def lock_all(self) :
        self.col_1_1_button.setEnabled(False)
        self.col_1_2_button.setEnabled(False)
        self.col_1_3_button.setEnabled(False)
        self.col_2_1_button.setEnabled(False)
        self.col_2_2_button.setEnabled(False)
        self.col_2_3_button.setEnabled(False)
        self.col_3_1_button.setEnabled(False)
        self.col_3_2_button.setEnabled(False)
        self.col_3_3_button.setEnabled(False)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
