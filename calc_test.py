import unittest
from calculator import Calculator
from ddt import ddt, data


class CalculatorSetup(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()


@ddt
class CalcTextboxTest(CalculatorSetup):

    def test_should_initialize_as_expected(self):
        self.assertEqual(self.calc.expression, "")
        self.assertEqual(self.calc.result, 0)

    @data("+", "*", "/")
    def test_expression_should_not_lead_with_non_negative_operator(self, value):
        self.calc.evaluate(value, 2)
        self.assertEqual(self.calc.expression, "2")

    def test_negative_number_should_lead_with_negative_operator(self):
        self.calc.evaluate("-", 2)
        self.assertEqual(self.calc.expression, "-2")
        self.calc.clear()


class CalcEvaluationTest(CalculatorSetup):

    def test_should_evaluate_one_plus_one_to_two(self):
        self.calc.evaluate("+", 1)
        self.calc.evaluate("+", 1)
        self.assertEqual(self.calc.result, 2)

    def test_should_evaluate_two_plus_two_to_four(self):
        self.calc.evaluate("+", 2)
        self.calc.evaluate("+", 2)
        self.assertEqual(self.calc.result, 4)

    def test_should_evaluate_expression_after_each_input(self):
        self.calc.evaluate("+", 12)
        self.assertEqual(self.calc.result, 12)
        self.calc.evaluate("+", 10)
        self.assertEqual(self.calc.result, 22)

    def test_should_support_standard_operators(self):
        self.calc.evaluate("+", 5)
        self.calc.evaluate("-", 2)
        self.calc.evaluate("*", 6)
        self.calc.evaluate("/", 3)
        self.assertEqual(self.calc.result, 1)

    def test_should_evaluate_parentheses_first(self):
        self.calc.evaluate("+(", 5)
        self.calc.evaluate("-", 2)
        self.calc.evaluate(")*", 6)
        self.calc.evaluate("/", 3)
        self.assertEqual(self.calc.result, 6)

    def test_should_reset_state_on_clear(self):
        self.calc.evaluate("+", 2)
        self.calc.clear()
        self.assertEqual(self.calc.expression, "")
        self.assertEqual(self.calc.result, 0)


if __name__ == '__main__':
    unittest.main()
