# import module PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

# bikin objek aplikasi dan window nya
app = QApplication([])
main_win = QWidget()

# title and size
main_win.setWindowTitle('Quiz App')
main_win.resize(400, 200)

# widget
question = QLabel("What year was Algorithmics founded in?")
ans1 = QRadioButton('2013')
ans2 = QRadioButton('2016')
ans3 = QRadioButton('2010')
ans4 = QRadioButton('2019')

# layout
h_layout = QHBoxLayout()
h_layout1 = QHBoxLayout()
h_layout2 = QHBoxLayout()

h_layout.addWidget(question, alignment=Qt.AlignCenter)

# horizontal layout 1
h_layout1.addWidget(ans1, alignment=Qt.AlignCenter)
h_layout1.addWidget(ans3, alignment=Qt.AlignCenter)

# horizontal layout 2
h_layout2.addWidget(ans2, alignment=Qt.AlignCenter)
h_layout2.addWidget(ans4, alignment=Qt.AlignCenter)

# vertical layout
v_layout = QVBoxLayout()

# add layout
v_layout.addLayout(h_layout)
v_layout.addLayout(h_layout1)
v_layout.addLayout(h_layout2)

main_win.setLayout(v_layout)

# function right and wrong
def show_right():
    right = QMessageBox()
    right.setText('Right')
    right.exec_()

def show_wrong():
    wrong = QMessageBox()
    wrong.setText('Wrong')
    wrong.exec_()

ans2.clicked.connect(show_right)

ans1.clicked.connect(show_wrong)
ans3.clicked.connect(show_wrong)
ans4.clicked.connect(show_wrong)

# run the app
main_win.show() # show the app
app.exec_() # open the app until click close button