"""
https://nuancesprog.ru/p/4567
Логирование через Python-декоратора

Реализуйте класс Calculator через следующие функции:
Sum(a,b), Multiply(a,b), Divide(a,b) и Subtract(a,b).

Импортируйте библиотеку логирования.

Декорируйте каждый метод класса Calculator пользовательским методом, который регистрирует значения a и b. Реализуйте пользовательский метод логгера.

Выполните calculator.Sum(a,b). Он должен выводить значения a и b. Например:

Входными значениями A и B являются ‘123’ и ‘234’, # если a =123 и b=234

"""
import logging
class Calculator:

    #Класс декоратор для логирования
    logging.basicConfig(level=logging.INFO, format ='%(levelname)s-%(message)s')
    def log_variables(func):
        def inner(*args):
            logging.info(f'Входными значениями A и B являются "{args[1]}" и "{args[2]}"')
            return func(*args)
        return inner

    @log_variables
    def Sum(self, a, b):
        return a + b

    @log_variables
    def Multiply(self, a, b):
        return a * b

    @log_variables
    def Divide(self, a ,b):
        return a / b

    @log_variables
    def Substract(self, a, b):
        return a - b
