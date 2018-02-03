# coding : utf-8
# create by ctz on 2017/5/27

from abc import ABCMeta, abstractmethod
#
# class Handler(metaclass=ABCMeta):
#     @abstractmethod
#     def handle_leave(self, day):
#         pass
#
#
# class GeneralManagerHandler(Handler):
#     def handle_leave(self, day):
#         if day < 10:
#             print("总经理批准%d天假"%day)
#         else:
#             print("呵呵")
#
#
# class DepartmentManagerHandler(Handler):
#     def __init__(self):
#         self.successor = GeneralManagerHandler()
#     def handle_leave(self, day):
#         if day < 7:
#             print("部门经理批准%d天假"%day)
#         else:
#             print("部门经理无权准假")
#             self.successor.handle_leave(day)
#
#
# class ProjectDirectorHandler(Handler):
#     def __init__(self):
#         self.successor = DepartmentManagerHandler()
#     def handle_leave(self, day):
#         if day < 3:
#             print("项目主管批准%d天假")
#         else:
#             print("项目主管无权准假")
#             self.successor.handle_leave(day)
#
#
# day = 4
# h = ProjectDirectorHandler()
# h.handle_leave(day)
#


#--高级例子--模仿js事件处理

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def add_event(self, func):
        pass

    @abstractmethod
    def handle(self):
        pass


class BodyHandler(Handler):
    def __init__(self):
        self.func = None

    def add_event(self, func):
        self.func = func

    def handle(self):
        if self.func:
            return self.func()
        else:
            print("已到最后一级，无法处理")


class ElementHandler(Handler):
    def __init__(self, successor):
        self.func = None
        self.successor = successor

    def add_event(self, func):
        self.func = func

    def handle(self):
        if self.func:
            return self.func()
        else:
            return self.successor.handle()


# 客户端

# <body><div><a>

body = {'type': 'body', 'name': 'body', 'children': [], 'father': None}

div = {'type': 'div', 'name': 'div', 'children': [], 'father': body}

a = {'type': 'a', 'name': 'a', 'children': [], 'father': div}

body['children'].append(div)
div['children'].append(a)

body['event_handler'] = BodyHandler()
div['event_handler'] = ElementHandler(div['father']['event_handler'])
a['event_handler'] = ElementHandler(a['father']['event_handler'])


def attach_event(element, func):
    element['event_handler'].add_event(func)

#test

def func_div():
    print("这是给div的函数")

def func_a():
    print("这是给a的函数")

def func_body():
    print("这是给body的函数")

#attach_event(div, func_div)
#attach_event(a, func_a)
#attach_event(body, func_body)





a['event_handler'].handle()