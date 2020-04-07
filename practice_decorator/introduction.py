__author__ = 'TQ'
# 开放封闭原则：对于函数和类不要在内部改，在外部改,对于外部是开放的


def outer(func):
    def inner():
        print("log")
        return func()

    return inner


@outer
def f1():
    print("f1")


@outer
def f2():
    print("f2")


def f100():  # 假设这个是100个函数
    print("f100")


f1()
f2()
