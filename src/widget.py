from datetime import datetime


def mask_count_card(card_name: str, count_card: int) -> str:
    """принимает на вход строку информацией тип карты/счета и номер карты/счета
    card_name - имя крты и её номер
    count_card - счет
    возвращает строку с замаскированным номером карты/счета"""

    words = []  # список букв
    numbers = []  # список цыфр

    for i in card_name:  # разделяю строку на цифры и буквы
        if i.isalpha():
            words.append(i)
        if i.isdigit():
            numbers.append(i)
    numbers = str(''.join(numbers))
    stars_number = numbers[:6] + (len(str(numbers[6:-4])) * "*") + numbers[-4:]  # маскирую намер карты
    mask_number = stars_number[0:4] + " " + stars_number[4:8] + " " + stars_number[8:12] + " " + stars_number[-4:]
    words = str(''.join(words))
    if not words.istitle():  # ставлю пробел между заглавными буквами в типе карты
        words = words[:4] + ' ' + words[:]
    print_words = words + ' ' + mask_number  # тип карты и замаскированный номер в одной строке

    str_account = str(count_card)
    mask_account = "*" * len(str_account[:2]) + str_account[-4:]  # маскирую счет
    return f'{print_words} \nCчет {mask_account}'


def date_time(date_string: str) -> str:
    """получает дату из стоки"""
    str_dat = date_string[:10]
    print_dat = datetime.strptime(str_dat, '%Y-%m-%d')
    return print_dat



