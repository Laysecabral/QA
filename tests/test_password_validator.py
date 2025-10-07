import pytest
from src.password_validator import validate_password

def test_valid_password():
    assert validate_password("Valid1@Password")

def test_invalid_password_length():
    assert not validate_password("Short1@")

def test_missing_uppercase():
    assert not validate_password("lowercase1@")

def test_missing_number():
    assert not validate_password("NoNumber@")

def test_missing_special():
    assert not validate_password("NoSpecial1")
