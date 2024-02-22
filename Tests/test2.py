import unittest
from logic.Calculator_app import CalculatorApp


class TestAppium(unittest.TestCase):
    def test_add_operation(self):
        Current_calculator_app = CalculatorApp()
        Current_calculator_app.performe_add_operation(7,7)
        expectedResult = Current_calculator_app.calculate_and_get_result()
        actualResult = '14'
        self.assertEqual(actualResult,expectedResult,"Answer is incorrect")


def test_mul_operation(self):
    Current_calculator_app = CalculatorApp()
    Current_calculator_app.performe_mul_operation(7, 7)
    expectedResult = Current_calculator_app.calculate_and_get_result()
    actualResult = '49'
    self.assertEqual(actualResult, expectedResult, "Answer is incorrect")


def test_sub_operation(self):
    Current_calculator_app = CalculatorApp()
    Current_calculator_app.performe_sub_operation(7, 7)
    expectedResult = Current_calculator_app.calculate_and_get_result()
    actualResult = '0'
    self.assertEqual(actualResult, expectedResult, "Answer is incorrect")


def test_div_operation(self):
    Current_calculator_app = CalculatorApp()
    Current_calculator_app.performe_div_operation(7, 7)
    expectedResult = Current_calculator_app.calculate_and_get_result()
    actualResult = '1'
    self.assertEqual(actualResult, expectedResult, "Answer is incorrect")


if __name__ == '__main__':
    unittest.main()