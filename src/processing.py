from typing import Any

def filter_by_state(list_of_dictionaries: Any) -> Any:
    ''' Вывод функции со статусом по умолчанию 'EXECUTED' '''
    answer = []
    for list in list_of_dictionaries:
        if list['state'] == 'EXECUTED':
            answer.append(list)
    return answer


print(filter_by_state(
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
)


def sort_by_date(enter_date: Any) -> Any:
    ''' Вывод функции (сортировка по убыванию, т. е. сначала самые последние операции) '''
    list = sorted(enter_date, key=lambda list_new: list_new['date'], reverse = reversed)
    return list


print(sort_by_date(
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
)