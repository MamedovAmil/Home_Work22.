# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read_csv(file: str) -> list[dict[str, int]]:
    # Чтение данных из строки
    data = file.split('\n')
    return [{'name': item.split(';')[0], 'age': int(item.split(';')[1])} for item in data]


def sort_data(data: list[dict]) -> list[dict]:
    return sorted(data, key=lambda x: x['age'])


def filter_by_age(data: list[dict]):
    return [{'name': item['name'], 'age': item['age']} for item in data if item['age'] > 10]


def get_users_list():
    data = read_csv(csv)
    sorted_data = sort_data(data)
    result = filter_by_age(sorted_data)

    return result


if __name__ == '__main__':
    print(get_users_list())
