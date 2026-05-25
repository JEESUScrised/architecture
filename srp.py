"""
S — Single Responsibility Principle (единственная ответственность).
Один класс — одна причина для изменения.
Пример из лекции: RentCarService разбит на несколько сервисов.
"""


class CarService:
    """Только поиск и бронирование машин."""

    def find_by_number(self, number: str) -> str:
        return f"машина {number}"

    def book(self, number: str) -> None:
        print(f"забронирована {number}")


class CarInfoService:
    """Только информация о типах машин — при новом типе меняем только этот класс."""

    def get_info(self, car_type: str) -> str:
        types = {
            "sedan": "легковой седан",
            "pickup": "пикап",
            "van": "фургон",
        }
        return types.get(car_type, "неизвестный тип")


class PrinterService:
    """Только печать заказа."""

    def print_order(self, order_id: int) -> None:
        print(f"печать заказа #{order_id}")


class NotificationService:
    """Только отправка уведомлений."""

    def send(self, message: str) -> None:
        print(f"email: {message}")


class RentCarService:
    """
    Координирует аренду, но не содержит логику печати, инфо о типах и отправки писем.
    Единственная зона ответственности — сценарий аренды.
    """

    def __init__(
        self,
        cars: CarService,
        info: CarInfoService,
        printer: PrinterService,
        notifications: NotificationService,
    ):
        self._cars = cars
        self._info = info
        self._printer = printer
        self._notifications = notifications

    def rent(self, number: str, car_type: str) -> None:
        car = self._cars.find_by_number(number)
        print(self._info.get_info(car_type))
        self._cars.book(number)
        self._printer.print_order(1)
        self._notifications.send(f"аренда оформлена: {car}")


if __name__ == "__main__":
    RentCarService(
        CarService(),
        CarInfoService(),
        PrinterService(),
        NotificationService(),
    ).rent("A123BC", "sedan")
