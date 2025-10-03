from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
	"""Функция, которая маскирует введенный номер карты согласно заданной маске"""

	# Проверка на наличие пустой строки:
	if card_number == "":
		raise ValueError("Отсутствует номер карты")

	# Проверка на наличие пробела:
	if card_number.isspace():
		raise ValueError("В номере карты не должно быть пробелов")
	# Проверка на наличие 16 цифр в номере карты:
	if len(str(card_number)) != 16:
		raise ValueError("Неверный формат ввода! Должно быть 16 цифр")

	# Проверка на наличие только цифр:
	if not card_number.isdigit():
		raise ValueError("Неверный формат ввода, не должно быть букв в номере карты")

	card_number = str(card_number)
	return "{} {}** **** {}".format(card_number[:4], card_number[4:6], card_number[12:])


def get_mask_account(account_number: Union[str, int]) -> str:
	"""Функция, которая маскирует введенный номер карты согласно заданной маске"""

	# Проверка на наличие пустой строки:
	if account_number == "":
		raise ValueError("Отсутствует номер счета")

	# Проверка на наличие пробела:
	if account_number.isspace():
		raise ValueError("В номере счета не должно быть пробелов")
	# Проверка на наличие 20 цифр в номере счета:
	if len(str(account_number)) != 20:
		raise ValueError("Неверный формат ввода! Должно быть 20 цифр")

	# Проверка на наличие только цифр:
	if not account_number.isdigit():
		raise ValueError("Неверный формат ввода, не должно быть букв в номере счета")


	account_number = str(account_number)
	return "**" + account_number[-4:]
