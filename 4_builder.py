# coding : utf-8
# create by ztypl on 2017/5/25

import random
from abc import abstractmethod, ABCMeta

#------产品------

class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.arm = arm
        self.leg = leg
        self.body = body

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.arm, self.body, self.leg)


#------建造者------


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass
    @abstractmethod
    def build_arm(self):
        pass
    @abstractmethod
    def build_leg(self):
        pass
    @abstractmethod
    def build_body(self):
        pass
    @abstractmethod
    def get_player(self):
        pass


class BeautifulWomanBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    def build_face(self):
        self.player.face = "漂亮脸蛋"
    def build_arm(self):
        self.player.arm="细胳膊"
    def build_body(self):
        self.player.body="细腰"
    def build_leg(self):
        self.player.leg="长腿"
    def get_player(self):
        return self.player

class RandomPlayerBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    def build_face(self):
        self.player.face = random.choice(["瓜子脸","西瓜子脸"])
    def build_arm(self):
        self.player.arm=random.choice(["长胳膊","短胳膊"])
    def build_body(self):
        self.player.body=random.choice(["苗条","胖"])
    def build_leg(self):
        self.player.leg=random.choice(["长腿","短腿"])
    def get_player(self):
        return self.player

class PlayerDirector:
    def __init__(self, builder):
        self.builder = builder
    # 控制组装顺序
    def build_player(self):
        self.builder.build_body()
        self.builder.build_face()
        self.builder.build_arm()
        self.builder.build_leg()
        return self.builder.get_player()




pd = PlayerDirector(RandomPlayerBuilder())
p = pd.build_player()
print(p)



