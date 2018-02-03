# coding : utf-8
# create by ztypl on 2017/5/27

from abc import ABCMeta, abstractmethod


class IOHandler(metaclass=ABCMeta):
    @abstractmethod
    def open(self, name):
        pass
    @abstractmethod
    def deal(self, change):
        pass
    @abstractmethod
    def close(self):
        pass
    def process(self, name, change):
        self.open(name)
        self.deal(change)
        self.close()


class FileHandler(IOHandler):



