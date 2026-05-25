"""
O — Open/Closed Principle (открыт для расширения, закрыт для изменения).
Новый способ уведомления добавляем новым классом, старый код не трогаем.
"""

from abc import ABC, abstractmethod


class NotificationService(ABC):
    """Абстракция — контракт для всех каналов отправки."""

    @abstractmethod
    def send_message(self, text: str) -> None:
        pass


class EmailNotification(NotificationService):
    def send_message(self, text: str) -> None:
        print(f"[email] {text}")


class SmsNotification(NotificationService):
    """Новый канал — расширение без правки EmailNotification и без if/else в одном методе."""

    def send_message(self, text: str) -> None:
        print(f"[sms] {text}")


class PushNotification(NotificationService):
    def send_message(self, text: str) -> None:
        print(f"[push] {text}")


def notify_all(services: list[NotificationService], text: str) -> None:
    for service in services:
        service.send_message(text)


if __name__ == "__main__":
    channels = [EmailNotification(), SmsNotification(), PushNotification()]
    notify_all(channels, "ваша машина готова")
