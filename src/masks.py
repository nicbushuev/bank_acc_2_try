def get_mask_card_number(card_number: int) -> str:
    """Функция, которая маскирует введенный номер карты согласно заданной маске"""

    card_number = str(card_number)
    return "{} {}** **** {}".format(card_number[:4], card_number[4:6], card_number[12:])


def get_mask_account(account_number: int) -> str:
    """Функция, которая маскирует введенный номер карты согласно заданной маске"""

    account_number = str(account_number)
    return "**" + account_number[-4:]
