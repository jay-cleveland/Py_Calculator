"""calculator class"""


class Calculator:

    def __init__(self):
        self.expression = ""
        self.result = 0

    def evaluate(self, operand, number):

        if self.expression == "" and operand != "-":
            if '(' in operand:
                self.expression = '(' + str(number)
            else:
                self.expression = str(number)
        else:
            self.expression = str(self.expression) + operand + str(number)

        if '(' in self.expression and ')' not in self.expression:
            return
        self.result = eval(self.expression)

    def clear(self):
        self.expression = ""
        self.result = 0
