# coding : utf-8
# create by ztypl on 2017/5/25

from abc import abstractmethod, ABCMeta

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name=None):
        if name is not None:
            self.name = name


a = MyClass("a")

print(a)
print(a.name)

b = MyClass("b")

print(b)
print(b.name)

print(a)
print(a.name)
