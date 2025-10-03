import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("payment_info, expected", [
	("Visa 1234123412341234", "Visa 1234 12** **** 1234"),
	("MasterCard 5555666677778888", "MasterCard 5555 66** **** 8888"),
	("Счет 12345678901234567890", "Счет **7890"),
	("Maestro 1111222233334444", "Maestro 1111 22** **** 4444"),
	("Visa Platinum 1111222233334444", "Visa Platinum 1111 22** **** 4444")
])
def test_mask_account_parametrize(payment_info, expected):
	"""Тест валидных банковских реквизитов(карта/счет)"""
	assert mask_account_card(payment_info) == expected


@pytest.mark.parametrize("invalid_payment_info, error_match", [
	("", "Пустые входные данные"),
	(" ", "Неверный формат ввода! Не может начинаться с пробела"),
	("Visa123", "Недостаточно данных"),
	("Visa Счет Много информации 123", "Некорректный ввод, слишком много данных"),
	("Vasa 1234123412341234", "Неизвестный тип"),
	("Утка 12341234123412340000", "Неизвестный тип"),
])
def test_account_card_invalid(invalid_payment_info, error_match):
	with pytest.raises(ValueError, match=error_match):
		mask_account_card(invalid_payment_info)


@pytest.mark.parametrize("date_input, expected", [
	("2012-03-05T18:35:29.512364", "05.03.2012"),
	("2201-02-01T18:35:29.512364", "01.02.2201"),
	("2000-01-05T18:35:29.512364", "05.01.2000"),
	("0001-01-05T18:35:29.512364", "05.01.1"),
])
def test_get_date_parametrize(date_input, expected):
	"""Тест с валидными датами"""
	assert get_date(date_input) == expected
