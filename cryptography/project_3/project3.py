from .tasks.addition import add
from .tasks.xtime import xtime
from .tasks.helper import hex_to_bin
from .tasks.multiplication import multiply


def start():
    # x = input("Enter x: ")
    # y = input("Enter y: ")
    x = "FF"
    y = "10"
    # print(x)
    # print(y)
    # print("Addition: ", addition(x, y))

    # result_x_time = xtime(x)
    # print("Xtime: ", result_x_time)
    # print("XtimeBin: ", hex_to_bin(result_x_time))

    print(multiply(x, y))
