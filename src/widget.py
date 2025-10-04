from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(payment_info: str) -> str:
	"""Функция маскирует номер карты или счета"""
	payment_info = str(payment_info)

	if not payment_info:
		raise ValueError("Пустые входные данные")

	if payment_info.startswith(" "):
		raise ValueError("Неверный формат ввода! Не может начинаться с пробела")

	split_payment_info = payment_info.split()

	# Проверка входящей информации на корректный ввод

	if len(split_payment_info) < 2:
		raise ValueError("Недостаточно данных")

	if len(split_payment_info) >3:
		raise ValueError("Некорректный ввод, слишком много данных")


	first_word_lower = split_payment_info[0].lower()

	# Обрабатываем карты

	if first_word_lower.startswith(("visa", 'mastercard', "maestro", "mir")):
		if len(split_payment_info) > 2:
			# Многословное название (например, "Visa Platinum")
			card_name = " ".join(split_payment_info[:-1])  # все кроме номера
		else:
			# Однословное название (например, "Maestro")
			card_name = split_payment_info[0]

		return f'{card_name} {get_mask_card_number(split_payment_info[-1])}'

	# Обрабатываем счета
	elif first_word_lower.startswith("счет"):
		return f'Счет {get_mask_account(split_payment_info[-1])}'

	else:
		raise ValueError("Неизвестный тип")




def get_date(date_string: str) -> str:
	"""Преобразует дату в новый формат"""

	try:
		date_obj = datetime.fromisoformat(date_string)
		return f"{date_obj.day:02}.{date_obj.month:02}.{date_obj.year}"
	except:
		raise ValueError("Неверный ISO формат")



print(get_date("2012-03-05T18:35:29.512364"))
print(get_date("2019-03-08T18:35:29.512364"))
print(get_date("2013-02-04T11:35:29.512364"))
