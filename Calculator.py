import math

class Calculator:
    def __init__(self):
        self.result = 0

    def get_user_input(self):
        try:
            self.num1 = float(input("Введіть перше число: "))
            self.operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            if self.operator != "√":  # Для квадратного кореня потрібно тільки одне число
                self.num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка: введіть дійсне число.")
            return False
        return True

    def check_operator(self):
        if self.operator in ['+', '-', '*', '/', '^', '√', '%']:
            return True
        else:
            print("Помилка: недійсний оператор.")
            return False

    def calculate(self):
        try:
            if self.operator == '+':
                self.result = self.num1 + self.num2
            elif self.operator == '-':
                self.result = self.num1 - self.num2
            elif self.operator == '*':
                self.result = self.num1 * self.num2
            elif self.operator == '/':
                if self.num2 == 0:
                    raise ZeroDivisionError
                self.result = self.num1 / self.num2
            elif self.operator == '^':
                self.result = self.num1 ** self.num2
            elif self.operator == '√':
                if self.num1 < 0:
                    raise ValueError("Неможливо обчислити квадратний корінь з від'ємного числа.")
                self.result = math.sqrt(self.num1)
            elif self.operator == '%':
                self.result = self.num1 % self.num2
        except ZeroDivisionError:
            print("Помилка: ділення на нуль.")
            return False
        except ValueError as e:
            print(e)
            return False
        return True

    def display_result(self):
        print(f"Результат: {self.result}")

    def ask_for_repeat(self):
        repeat = input("Бажаєте виконати ще одне обчислення? (так/ні): ").strip().lower()
        return repeat == 'так'

    def run(self):
        while True:
            if not self.get_user_input():
                continue
            if not self.check_operator():
                continue
            if not self.calculate():
                continue
            self.display_result()
            if not self.ask_for_repeat():
                print("Дякую за використання калькулятора!")
                break

# Створюємо об'єкт калькулятора та запускаємо його
calculator = Calculator()
calculator.run()
