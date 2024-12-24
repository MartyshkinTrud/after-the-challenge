'''
1) Вывести равнобедренный треугольник из символа "*" (высота указывается с клавиатуры)
'''

#
# h = int(input('введите высоту треугольника '))
# j = 1
# while h != 0:
#     print(' ' * (h - 1) + '*' * j)
#     h -= 1
#     j += 2
'''

2) Есть список из 10 элементов. Найти наибольшее и наименьшее число в списке 
'''

# import random
#
# practice_list = [random.randint(1, 100) for _ in range(10)]
# print(practice_list)
#
# max_elem = practice_list[0]
# min_elem = practice_list[0]
#
# for i in practice_list:
#     if i > max_elem:
#         max_elem = i
#     elif i < min_elem:
#         min_elem = i
#
# print("наибольшее число:", max_elem)
# print("наименьшее число:", min_elem)
'''
3) Написать функцию, которая будет обменивать местами первую и последнюю цифру числа N (1234 → 4231)
'''
# N = 1234
# a = N // 1000
# b = N % 10
# d = (N % 1000) // 10
# result = (int(( str(b)+str(d) +str(a))))
# print(result)
#
# def swap_first_last(N):
#     str_N = str(N)
#     return int(str_N[-1] + str_N[1:-1] + str_N[0])
#
# N = 1234
# print(swap_first_last(N))
'''

4) Необходимо написать программу, которая сможет посчитать повторяющиеся символы и вывести сокращенную строку, пример:
Вход: s = 'aaaabbcaa'
Выход: 'a4b2c1a2'
'''
#
# s = 'aaaabbcaa'
# b = s[0]
# sum_str = 0
# str_new = []
# 
# for i in s:
#     if i == b:
#         sum_str += 1
#     else:
#         str_new.append(b)
#         str_new.append(str(sum_str))
#         b = i
#         sum_str = 1
# str_new.append(b)
# str_new.append(str(sum_str))
# 
# print(''.join(str_new))
#

'''
5) Когда Антон прочитал «Войну и мир», ему стало интересно, 
сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, 
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и 
выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) 
в формате "слово: количество;"
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз
(из урока 6 (https://t.me/semolina_code_python/16))
'''

# s = input().lower().split()
# words = {}
# 
# for word in s:
#     if word in words:
#         words[word] += 1
#     else:
#         words[word] = 1
# for word, count in words.items():
#     print(f"{word}: {count};")
'''
6) Создайте класс Vector с полями x и y, определите для него конструктор, метод str, необходимые арифметические операции:
сложение (add)
вычитание (sub)
умножение на число справа (mul) и слева (rmul)
отрицание (унарный минус neg)
'''
# class Vector:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)

#     def __mul__(self, other):
#         return Vector(self.x * other, self.y * other)

#     def __rmul__(self, other):
#         return self.__mul__(other)

#     def __neg__(self):
#         return Vector(self.x *-1, self.y *-1)




