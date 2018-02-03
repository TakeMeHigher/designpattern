# coding : utf-8
# create by ztypl on 2017/5/27


class LinkList:
    """链表 头结点保存链表的长度"""
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node
        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration
        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = LinkList.Node(0)
        self.tail = self.head
        self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        self.tail.next = s
        self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)
        self.head.item += len(iterable)

    def __iter__(self):
        return self.LinkListIterator(self.head.next)

    def __len__(self):
        return self.head.item

    def __str__(self):
        return "<<"+", ".join(map(str, self))+">>"



li = [i for i in range(100)]
print(li)
lk = LinkList(li)
# for i in lk:
#     print(i)

print(lk)
# print(len(lk))