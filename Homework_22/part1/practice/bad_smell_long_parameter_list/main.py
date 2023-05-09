# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, field, x: int, y: int, state: str = 'fly'):
        self.speed = 1
        self.state = state
        self.x = x
        self.y = y
        self.field = field

    def _get_speed(self):

        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Что ты за зверь?)')

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(self.x, self.y + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(self.x, self.y - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(self.x - speed, self.y, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(self.x + speed, self.y, unit=self)
