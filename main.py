import re
from zubachev import counter_fingers_qwer, counter_fingers, data_dict


def value_passing_fingers(column, value):
    """
    На вход получает колону и нагрузку
    Заполняет в словарь палец+=значение
    """
    match column:
        case 0 | 1:
            counter_fingers['f5l'] += value
        case 2:
            counter_fingers['f4l'] += value
        case 3:
            counter_fingers['f3l'] += value
        case 4 | 5:
            counter_fingers['f2l'] += value
        case 6 | 7:
            counter_fingers['f2r'] += value
        case 8:
            counter_fingers['f3r'] += value
        case 9:
            counter_fingers['f4r'] += value
        case 10 | 11 | 12:
            counter_fingers['f5r'] += value


def value_passing_fingers_qwer(column, value):
    """
    На вход получает колону и нагрузку
    Заполняет в словарь палец+=значение
    """
    match column:
        case 0 | 1:
            counter_fingers_qwer['f5l'] += value
        case 2:
            counter_fingers_qwer['f4l'] += value
        case 3:
            counter_fingers_qwer['f3l'] += value
        case 4 | 5:
            counter_fingers_qwer['f2l'] += value
        case 6 | 7:
            counter_fingers_qwer['f2r'] += value
        case 8:
            counter_fingers_qwer['f3r'] += value
        case 9:
            counter_fingers_qwer['f4r'] += value
        case 10 | 11 | 12:
            counter_fingers_qwer['f5r'] += value


def getting_coordinates(symbol) -> list:
    """
     На вход получаем символ,
     на выход список из ряда и колоны
    """
    for key in data_dict:
        for value in data_dict[key]['key']:
            if value == symbol:
                return [data_dict[key]['raw'], data_dict[key]['column']]


def getting_coordinates_qwer(symbol) -> list:
    """
     На вход получаем символ,
     на выход список из ряда и колоны
    """
    for key in data_dict:
        for value in data_dict[key]['qwer']:
            if value == symbol:
                return [data_dict[key]['raw'], data_dict[key]['column']]


