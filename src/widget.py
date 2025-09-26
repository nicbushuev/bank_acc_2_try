from src.masks import get_mask_card_number, get_mask_account



def mask_account_card(payment_info: str) -> str:
	"""Функция маскирует номер карты или счета"""
	payment_info = str(payment_info)
	split_payment_info = payment_info.split()

	# print(split_payment_info)  # для отладки

	if len(split_payment_info) < 2:
		raise ValueError("Недостаточно данных")

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
		raise ValueError(f"Неизвестный тип: {payment_info}")

print(mask_account_card("Visa Platinum 1234123412341234"))
print(mask_account_card("Счет 123123123123"))
print(mask_account_card("Visa 1234123412341234"))

