from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton, 
        QPushButton, QLabel)
from random import shuffle

class Question():
        def __init__(self, _q, _r, _w1, _w2, _w3):
                self.q = _q
                self.r = _r
                self.w1 =_w1
                self.w2 = _w2
                self.w3 = _w3
q1=Question("In what year was the great fire of London?", "1666", "1999", "1062", "666")
q2=Question("In what year was Moscow founded?", "1047", "1666", "147", "2012")
q3=Question("What is the powerhouse of the cell?", "mytochondria", "heart", "nucleus", "oven")
q4=Question("What is Force divided by mass?", "acceleration", "distance", "power", "speed")
q5=Question("What is the integral of sin(x)?", "-cos(x)", "tan(x)", "cos(x)", "-sin(x)")
score = 0
q_list = [q1,q2,q3,q4,q5]

def nextQst():
        global score
        if len(q_list)>0:
                shuffle(q_list)
                main_win.counter = main_win.counter+1
                if main_win.counter>=len(q_list):
                        main_win.counter = 0
                ask(q_list[main_win.counter])
                q_list.remove(q_list[main_win.counter])
        else:
                gbox1.hide()
                gbox2.show()
                label1.hide()
                label3.hide()
                gbox2.setTitle("Score:")
                label2.setText(str(score)+"/5")
                but1.setText("Quit")
def show_ans():
        global score
        gbox1.hide()
        gbox2.show()
        but1.setText("Next Question")
        if bList[0].isChecked():
                label2.setText("Correct!")
                score +=1
        else:
                label2.setText("Incorrect! The correct answer was: ")
def show_qst():
        gbox2.hide()
        gbox1.show()
        but1.setText("Answer")
        RadioGroup.setExclusive(False)
        b1.setChecked(False)
        b2.setChecked(False)
        b3.setChecked(False)
        b4.setChecked(False)
        RadioGroup.setExclusive(True)
def test():
        if but1.text() == "Answer":
                show_ans()
        elif but1.text() == "Quit":
                app.quit()
        else:
                nextQst()
def ask(q: Question):
        shuffle(bList)
        label1.setText(q.q)
        bList[0].setText(q.r)
        bList[1].setText(q.w1)
        bList[2].setText(q.w2)
        bList[3].setText(q.w3)
        label3.setText(q.r)
        show_qst()
 
 
app=QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card App")
main_win.move(400,300)
main_win.resize(400,300)
main_win.counter = -1
label1 = QLabel("--A very difficult question goes here.--")
gbox1=QGroupBox("Answer options")
gbox2=QGroupBox("Correct answer:")
label2 =QLabel("Correct/Incorrect")
label3 =QLabel("Correct answer goes here")
vline4 =QVBoxLayout()
vline4.addWidget(label2)
vline4.addWidget(label3)
gbox2.setLayout(vline4)
RadioGroup = QButtonGroup()
b1=QRadioButton("Option 1")
b2=QRadioButton("Option 2")
b3=QRadioButton("Option 3")
b4=QRadioButton("Option 4")
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)
but1 = QPushButton("Answer")
bList = [b1, b2, b3, b4]
 
vline1=QVBoxLayout()
vline2=QVBoxLayout()
vline3=QVBoxLayout()
hline1=QHBoxLayout()
 
vline1.addWidget(label1, alignment=Qt.AlignCenter)
vline1.addWidget(gbox1)
vline1.addWidget(gbox2)
vline1.addWidget(but1, stretch=3)
 
vline2.addWidget(b1)
vline2.addWidget(b2)
vline3.addWidget(b3)
vline3.addWidget(b4)
hline1.addLayout(vline2)
hline1.addLayout(vline3)
gbox1.setLayout(hline1)
main_win.setLayout(vline1)

gbox2.hide()
nextQst()
but1.clicked.connect(test)
main_win.show()
app.exec()
