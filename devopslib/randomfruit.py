from random import choices


def fruit() -> str:
    """
    returns random Fruit
    """
    fruits = ["apple", "orange", "mango"]
    return choices(fruits)[0]
