from .helper import hex_to_bin


#TODO: to można zrobić na stringach (wtedy >> i xor (^), ale trzeba jakoś ograniczyć wielkość liczb???
def xtime(x):
    ideal = hex_to_bin("1B")

    if x[0] == "0":
        result = x[1:] + '0'
    elif x[0] == "1":
        x = x[1:] + '0'

        result = ""
        for idx, num in enumerate(x):
            result += xor(num, ideal[idx])
    else:
        result = hex_to_bin("00")
        print("ARGUMENT ERROR")

    return result


def xor(x, y):
    if x != y:
        return "1"
    return "0"
