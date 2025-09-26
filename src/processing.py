from typing import List, Dict, Any, Optional

def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция, которая принимает список словарей и опционально значение для ключа state(по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.

    Args:
        data: Список словарей с данными
        state: Значение состояния для фильтрации (по умолчанию "EXECUTED")

    Returns:
        Отфильтрованный список словарей"""

    sorted_data = []

    for example in data:
        if example.get('state') == state:
            sorted_data.append(example)
    return sorted_data

data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

