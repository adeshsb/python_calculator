"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 5 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
    
    def test_division(self):
        assert 2 == calculator.division(10, 5)
        assert "Undefined" == calculator.division(10, 0)
