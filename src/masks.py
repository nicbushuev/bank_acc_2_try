from typing import Union



def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция, которая маскирует введенный номер карты согласно заданной маске"""

    if len(card_number) != 16:
        raise "Неверный формат ввода! Должно быть 16 цифр"


    card_number = str(card_number)
    return "{} {}** **** {}".format(card_number[:4], card_number[4:6], card_number[12:])


def get_mask_account(account_number: Union[str,int]) -> str:
    """Функция, которая маскирует введенный номер карты согласно заданной маске"""

    account_number = str(account_number)
    return "**" + account_number[-4:]
