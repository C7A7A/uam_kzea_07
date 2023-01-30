from .tasks.addition import add
from .tasks.xtime import xtime
from .tasks.helper import hex_to_bin
from .tasks.multiplication import multiply


def start():
    x = input("Enter x: ")
    y = input("Enter y: ")
    # x = "FF"
    # y = "FF"
    print("x: ", x)
    print("xBin: ", hex_to_bin(x))
    print("y: ", y)
    print("yBin: ", hex_to_bin(y))

    result_add = add(x, y)
    print("add: ", result_add)
    print("addBin: ", hex_to_bin(result_add))

    result_x_time = xtime(x)
    print("xtime: ", result_x_time)
    print("xtimeBin: ", hex_to_bin(result_x_time))

    result_multiply = multiply(x, y)
    print("multiply: ", result_multiply)
    print("multiplyBin: ", hex_to_bin(result_multiply))
