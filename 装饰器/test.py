import time


def set_func(func):
    def call_func():
        print("---验证1---")
        print("---验证2---")
        start_time = time.time()
        func()
        stop_time = time.time()
        print("alltimes %f" % (stop_time - start_time))

    return call_func


@set_func  # 等价于 test1 = set_func(test1)
def test1():
    print("-----test1-----")
    for i in range(100000):
        pass


test1()


# 有参数

def set_func(func):
    def call_func(num):
        print("---验证1---")
        print("---验证2---")
        start_time = time.time()
        func(num)
        stop_time = time.time()
        print("alltimes %f" % (stop_time - start_time))

    return call_func


@set_func  # 等价于 test1 = set_func(test1)
def test1(num):
    print("-----test1-----%d" % num)
    for i in range(100000):
        pass


test1(100)


# 不定长参数

def set_func(func):
    def call_func(*args, **kwargs):
        func(*args, **kwargs)

    return call_func


@set_func  # 等价于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("-----test1-----%d" % num)
    print("-----test1-----", args)
    print("-----test1-----", kwargs)


test1(100)
test1(100, 200)
test1(100, 200, 300, mm=100)


# 有返回值

def set_func(func):
    def call_func(*args, **kwargs):
        return func(*args, **kwargs)

    return call_func


@set_func  # 等价于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("-----test1-----%d" % num)
    print("-----test1-----", args)
    print("-----test1-----", kwargs)
    return "ok"


test1(100)
test1(100, 200)
ret = test1(100, 200, 300, mm=100)
print(ret)

print("-" * 500)


# 多个装饰器
def set_func1(func):
    print("装饰器1")

    def call_func(*args, **kwargs):
        print("权限验证1")
        return func(*args, **kwargs)

    return call_func


def set_func2(func):
    print("装饰器2")

    def call_func(*args, **kwargs):
        print("权限验证2")
        return func(*args, **kwargs)

    return call_func


@set_func1  # test1 = set_func1(test1)
@set_func2  # test1 = set_func2(test1)
def test1(num, *args, **kwargs):
    print("-----test1-----%d" % num)
    print("-----test1-----", args)
    print("-----test1-----", kwargs)
    return "ok"


print(test1(100))

print("-" * 500)


class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("这里是装饰添加的功能")
        return self.func()


@Test  # 相当于 get_str = Test(get_str)
def get_str():
    return "hahaha"


print(get_str())


def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("权限级别1，验证")
            elif level_num == 2:
                print("权限级别2，验证")
            return func(*args, **kwargs)

        return call_func
    return set_func

@set_level(1)
def get_str():
    return "hahaha"


@set_level(2)
def get_str2():
    return "hahaha"

get_str()
get_str2()