class Enemy:
    """
    Базовый класс Enemy, обозначющее Врага в игре
    Создание и подготовка к работе объекта Враг
        :param name: Название врага
        :param health: Количество очков здоровья
        :param attack: Количество очков атаки, которую наносит враг, сила атаки
    Пример:
    >>> slime = Enemy('slime', 200, 50)
    """

    def __init__(self, name: str, health: int, attack: int):
        """
        :param name: Название врага
        :param health: Количество очков здоровья
        :param attack: Количество очков атаки, которую наносит враг, сила атаки
        """
        if not isinstance(name, str):
            raise TypeError("Название врага должно быть типа str")
        # имя изменяться не может, поэтому делаем его непубличным
        self._name = name

        if not isinstance(health, int):
            raise TypeError("Здоровье врага должно быть типа int")
        elif health < 0:
            raise ValueError("Здоровье врага должно быть неотрицательным")
        self.health = health

        if not isinstance(attack, int):
            raise TypeError("Сила атаки должна быть типа int")
        elif attack < 0:
            raise ValueError("Сила атаки должна быть неотрицателен")
        self.attack = attack

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Название врага {self.name}. Количество здоровья {self.health}. Урон от атаки {self.attack}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, health={self.health!r}, attack={self.attack!r})"

    def apply_attack_buff(self, buff: float):
        """
        Метод, изменяющий урон в зависимости от баффа (buff)
        :param buff: Бафф, коэффициент, изменяющий силу атаки.
                    Может быть как больше 1, увеличивая силу атаки,
                    меньше 1, уменьшая силу атаки,
                    и равен 1, не изменяя силу атаки.
        Пример:
        >>> slime = Enemy('slime', 100, 50)
        >>> slime.apply_attack_buff(1.5)
        """
        if not isinstance(buff, float):
            raise TypeError("Коэффициент должен быть типа float")
        elif buff <= 0:
            raise ValueError("Коэффициент должен быть положителен")
        self.attack = round(self.attack * buff)

    def reduce_health(self, damage: int):
        """
        Метод, уменьшающий здоровье
        :param damage: Наносимый урон — количество очков, на которое уменьшится здоровье
        Пример:
        >>> slime = Enemy('slime', 100, 50)
        >>> slime.reduce_health(25)
        """
        if not isinstance(damage, int):
            raise TypeError("Наносимый урон должен быть типа int")
        elif damage < 0:
            raise ValueError("Наносимый урон должен быть неотрицателен")
        self.health -= damage


class Paladin(Enemy):
    """
    Класс Паладин. Дочерний класс класса Враг (Enemy).
    Характеризуется дополнительной характерстикой Защита от атаки

    Создание и подготовка к работе объекта Паладин
        :param name: Название врага
        :param health: Количество очков здоровья
        :param attack: Количество очков атаки, которую наносит враг, сила атаки
        :param defence: Количество очков защиты
    Пример:
    >>> Troy = Paladin('Troy', 500, 100, 200)
    """

    def __init__(self, name: str, health: int, attack: int, defence: int):
        """
        :param name: Название врага
        :param health: Количество очков здоровья
        :param attack: Количество очков атаки, которую наносит враг, сила атаки
        :param defence: Количество очков защиты
        """
        super().__init__(name, health, attack)
        if not isinstance(defence, int):
            raise TypeError("Количество очков защиты должно быть типа int")
        elif defence < 0:
            raise ValueError("Количество очков защиты должно быть неотрицательным")
        self.defence = defence

    def reduce_health(self, damage: int):
        """
        Метод, уменьшающий здоровье
        Перегружаем родительский метод, потому что у данного класса есть характеристика защиты,
            позволяющая сократить уменьшение здоровья
        :param damage: Наносимый урон — количество очков, на которое уменьшится здоровье
        Пример:
        >>> Troy = Paladin('Troy', 100, 100, 200)
        >>> Troy.reduce_health(50) #уменьшится только защита
        >>> Jeff = Paladin('Jeff', 100, 100, 200)
        >>> Jeff.reduce_health(250) #защита уменьшится до 0 и уменьшится здоровье
        """
        if not isinstance(damage, int):
            raise TypeError("Наносимый урон должен быть типа int")
        elif damage < 0:
            raise ValueError("Наносимый урон должен быть неотрицателен")

        # усли нанесенный урон больше, чем защита, то урон уменьшается на количество очков защиты,
        # а защита равняется 0
        if damage > self.defence:
            damage -= self.defence
            self.defence = 0
        # если урон равен защите, то оба становятся равны 0
        elif damage == self.defence:
            damage = 0
            self.defence = 0
        # если защита больше урона, то урон не наносится (равен 0), а защита уменьшается
        else:
            self.defence -= damage
            damage = 0

        self.health -= damage

    def __str__(self):
        return f"{super().__str__()} Защита {self.defence}."

    def __repr__(self):
        return f"{super().__repr__()}, defence={self.defence!r})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    pass
