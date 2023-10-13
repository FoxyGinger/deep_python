class Animal:
    name: str

    def __init__(self, name: str):
        self.name = name


class Bird(Animal):
    wingspan: int

    def __init__(self, name: str, wingspan: int):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    max_depth: int

    def __init__(self, name: str, max_depth: int):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 50:
            return "Мелководная рыба"
        elif 50 <= self.max_depth < 100:
            return "Средневодная рыба"
        else:
            return "Глубоководная рыба"


class Mammal(Animal):
    weight: int

    def __init__(self, name: str, weight: int):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 50:
            return "Малявка"
        elif 50 <= self.weight < 100:
            return "Обычный"
        else:
            return "Гигант"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == "Bird":
            return Bird(*args)
        elif animal_type == "Fish":
            return Fish(*args)
        elif animal_type == "Mammal":
            return Mammal(*args)
        else:
            raise ValueError('Недопустимый тип животного')


# Создание экземпляров животных
animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

# Вывод результатов
print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())
