# Классы и объекты: поля, методы, конструктор, self


class Person:
    def __init__(self, x: int = 0):
        self.x = x  # поле объекта

    def run(self):
        self.x += 1  # метод работает с собственным состоянием


if __name__ == "__main__":
    kirill = Person(0)  # new / создание экземпляра
    kirill.run()
    print(kirill.x)  # 1
    kirill.run()
    print(kirill.x)  # 2
