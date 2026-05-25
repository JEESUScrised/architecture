"""
I — Interface Segregation Principle (разделение интерфейсов).
Клиент не обязан реализовывать методы, которые ему не нужны.
"""

from abc import ABC, abstractmethod


# Плохо было бы одним жирным интерфейсом Payments с webmoney + card + phone.
# Терминалу телефонная оплата не нужна — выносим узкие контракты.


class WebMoneyPayment(ABC):
    @abstractmethod
    def pay_webmoney(self, amount: float) -> None:
        pass


class CardPayment(ABC):
    @abstractmethod
    def pay_card(self, amount: float) -> None:
        pass


class PhonePayment(ABC):
    @abstractmethod
    def pay_phone(self, amount: float) -> None:
        pass


class InternetPaymentService(WebMoneyPayment, CardPayment, PhonePayment):
    """Онлайн-сервис поддерживает все способы."""

    def pay_webmoney(self, amount: float) -> None:
        print(f"webmoney: {amount}")

    def pay_card(self, amount: float) -> None:
        print(f"карта: {amount}")

    def pay_phone(self, amount: float) -> None:
        print(f"телефон: {amount}")


class TerminalPaymentService(WebMoneyPayment, CardPayment):
    """
    Терминал — только webmoney и карта.
    Не имплементируем PhonePayment, значит не пишем заглушку pay_phone().
    """

    def pay_webmoney(self, amount: float) -> None:
        print(f"терминал webmoney: {amount}")

    def pay_card(self, amount: float) -> None:
        print(f"терминал карта: {amount}")


if __name__ == "__main__":
    InternetPaymentService().pay_phone(100)
    TerminalPaymentService().pay_card(50)
