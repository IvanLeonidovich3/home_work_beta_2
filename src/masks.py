def mask_card(card_number: int) -> str:
    """получает, делит на части и возвращает маскированный номер карты"""
    str_number = str(card_number).split()[-1]
    stars_number = str_number[:6] + (len(str_number[6:-4]) * "*") + str_number[-4:]
    mask_number = stars_number[0:4] + " " + stars_number[4:8] + " " + stars_number[8:12] + " " + stars_number[-4:]
    return mask_number


def account_mask(account_number: int) -> str:
    """получает и маскируетмаску счета"""
    get_account = account_number
    str_account = str(get_account)
    mask_account = "*" * len(str_account[:-4]) + str_account[-4:]
    return mask_account


print(mask_card(7000792289606361))
print()
print(account_mask(73654108430135874305))
