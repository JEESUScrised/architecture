# Наследование, перегрузка метода, полиморфизм


class Person:
    def run(self):
        print("бежит")

    def fire(self):
        print("стреляет из обычного оружия")


class Desant(Person):
    def fight(self):
        print("бой в воздухе")

    def fire(self):  # перегрузка — своя реализация
        print("стреляет с плутониевой пушки")


class Morpeh(Person):
    def fight(self):
        print("бой в воде")

    def fire(self):
        print("стреляет из плазменной пушки")


def order_attack(soldier: Person):
    """Игра знает только про Person.attack — полиморфный вызов."""
    soldier.fire()


if __name__ == "__main__":
    kirill = Desant()
    ivan = Morpeh()

    kirill.run()   # метод родителя
    kirill.fight()
    order_attack(kirill)
    order_attack(ivan)
