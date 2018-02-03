# coding : utf-8
# create by ctz on 2017/5/27

from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass


class Notice:
    def __init__(self):
        self.observers = [] # 记录该主体的观察者（订阅者）

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        obs.company_info = None
        self.observers.remove(obs)

    def notify(self):
        for obj in self.observers:
            obj.update(self)


class ManagerNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()



class Manager(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, noti):
        self.company_info = noti.company_info


notice = ManagerNotice()

alex = Manager()
wusir = Manager()

# print(alex.company_info)
# print(wusir.company_info)

notice.attach(alex)
notice.attach(wusir)
#
notice.company_info="公司运行良好"
#
print(alex.company_info)
print(wusir.company_info)
#
notice.detach(wusir)
#
notice.company_info="公司要破产了"

print(alex.company_info)
print(wusir.company_info)