def load_step_counter(first_sim, second_sim):
    """
    функция подсчета шагов
    на вход символ и след символ
    """
    if getting_coordinates(first_sim)[1] == getting_coordinates(second_sim)[1]:
        value_passing_fingers(getting_coordinates(second_sim)[1],
                              abs(getting_coordinates(first_sim)[0] - getting_coordinates(second_sim)[0]))
    else:
        if getting_coordinates(first_sim)[0] != getting_coordinates(second_sim)[0]:
            match getting_coordinates(second_sim)[1]:
                case 5 | 6:
                    if getting_coordinates(second_sim)[0] == 2:
                        value_passing_fingers(getting_coordinates(second_sim)[1], 1)
                    else:
                        value_passing_fingers(getting_coordinates(second_sim)[1],
                                              abs(getting_coordinates(first_sim)[0] - getting_coordinates(second_sim)[
                                                  0]) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    if getting_coordinates(second_sim)[0] == 2:
                        pass
                    else:
                        value_passing_fingers(getting_coordinates(second_sim)[1],
                                              abs(getting_coordinates(first_sim)[0] - getting_coordinates(second_sim)[
                                                  0]))
                case 11:
                    value_passing_fingers(getting_coordinates(second_sim)[1],
                                          abs(getting_coordinates(first_sim)[0] - getting_coordinates(second_sim)[
                                              0]) + 1)
                case 12:
                    value_passing_fingers(getting_coordinates(second_sim)[1],
                                          abs(getting_coordinates(first_sim)[0] - getting_coordinates(second_sim)[
                                              0]) + 2)
        if getting_coordinates(first_sim)[0] == getting_coordinates(second_sim)[0]:
            match getting_coordinates(second_sim)[1]:
                case 5 | 6 | 11:
                    value_passing_fingers(getting_coordinates(second_sim)[1],
                                          abs(getting_coordinates(second_sim)[0] - 2) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    value_passing_fingers(getting_coordinates(second_sim)[1],
                                          abs(getting_coordinates(second_sim)[0] - 2))
                case 12:
                    value_passing_fingers(getting_coordinates(second_sim)[1],
                                          abs(getting_coordinates(second_sim)[0] - 2) + 2)


def load_space_counter(text1):
    """
    Функция считает кол-во пробелов в тексте
    """
    text1 = re.sub(r'[^" "]', '', text1)
    counter_fingers_qwer['f1l'] += int(len(text1) * 0.6)
    counter_fingers_qwer['f1r'] += int(len(text1) * 0.4)
    counter_fingers['f1l'] += int(len(text1) * 0.55)
    counter_fingers['f1r'] += int(len(text1) * 0.45)


def load_step_counter_qwer(first_sim, second_sim):
    """
    На вход получает колону и нагрузку
    Заполняет в словарь палец += значение
    """
    if getting_coordinates_qwer(first_sim)[1] == getting_coordinates_qwer(second_sim)[1]:
        value_passing_fingers_qwer(getting_coordinates_qwer(second_sim)[1],
                                   abs(getting_coordinates_qwer(first_sim)[0] - getting_coordinates_qwer(second_sim)[
                                       0]))
    else:
        if getting_coordinates_qwer(first_sim)[0] != getting_coordinates_qwer(second_sim)[0]:
            match getting_coordinates_qwer(second_sim)[1]:
                case 5 | 6:
                    if getting_coordinates_qwer(second_sim)[0] == 2:
                        value_passing_fingers_qwer(getting_coordinates_qwer(second_sim)[1], 1)
                    else:
                        value_passing_fingers_qwer(getting_coordinates_qwer(second_sim)[1],
                                                   abs(getting_coordinates_qwer(first_sim)[0] -
                                                       getting_coordinates_qwer(second_sim)[
                                                           0]) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    if getting_coordinates_qwer(second_sim)[0] == 2:
                        pass
                    else:
                        value_passing_fingers_qwer(getting_coordinates_qwer(second_sim)[1],
                                                   abs(getting_coordinates_qwer(first_sim)[0] -
                                                       getting_coordinates_qwer(second_sim)[0]))
                case 11:
                    value_passing_fingers_qwer(getting_coordinates_qwer(second_sim)[1],
                                               abs(getting_coordinates_qwer(first_sim)[0] -
                                                   getting_coordinates_qwer(second_sim)[0]) + 1)
                case 12:
                    value_passing_fingers_qwer(getting_coordinates_qwer(second_sim)[1],
                                               abs(getting_coordinates_qwer(first_sim)[0] -
                                                   getting_coordinates_qwer(second_sim)[0]) + 2)
        if getting_coordinates_qwer(first_sim)[0] == getting_coordinates_qwer(second_sim)[0]:
            match getting_coordinates_qwer(second_sim)[1]:
                case 5 | 6 | 11:
                    value_passing_fingers_qwer(getting_coordinates_qwer(second_sim)[1],
                                               abs(getting_coordinates_qwer(second_sim)[0] - 2) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    value_passing_fingers_qwer(getting_coordinates_qwer(second_sim)[1],
                                               abs(getting_coordinates_qwer(second_sim)[0] - 2))
                case 12:
                    value_passing_fingers_qwer(getting_coordinates_qwer(second_sim)[1],
                                               abs(getting_coordinates_qwer(second_sim)[0] - 2) + 2)


def print_fingers():
    """
    Функция Вывода текста и результатов
    """
    print(f'\t\tЗУБАЧЕВ\t\t\t\t\t\t\tЙЦУКЕН')
    print(
        f'f1l - {counter_fingers["f1l"]}\tf1r - {counter_fingers["f1r"]}\t\t\tf1l - {counter_fingers_qwer["f1l"]}\tf1r '
        f'- {counter_fingers_qwer["f1r"]}')
    print(
        f'f2l - {counter_fingers["f2l"]}\tf2r - {counter_fingers["f2r"]}\t\t\tf2l - {counter_fingers_qwer["f2l"]}\tf2r '
        f'- {counter_fingers_qwer["f2r"]}')
    print(
        f'f3l - {counter_fingers["f3l"]}\tf3r - {counter_fingers["f3r"]}\t\t\tf3l - {counter_fingers_qwer["f3l"]}\tf3r '
        f'- {counter_fingers_qwer["f3r"]}')
    print(
        f'f4l - {counter_fingers["f4l"]}\tf4r - {counter_fingers["f4r"]}\t\t\tf4l - {counter_fingers_qwer["f4l"]}\tf4r '
        f'- {counter_fingers_qwer["f4r"]}')
    print(
        f'f5l - {counter_fingers["f5l"]}\tf5r - {counter_fingers["f5r"]}\t\t\tf5l - {counter_fingers_qwer["f5l"]}\tf5r '
        f'- {counter_fingers_qwer["f5r"]}')


if __name__ == "__main__":
    text_name = r'kipling.txt'
    with open(text_name, 'r', encoding='utf-8') as f:
        text = f.read()
    load_space_counter(text)
    text = re.sub(r'[^А-Яа-яёЁ1-9,0]', '', text)
    text = list(text)
    list_upper_case = [i for i in text if i.isupper()]
    value_passing_fingers(0, (len(list_upper_case) * 2))
    value_passing_fingers_qwer(0, (len(list_upper_case) * 2))
    text = ''.join(text)
    text = [i.lower() for i in text]
    for i in range(1, len(text)):
        load_step_counter(text[i - 1], text[i])
        load_step_counter_qwer(text[i - 1], text[i])
    print_fingers()
