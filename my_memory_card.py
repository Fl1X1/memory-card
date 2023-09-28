
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup,  QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox

app = QApplication([])
win = QWidget()
win.resize(400,200)

question_text_1 = "Какой национальности не существует?"
question_text_2 = "Самый сложный вопрос в мире"


win.setWindowTitle("Memory Card")
question =QLabel(question_text_1)
true_answer = QLabel("Правильный ответ")
false_answer = QLabel("Неправильный ответ")
answer_before = QLabel("Правильно/Неправильно")

button = QPushButton("Ответить")
button_2 = QPushButton("Следущий вопрос")


RadioGroupBox = QGroupBox("Варианты ответов:")
AnswerGroupBox = QGroupBox("Результат теста")
AnswerGroupBox.hide()

RadioGroup = QButtonGroup()
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чулымцы")
rbtn_4  = QRadioButton("Алеуты")
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_end1 = QHBoxLayout()
layout_end2 = QVBoxLayout()
layout_end3 = QVBoxLayout()

layout_end2.addWidget(true_answer)
layout_end3.addWidget(answer_before)

layout_end1.addLayout(layout_end2)
layout_end1.addLayout(layout_end3)


layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
AnswerGroupBox.setLayout(layout_end1)
#Заготовка:
AnswerGroupBox.hide()
RadioGroupBox.hide()
button.hide()
button_2.hide()
question.hide()

v_line = QVBoxLayout()


v_line.addWidget(question,alignment = Qt.AlignHCenter)
v_line.addWidget(RadioGroupBox)
v_line.addWidget(AnswerGroupBox)
v_line.addWidget( button,alignment = Qt.AlignCenter)
v_line.addWidget( button_2,alignment = Qt.AlignCenter)
win.setLayout(v_line)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def show_result():
    question.setText(question_text_2)
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    button.hide()
    button_2.show()
    check = False
    return check

def show_question():
    question.setText(question_text_1)
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    button.show()
    button_2.hide()
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    check = True
    return check
     
def start_test(check):
    if check == True:
        check = show_question()
    elif check == False:
        check = show_result()
def ask(question,right_answer, wrong1, wrong2,wrong3):
    shuffle(answers)
    answer[0].setText(right_answer)
    answer[1].setText(wrong1)
    answer[2].setText(wrong2)
    answer[3].setText(wrong3)
    Ln_Question.setText(question)
    Lb_Correct.setText(right_answer)
    show_question()

check = True
start_test(check)
win.show()
app.exec_()




