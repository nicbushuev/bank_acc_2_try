from src.conftest import default_card_number, default_account_number
from src.masks import get_mask_card_number, get_mask_account
import pytest

"""ТЕСТИРОВАНИЕ get_mask_card_number"""

def test_get_mask_card_number(default_card_number):
	"""Тест с валидным номером карты"""
	assert get_mask_card_number(default_card_number) == "1234 12** **** 1234"


@pytest.mark.parametrize("card_number, expected", [
	("1234567812345678", "1234 56** **** 5678"),
	("5555666677778888", "5555 66** **** 8888"),
	("1111222233334444", "1111 22** **** 4444"),
	("0000111122223333", "0000 11** **** 3333"),
])
def test_get_mask_card_number_parametrized(card_number, expected):
	"""Тест маскировки различных номеров карт с параметризацией"""
	assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_card_number, error_match", [
	("", "Отсутствует номер карты"),
	(" ", "В номере карты не должно быть пробелов"),
	("123", "Неверный формат ввода! Должно быть 16 цифр"),
	("1234abcd12341234", "Неверный формат ввода, не должно быть букв в номере карты"),

])
def test_get_mask_card_number_invalid(invalid_card_number, error_match):
	"""Тест на отработку ошибок ValueError с параметризацией"""
	with pytest.raises(ValueError, match=error_match):
		get_mask_card_number(invalid_card_number)

"""ТЕСТИРОВАНИЕ get_mask_account"""

def test_get_mask_account_number(default_account_number):
	"""Тест с валидным номером счета"""
	assert get_mask_account(default_account_number) == "**2345"

@pytest.mark.parametrize("account_number, expected", [
	("12345678901234567890", "**7890"),
	("55556666777788881111", "**1111"),
	("11112222333344445555", "**5555"),
	("00001111222233333211", "**3211"),
])

def test_account_number_parametrize(account_number,expected):
	assert get_mask_account(account_number) == expected
