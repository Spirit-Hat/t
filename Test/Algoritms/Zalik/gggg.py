def function_1():
    return 7.5 / 0.5


def function_2():
    return 12.4 / 0.4


def function_3():
    return 6.3 / 0.3


def function_4():
    return 4.6 / 0.2


def function_5(a, b, c, d):
    return (a - b) / (c - d)


a = function_1()
b = function_2()
c = function_3()
d = function_4()

print(function_5(a, b, c, d))