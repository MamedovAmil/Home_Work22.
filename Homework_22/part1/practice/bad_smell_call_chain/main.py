# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов
from typing import Type


class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, room, city_population):
        self.room = room
        self.city_population = city_population

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.city_population


a = Person(Room().get_name(), City().population())
print(a.get_person_room(), a.get_city_population())
