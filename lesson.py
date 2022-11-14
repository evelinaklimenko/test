def add_one(x):
    return x+1


# . venv/bin/activate ->активирует виртуальную реальность 


def division(x: int, y:int) -> float:
    if y == 0:
        raise  ZeroDivisionError
    return x/y



def add_number(x:int, y:int) -> int:
    return x + y 