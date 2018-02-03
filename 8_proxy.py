# coding : utf-8
# create by ctz on 2017/5/26

from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        print("读取%s文件内容"%filename)
        f = open(filename)
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w')
        f.write(content)
        f.close()



class ProxyA(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()


class ProxyB(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()


class ProxyC(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.get_content()

    def set_content(self):
        raise PermissionError

    # 写一个set_content

b = ProxyB("abc.txt")
#print(b.get_content())