from credit_check import credit_check
import pytest

def test_validity_one():
    assert credit_check('5541808923795240') == "The number is valid!"

def test_validity_two():
    assert credit_check("4024007136512380") == "The number is valid!"
    
def test_validity_three():
    assert credit_check("6011797668867828") == "The number is valid!"

def test_invalidity_one():
    assert credit_check("5541801923795240") == "The number is invalid!"

def test_invalidity_two():
    assert credit_check("4024007106512380") == "The number is invalid!"
    
def test_invalidity_three():
    assert credit_check("6011797668868728") == "The number is invalid!"