from .tasks.addition import addition
from .tasks.xtime import xtime
from .tasks.helper import hex_to_bin


def start():
    # x = input("Enter x: ")
    # y = input("Enter y: ")
    x = hex_to_bin("11")
    y = hex_to_bin("0E")
    print(x)
    print(y)
    print(addition(x, y))
    print(xtime(x))
