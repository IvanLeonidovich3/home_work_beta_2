def sort_state(sort_list: list) -> list:
    """сортирует список словарей по ключу EXECUTED"""
    new_list = []  # отсорированный список
    for sorting in sort_list:
        if sorting["state"] == "EXECUTED":
            new_list.append(sorting)
    return new_list


def sort_data(data_list: list) -> list:
    """сортирует список словарей по убыванию даты"""
    sort_list = []
    for sorting in data_list:
        sort_list.append(sorting)
        get_sort = sorted(sort_list, key=lambda d: d["date"], reverse=True)
    return get_sort
