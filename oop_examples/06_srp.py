# SRP: один класс — одна зона ответственности


# Плохо: класс делает всё сразу
class SoldierGodObject:
    def save_to_db(self):
        pass

    def send_email(self):
        pass

    def calculate_damage(self):
        return 10


# Лучше: обязанности разнесены
class DamageCalculator:
    def calculate(self) -> int:
        return 10


class SoldierRepository:
    def save(self, soldier_id: int):
        print(f"сохранён {soldier_id}")


class Soldier:
    def __init__(self, soldier_id: int, damage: DamageCalculator, repo: SoldierRepository):
        self.soldier_id = soldier_id
        self._damage = damage
        self._repo = repo

    def attack_power(self) -> int:
        return self._damage.calculate()

    def persist(self):
        self._repo.save(self.soldier_id)


if __name__ == "__main__":
    s = Soldier(1, DamageCalculator(), SoldierRepository())
    print(s.attack_power())
    s.persist()
