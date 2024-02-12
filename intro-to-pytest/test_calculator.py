import calculator
import pytest

def test_add():
    assert calculator.calculate(2, 3, "add") == 5
    
def test_subtract():
    assert calculator.calculate(10, 2, "subtract") == 8

def test_multiply():
    assert calculator.calculate(5, 5, "multiply") == 25

def test_divide():
    assert calculator.calculate(9, 3, "divide") == 3

# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    result = calculator.calculate(10, 2, "multiply")
    print(str(result))
    captured = capsys.readouterr()
    assert captured.out == "20\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.calculate(1, 0, "divide")

# Add more tests to cover edge cases and negative scenarios