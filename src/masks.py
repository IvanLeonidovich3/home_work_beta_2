from typing import Any

card = {
    "card_number": 7000792289606361,  # 7000 7922 8960 6361 -> 700079******631 -> 7000 79** **** 6361
    "account_number": 73654108430135874305,
}


def mask_card() -> Any:
    """получает, делит на части и возвращает маскированный номер карты"""
    for key in card:
        get_number = card[key]
        str_number = str(get_number).split()[-1]
        stars_number = str_number[:6] + (len(str_number[6:-4]) * "*") + str_number[-4:]
        mask_number = stars_number[0:4] + " " + stars_number[4:8] + " " + stars_number[8:12] + " " + stars_number[-4:]
        return mask_number


def account_mask() -> str:
    """получает и маскируетмаску счета"""
    get_account = card["account_number"]
    str_account = str(get_account)
    mask_account = "*" * len(str_account[:-4]) + str_account[-4:]
    return mask_account


print(mask_card())
print(account_mask())
