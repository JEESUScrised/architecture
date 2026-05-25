"""
D — Dependency Inversion Principle (инверсия зависимостей).
Shop (верхний уровень) зависит от абстракции Payment, а не от Cash.
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    """Абстракция — и магазин, и способы оплаты зависят от неё."""

    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class Cash(Payment):
    def pay(self, amount: float) -> None:
        print(f"оплата наличными: {amount} руб.")


class Card(Payment):
    def pay(self, amount: float) -> None:
        print(f"оплата картой: {amount} руб.")


class PhonePay(Payment):
    def pay(self, amount: float) -> None:
        print(f"оплата с телефона: {amount} руб.")


class Shop:
    """
    Магазин не знает про Cash/Card — получает Payment снаружи (DI).
    Новый способ оплаты = новый класс Payment, Shop не меняем.
    """

    def __init__(self, payment: Payment):
        self._payment = payment

    def buy(self, price: float) -> None:
        print(f"покупка на {price} руб.")
        self._payment.pay(price)


if __name__ == "__main__":
    for method in (Cash(), Card(), PhonePay()):
        shop = Shop(method)
        shop.buy(999)
