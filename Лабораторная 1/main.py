# TODO Написать 3 класса с документацией и аннотацией типов

# описание класса Hero
class Hero:
    def __init__(self, name: str, health: int, attack: int):
        """
        Создание и подготовка к работе объекта "Герой"
        :param name: Имя героя
        :param health: Здоровье героя
        :param attack: Урон атаки, наносимой героем
        Примеры:
        >>> hero = Hero('Bennet', 200, 100)  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Имя героя должно быть типа str")
        self.name = name

        if not isinstance(health, int):
            raise TypeError("Здоровье героя должно быть типа int")
        elif health < 0:
            raise ValueError("Здоровье героя должно быть неотрицательным")
        self.health = health

        if not isinstance(attack, int):
            raise TypeError("Атака героя должна быть типа int")
        elif attack < 0:
            raise ValueError("Атака героя должна быть неотрицательна")
        self.attack = attack

    def take_damage(self, damage: int):
        """
        Функция, которая принимает удар на героя и уменьшает здоровье
        :param damage: Сила удара

        Пример:
        >>> hero = Hero('Bennet', 200, 100)
        >>> hero.take_damage(3)
        """

        if not isinstance(damage, int):
            raise TypeError("Урон, наносимый горою, должен быть типа int")
        self.health -= damage


    def health_to_attack(self, health_points: int):
        """
        Функция превращения очков здоровья героя в очки атаки в соотношении 2 к 1
        :param health_points:

        Пример:
        >>> hero = Hero('Bennet', 100, 50)
        >>> hero.health_to_attack(50)
            """
        if self.health <= health_points:
            raise ValueError("Количество преобразуемых очков здоровья должно быть больше, чем здоровье героя")

        self.health -= health_points
        self.attack += round(health_points/2)

# описание класса Enemy
class Enemy:
    def __init__(self, category: str, health: int, damage: int):
        """
        Создание и подготовка к работе объекта "Враг"
        :param category: Категория врага
        :param health: Здоровье врага
        :param damage: Урон, наносимый врагом
        Примеры:
        >>> enemy = Enemy('spider', 50, 10)  # инициализация экземпляра класса
        """

        if not isinstance(category, str):
            raise TypeError("Категория врага должен быть типа str")
        self.category = category

        if not isinstance(health, int):
            raise TypeError("Здоровье врага должно быть типа int")
        elif health < 0:
            raise ValueError("Здоровье врага должно быть неотрицательным")
        self.health = health

        if not isinstance(damage, int):
            raise TypeError("Урон врага должен быть типа int")
        elif damage < 0:
            raise ValueError("Урон врага должен быть неотрицателен")
        self.attack = damage

    def instant_kill(self):
        """
        Функция, мгновенно убивающая врага
        """
        self.health = 0

    def check_health_to_damage(self) -> bool:
        """
        Проверка, что здоровья больше, чем атаки
        :return: Здоровья больше, чем атаки
        """

        return self.health > self.damage

# описание класса Weapon
class Weapon:
    def __init__(self, element: str, bonus_attack: float):
        """
       Создание и подготовка к работе объекта "Оружие"
       :param element: Элемент оружия
       :param bonus_attack: Бонус к атаке
       Примеры:
       >>> weapon = Weapon('pyro', 1.5)  # инициализация экземпляра класса
       """

        if not isinstance(element, str):
            raise TypeError("Элемент оружия должен быть типа str")
        self.element = element

        if not isinstance(bonus_attack, float):
            raise TypeError("Бонус к атаке должен быть типа float")
        elif bonus_attack < 1.0:
            raise ValueError("Бонус к атаке должен быть больше 1")
        self.bonus_attack = bonus_attack

    def improve_bonus_attack(self):
        """
        Функция, увеличивающая бонус к атаке
        """
        ...

    def change_element(self, new_element: str):
        """
        Функция изменения элемента оружия

        Пример:
        >>> sword = Weapon('pyro', 1.5)
        >>> sword.change_element('hydro')
        """
        if not isinstance(new_element, str):
            raise TypeError("Элемент оружия должен быть типа str")
        self.element = new_element

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
