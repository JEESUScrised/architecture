# Интерфейсы (ABC), композиция слотов, ISP — узкие интерфейсы


from abc import ABC, abstractmethod


class IWeapon(ABC):
    @abstractmethod
    def fire(self):
        pass


class IMedicine(ABC):
    @abstractmethod
    def heal(self):
        pass


class LaserGun(IWeapon):
    def fire(self):
        print("лазерный выстрел")


class FirstAidKit(IMedicine):
    def heal(self):
        print("аптечка: лечение")


class Person:
    def __init__(self):
        self.slot_weapon: IWeapon | None = None
        self.slot_medicine: IMedicine | None = None

    def install_weapon(self, weapon: IWeapon):
        self.slot_weapon = weapon

    def install_medicine(self, medicine: IMedicine):
        self.slot_medicine = medicine

    def use_weapon(self):
        if self.slot_weapon:
            self.slot_weapon.fire()


class PersonFactory:
    def build(self) -> Person:
        person = Person()
        person.install_weapon(LaserGun())
        person.install_medicine(FirstAidKit())
        return person


# Утиная типизация: объект без наследования, но с нужным методом
class FakeGun:
    def fire(self):
        print("что-то стреляет как пушка")


if __name__ == "__main__":
    oleg = PersonFactory().build()
    oleg.use_weapon()

    p = Person()
    p.install_weapon(FakeGun())  # не наследует IWeapon, но fire() есть
    p.use_weapon()
