import doctest


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        '''
        >>> p = Person("Ivanov", "Ivan", "Ivanovich", 30)
        >>> p.full_name()
        'Ivanov Ivan Ivanovich'
        '''
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        '''
        >>> p = Person("Ivanov", "Ivan", "Ivanovich", 30)
        >>> p.birthday()
        >>> p.get_age()
        31
        '''
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        '''
        >>> e = Employee("ivanov", "ivan", "ivanovich", 30, "manager", 50000)
        >>> e.last_name
        'Ivanov'
        '''
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        '''
        >>> e = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        >>> e.__str__()
        'Ivanov Ivan Ivanovich (Manager)'
        '''
        return f'{self.full_name()} ({self.position})'


def test_employee_raise_salary():
    '''
    >>> emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
    >>> emp.raise_salary(10)
    >>> emp.salary
    55000.0
    '''


if __name__ == "__main__":
    import doctest
    doctest.testmod()