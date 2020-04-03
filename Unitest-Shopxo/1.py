class Person(object):
    # 构造方法，固定的写法：初始化类
    def __init__(self, xb=None, mz=None):
        self.sex = xb
        self.name = mz
        # self.test1 = None #无地址
        # self.test2 = "" #有地址，但是为空


if __name__ == "__main__":
    d1 = Person("女", "王广发")
    print(d1.sex)
    print(d1.name)
    # d1.test2.count()

    d2 = Person()
    print(d2.sex)
    print(d2.name)
    #
    # if d1.name is not None:
    #     print(True)
    # else:
    #     print(False)
    # if d2.name is not None:
    #     print(True)
    # else:
    #     print(False)
