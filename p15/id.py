#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sort_list(func):
    """
    Сортировка списка
    """
    def wrapper(*args):
        arg = args[0]
        sort_line = sorted(func(arg))
        return sort_line
    return wrapper


@sort_list
def get_list(line):
    """
    Создание списка из строки цифр разделенных пробелами
    """
    new_line = [int(i) for i in line.split()]
    return new_line


if __name__ == '__main__':
    s = input("Enter line: ")
    print(get_list(s))
