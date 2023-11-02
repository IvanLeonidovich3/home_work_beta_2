from datetime import datetime
from typing import Any

from masks import account_mask, mask_card


def mask_count_card(card_name: str) -> Any:
    """принимает на вход строку информацией тип карты/счета и номер карты/счета
    card_name - имя карты, её номер и счет
    возвращает строку с замаскированным номером карты/счета"""
    input_argument = card_name.split(" ")[-1]
    if len(input_argument) > 16:
        return card_name.split(" ")[0] + " " + account_mask("".join(input_argument))
    else:
        return " ".join(card_name.split(" ")[0:-1]) + " " + mask_card(input_argument)


def date_time(date_string: str) -> Any:
    """получает дату из стоки"""
    str_dat = date_string[:10]
    print_dat = datetime.strptime(str_dat, "%Y-%m-%d")
    return print_dat


mask_count_card("")
