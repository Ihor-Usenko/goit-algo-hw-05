def caching_fibonacci():

    cache = {}  # Зберігаємо кеш у словник.

    def fibonacci(n):
        if n in cache:  # Якщо у словнику значення вже існує, то повертаємо.
            return cache[n]
        elif n <= 1:  # Базовий випадок.
            return n
        else:
            # Рекурсивно вираховуєм число Фібоначчі.
            fib_value = fibonacci(n - 1) + fibonacci(n - 2)
            # Зберігаємо значення в кеше.
            cache[n] = fib_value
            return fib_value
    return fibonacci


fib = caching_fibonacci()

print(fib(5))
