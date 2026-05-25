"""
L — Liskov Substitution Principle (подстановка Лисков).
Подтип можно подставить вместо базового типа без сюрпризов.
Плохой пример: DepositAccount наследует Account с payment(), который кидает ошибку.
Исправление: payment вынесен в отдельную ветку иерархии.
"""


class Account:
    """Базовый счёт: только то, что общее для всех типов."""

    def __init__(self, balance: float = 0):
        self._balance = balance

    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("сумма должна быть > 0")
        self._balance += amount


class PaymentAccount(Account):
    """Счёт, с которого можно платить — отдельная ветка, не все счета обязаны платить."""

    def payment(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("сумма должна быть > 0")
        if amount > self._balance:
            raise ValueError("недостаточно средств")
        self._balance -= amount


class DepositAccount(Account):
    """Депозит: пополнение и просмотр — payment() здесь не нужен и не ломает LSP."""

    pass


class SalaryAccount(PaymentAccount):
    """Зарплатный счёт — полная замена PaymentAccount в коде клиента."""

    pass


def print_balance(account: Account) -> None:
    """Работает для Account, DepositAccount, PaymentAccount, SalaryAccount."""
    print(f"остаток: {account.balance()}")


def pay_from(account: PaymentAccount, amount: float) -> None:
    account.payment(amount)
    print(f"оплачено {amount}, остаток {account.balance()}")


if __name__ == "__main__":
    deposit = DepositAccount(1000)
    salary = SalaryAccount(5000)

    print_balance(deposit)
    print_balance(salary)

    deposit.deposit(200)
    pay_from(salary, 1500)

    # pay_from(deposit, 100)  # TypeError — компилятор/типы не дадут, а не Exception в рантайме
