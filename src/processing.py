def sort_state(sort_list: list) -> list:
    """сортирует список словарей по ключу EXECUTED"""
    new_list = []  # отсорированный список
    for sorting in sort_list:
        if sorting['state'] == 'EXECUTED':
            new_list.append(sorting)
    return new_list


