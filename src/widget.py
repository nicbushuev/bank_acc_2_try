from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(payment_info:str)->str:
	"""Функция, принимающая на вход информацию о платежном инструменте и применяющая соответствующую маску"""
	payment_info = str(payment_info)

	split_payment_info = payment_info.lower().split(" ")


	if split_payment_info[0].startswith(("visa",'mastercard',"maestro","mir")):
		masked_number = f'{split_payment_info[0]} + ' get_mask_card_number(split_payment_info[])
	elif payment_info.lower().startswith(("cчет")):
		masked_number = get_mask_account(payment_info)
	else:
		raise ValueError("Неверный формат ввода")

	print(masked_number)

mask_account_card("Maestro 1596837868705199")




