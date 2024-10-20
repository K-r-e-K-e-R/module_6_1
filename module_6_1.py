class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        if self.alive:
            if food.edible:
                self.fed = True
                print(f"{self.name} съел {food.name} и остался живым.")
            else:
                self.alive = False
                print(f"{self.name} не стал есть {food.name}.")
        else:
            print(f"{self.name} уже мертв.")


class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible


# Класс-наследник для млекопитающих
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)  # Вызов конструктора родительского класса


# Класс-наследник для хищников
class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)  # Вызов конструктора родительского класса


# Класс-наследник для растений - цветы
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)  # Вызов конструктора родительского класса


# Класс-наследник для растений - фрукты
class Fruit(Plant):
    def __init__(self, name, edible=True):
        super().__init__(name, edible)  # Вызов конструктора родительского класса
        self.edible = edible  # Установка атрибута edible


# Создание животных
a1 = Predator('Тигр Шер-Хан')
a2 = Mammal('Ослик Иа')
# Создание растений
p1 = Flower('Аленький цветочек')
p2 = Fruit('Красное Яблоко')

# Тестирование взаимодействия
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
