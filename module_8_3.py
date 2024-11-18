class Car:
    def __init__(self, model:str, __vin:int, __numbers:str):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.__vin = __vin
        if self.__is_valid_numbers(__numbers):
            self.__numbers = __numbers
        # print(self.model, self.__vin, self.__numbers) # проверочный принт

    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number

        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        elif not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, __numbers):
        self.__numbers = __numbers
        if not isinstance(__numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных  для номеров')
        if len(__numbers) != 6:
            raise IncorrectCarNumbers('Неверная длинна номера')
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')