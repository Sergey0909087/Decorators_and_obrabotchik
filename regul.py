# from functools import wraps
# from functools import cache

# def decor(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

# def func(a,b):
#     """Функция возвращает сложение двух чисел"""
#     return (a + b)

# func(111, 111)

# print(func(1,5))
# print(func.__doc__)
# print(func.__name__)

# @decor
# def func(a,b):
#     """Функция возращает сложение двух чисел"""
#     return a+b

# def decor(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

# @cache
# def  func(n):
#     result = 0
#     for i in range(n):
#         result += i
#     return result

# import time

# start = time.time()
# print(func(10000000))
# end = time.time()
# print(end - start)


# start = time.time()
# print(func(10000000))
# end = time.time()
# print(end - start)
# start1 = time.time()
# print(func(10000))
# end1 = time.time()
# print(end1 - start1)

try:
    k = 1 / 0
except ZeroDivisionError:
    k = 10

print(k)