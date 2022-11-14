from lesson import add_one, division, add_number 
import pytest

"""Оператор assert -> принимает условие и необезательное сообщение , если условие ложно выведет сообщение
 .Если условие истина ,то ничего не происходиит и будет выполняться следущая строчка кода которую мы передали
 Используется для проверки ожидаемого результата, проверяет верно ли наи это условие True,
 в противном случае тест упадет """


def test_answer():
    assert add_one(5) == 6



def test_add_one():
    assert add_one(4) == 6


def test_division():
    assert division(6, 3) == 3, 'Oops'


def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        division(9, 0)


def test_passing():
    test_case = [[1, 2, 3], [1, 1, 2], [3, 6, 9]]
    for t in test_case:
        assert add_number(t[0], t[1]) == t[2]




