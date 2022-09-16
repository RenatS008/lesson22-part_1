# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)  # Чтение данных из строки
    _new_data = _sorting(data)  # Сортировка по возрасту по возрастанию
    result_data = _filtering(data)  # Фильтрация
    return result_data


def _read(csv):
    return [data.split(';') for data in csv.split('\n')]


def _sorting(data):
    return sorted(data, key=lambda age: int(age[1]))


def _filtering(data):
    return [age for age in data if int(age[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
