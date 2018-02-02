# coding : utf-8
# create by ztypl on 2017/5/25

from abc import abstractmethod, ABCMeta

class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def add(self, graphic):
        pass

    @abstractmethod
    def getchildren(self):
        pass


class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(self)

    def add(self, graphic):
        raise TypeError

    def getchildren(self):
        raise TypeError

    def __str__(self):
        return "点(%s, %s)" % (self.x, self.y)


class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        print(self)

    def add(self, graphic):
        raise TypeError

    def getchildren(self):
        raise TypeError

    def __str__(self):
        return "线段[%s, %s]" % (self.p1, self.p2)


class Picture(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic):
        self.children.append(graphic)

    def getchildren(self):
        return self.children

    def draw(self):
        print("------复合图形------")
        for g in self.children:
            g.draw()
        print("------END------")


pic1 = Picture()
pic1.add(Point(2,3))
pic1.add(Line(Point(1,2), Point(4,5)))
pic1.add(Line(Point(0,1), Point(2,1)))

pic2 = Picture()
pic2.add(Point(-2,-1))
pic2.add(Line(Point(0,0), Point(1,1)))

pic = Picture()
pic.add(pic1)
pic.add(pic2)

pic.draw()


