class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius  # Защищенный атрибут

    @property
    def celsius(self):
        """Геттер для celsius"""
        return f'Температура: {self._celsius}'

    @celsius.setter
    def celsius(self, value):
        """Сеттер для celsius с валидацией"""
        if value < -273.15:
            raise ValueError('Temperature below absolute zero!')
        self._celsius = value

    @property
    def fahrenheit(self):
        """Вычисляемое свойство"""
        return f'{(self._celsius * 9 / 5) + 32} F'

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Сеттер для fahrenheit"""
        self._celsius = (value - 32) * 5 / 9


# Использование
temp = Temperature(25)
print(temp.celsius)  # ✅ 25
print(temp.fahrenheit)  # ✅ 77.0

temp.celsius = 30  # ✅ Работает через сеттер
print(temp.celsius)
temp.celsius = -300  # ❌ ValueError
print(temp.celsius)
