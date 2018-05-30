from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([]) #vytvorim praydnou aplikaci
window = QtWidgets.QWidget() # vytvatim okno

with open('kalkulacka1.ui', encoding='utf-8') as file: # oteviram kalkulacka1.ui jako file
    uic.loadUi(file, window) # nacti UI z toho souboru file, do toho okna window

operand1 = window.findChild(QtWidgets.QDoubleSpinBox, 'operand1')
print(operand1)
operand2 = window.findChild(QtWidgets.QDoubleSpinBox, 'operand2')
print(operand2)
operator = window.findChild(QtWidgets.QComboBox, 'operator_box')
print(operator)
result = window.findChild(QtWidgets.QLabel, 'result')
print(result)
cancel = window.findChild(QtWidgets.QPushButton, 'cancel')
print(cancel)

def calculate(): # když se změní hodnota, zavolej mi nějakou funkci
    number1 = operand1.value()
    number2 = operand2.value()
    operator_text = operator.currentText()

    try:
        if operator_text == "+":
            result_number = number1 + number2
        if operator_text == "-":
            result_number = number1 - number2
        if operator_text == "*":
            result_number = number1 * number2
        if operator_text == "/":
            result_number = number1 / number2

    except Exception:
        result_number = 'CHYBA'

    print(number1, operator_text, number2, result_number)

    #result.setValue(str(result_number))
    result.setText(str(result_number))

def delete():
    number1 = '0'
    number2 = '0'
    operator_text = operator.currentText()
    result_number = '0'
    if cancel.clicked:
        print('jde to')
        print(number1, operator_text, number2, result_number)
    operand1.setValue(int(number1))
    operand2.setValue(int(number2))
    result.setText(str(result_number))

operand1.valueChanged.connect(calculate) # připojim na tu hodnotu
operand2.valueChanged.connect(calculate) # připojim na tu hodnotu
operator.currentTextChanged.connect(calculate) # připojim na tu hodnotu
cancel.clicked.connect(delete)

calculate() # aby to bylo v tom počátečním stavu 0, aby se to tedy vypočítalo

window.show()
app.exec()


# Nastavení hodnoty ComboBoxu:
# operator.setCurretnText("+")
# Nastavení hodnoty DoubleSpinBoxu:
# operator.setValue(0)
