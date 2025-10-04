import pytest


@pytest.fixture
def default_card_number() -> str:
	"""Фикстура со стандартным номером из 16 цифр"""
	return '1234123412341234'

@pytest.fixture
def default_account_number() -> str:
	"""Фикстура со стандартным номером 20 цифр"""
	return '12345123451234512345'
