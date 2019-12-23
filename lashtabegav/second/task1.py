"""
Використовуючи регулярні вирази, для поданого
нижче тексту замініть кожне число на його шіснадцяткове представлення.
Виведіть результат.
"""
import re

def read(q):
    x=input(q)
    while not re.match(r'(?:[0]\.\d+)|(?:[1-9]\d*(?:\.\d+)?)', x):
        x= input(q)
    return float(x)

def convert_base(num, to_base=10, from_base=10):
    if isinsance(num, str):
        n = int(num, from_base)
    else:
        n=int(num)
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

number = read('Введіть число: ')
convert_base(number, to_base=16, from_base=10)