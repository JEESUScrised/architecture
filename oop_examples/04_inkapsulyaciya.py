# Инкапсуляция: сокрытие поля, геттер/сеттер с валидацией


class Wallet:
    def __init__(self, balance: int = 0):
        self._balance = balance  # «приватное» поле по соглашению

    def get_balance(self):
        return self._balance

    def set_balance(self, value: int):
        if value < 0:
            raise ValueError("баланс не может быть отрицательным")
        self._balance = value

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("сумма должна быть положительной")
        self._balance += amount


if __name__ == "__main__":
    w = Wallet(100)
    w.deposit(50)
    print(w.get_balance())  # 150
    # w._balance = -10  # так можно, но снаружи лучше через методы
