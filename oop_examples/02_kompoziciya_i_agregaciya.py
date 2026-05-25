# Ассоциация: композиция (пушка живёт с человеком) и агрегация (пушку передали снаружи)


class Gun:
    def __init__(self):
        self.ammo_count = 0
        self.reload()

    def fire(self):
        if self.ammo_count > 0:
            self.ammo_count -= 1

    def reload(self):
        self.ammo_count = 10


class PersonWithGuns:
    """Агрегация: пушки создаются снаружи и передаются в конструктор."""

    def __init__(self, gun_left: Gun, gun_right: Gun):
        self.gun_left = gun_left
        self.gun_right = gun_right

    def fire(self):
        self.gun_left.fire()
        self.gun_right.fire()


class PersonComposition:
    """Композиция: пушки создаются внутри — умирают вместе с человеком."""

    def __init__(self):
        self.gun_left = Gun()
        self.gun_right = Gun()


if __name__ == "__main__":
    g1, g2 = Gun(), Gun()
    soldier = PersonWithGuns(g1, g2)
    soldier.fire()
    print(g1.ammo_count, g2.ammo_count)  # 9, 9

    comp = PersonComposition()
    comp.gun_left.fire()
    print(comp.gun_left.ammo_count)  # 9
