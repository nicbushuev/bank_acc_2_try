import pytest


@pytest.fixture
def default_card_number() -> str:
	"""Фикстура со стандартным номером из 16 цифр"""
	return '1234123412341234'

@pytest.fixture
def default_account_number() -> str:
	"""Фикстура со стандартным номером 20 цифр"""
	return '12345123451234512345'

# @pytest.fixture
# def default_account_number() -> str:
# 	"""Фикстура со стандартным номером из 20 цифр"""
# 	return '12341234123412341234'
#
#
# @pytest.fixture
# def empty_number() -> str:
# 	"""Фикстура без символов"""
# 	return ''
#
#
# @pytest.fixture
# def wrong_card_number() -> str:
# 	"""Фикстура с неверным форматом ввода номера карты"""
# 	return '1234asdf12341234'
#
#
# @pytest.fixture
# def card_number_with_spaces():
# 	"""Фикстура номера карты с пробелами"""
# 	return '1234 1234 1234 1234'
