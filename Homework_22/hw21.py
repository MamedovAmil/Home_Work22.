
"""
Мамедов Амиль
Я изучил работу https://github.com/bchkrvn/HW_21.git
1)

строки где замечено: 
https://github.com/bchkrvn/HW_21/blob/master/main.py#L63
https://github.com/bchkrvn/HW_21/blob/master/main.py#L68
https://github.com/bchkrvn/HW_21/blob/master/main.py#L68


строго записаны "склад" и "магазин" и вывод данных именно для этих двух структур, если будут ещё дополнительные склады, магазины, другие логистические объекты то придётся всё переписывать.

как бы я решил/переписал:
"""
print(f'Нужное количество есть в {request.from_storage}')
print(f'Курьер забрал {request.amount} {request.product} из {request.from_storage}')
print(f'Курьер везёт {request.amount} {request.product} из {request.from_storage} в {request.to_storage}')
print(f'Курьер доставил {request.amount} {request.product} в {request.to_storage}\n')
print(storage)
print(shop)

# последние два принта у меня возвращают __repr__ с содержимым магазина/склада такого вида:
def __repr__(self):
    if len(self.get_items) == 0:
        return f'На складе пусто! Вместимость: {self._capacity}.'
    return 'На складе хранятся:\n' + '\n'.join(f'> {amount} {item}' for item, amount in self.get_items.items())

"""
2)

строки где замечено: 
https://github.com/bchkrvn/HW_21/blob/master/exceptions.py


не понимаю, зачем прописывать __init__ и __str__ для пользовательских исключений, как-то всё сложно

как бы я решил/переписал:
"""
class NotEnoughSpace(BaseException):
    message = 'Невозможно доставить товар, недостаточно места!\n'


class NotEnoughGoods(BaseException):
    message = 'Не достаточно товара! Попробуйте заказать меньше!\n'


class NoGoodsInStorage(BaseException):
    message = 'Данного товара нет на складе!\n'


class MaxUniqueItemsInStorage(BaseException):
    message = 'Невозможно доставить товар!\n'


class BadRequest(BaseException):
    message = 'Неверный формат запроса. Попробуйте заново!\n'


"""
3)

строки где замечено: 
https://github.com/bchkrvn/HW_21/blob/master/base_class.py#L6


BaseClass наследуется от абстрактного и инициализацию можно вынести в абстрактный, 
где уже будет capacity и словарь для наших товаров, а в BaseClass в __init__ отнаследовать
от родителя

как бы я решил/переписал:
"""
def __init__(self):
    super().__init__()


"""
4)

строки где замечено: 
https://github.com/bchkrvn/HW_21/blob/master/base_class.py#L39


is_item - лишний ненужный метод, т.к. мы получаем словарь с товарами через get_items и 
можем проверить вхождение товара в словарь get_items

как бы я решил/переписал:
"""
def add(self, title: str, qty: int) -> None:
    if not self.get_free_space() >= qty:
        raise NotEnoughSpace()

    if title not in self.get_items:
        self._items[title] = 0
    self._items[title] += qty


"""
5)

строки где замечено:
https://github.com/bchkrvn/HW_21/blob/master/base_class.py#L25


лишнее создание переменной amount_in_store и потом использование её для 
проверки когда можно сразу сделать проверку if (и опять же я бы использовал метод get_items)

как бы я решил/переписал:
"""
def remove(self, title: str, qty: int) -> None:
    if title not in self.get_items:
        raise NoGoodsInStorage()

    if qty > self.get_items[title]:
        raise NotEnoughGoods()

    self.get_items[title] -= qty
    if self.get_items[title] == 0:
        del self._items[title]


"""
6)

строки где замечено:
https://github.com/bchkrvn/HW_21/blob/master/base_class.py#L36


можно упросить без создания переменной occupied_space

как бы я решил/переписал:
"""
def get_free_space(self) -> int:
    return self._capacity - sum(self.get_items.values())

