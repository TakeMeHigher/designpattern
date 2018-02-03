# coding : utf-8
# create by ztypl on 2017/5/27

from abc import ABCMeta, abstractmethod
import random

class Sort(metaclass=ABCMeta):
    @abstractmethod
    def sort(self, data):
        pass


class QuickSort(Sort):
    def quick_sort(self, data, left, right):
        if left < right:
            mid = self.partition(data, left, right)
            self.quick_sort(data, left, mid - 1)
            self.quick_sort(data, mid + 1, right)

    def partition(self, data, left, right):
        tmp = data[left]
        while left < right:
            while left < right and data[right] >= tmp:
                right -= 1
            data[left] = data[right]
            while left < right and data[left] <= tmp:
                left += 1
            data[right] = data[left]
        data[left] = tmp
        return left

    def sort(self, data):
        print("快速排序")
        return self.quick_sort(data, 0, len(data) - 1)


class MergeSort(Sort):
    def merge(self, data, low, mid, high):
        i = low
        j = mid + 1
        ltmp = []
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                ltmp.append(data[i])
                i += 1
            else:
                ltmp.append(data[j])
                j += 1

        while i <= mid:
            ltmp.append(data[i])
            i += 1

        while j <= high:
            ltmp.append(data[j])
            j += 1

        data[low:high + 1] = ltmp


    def merge_sort(self, data, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(data, low, mid)
            self.merge_sort(data, mid + 1, high)
            self.merge(data, low, mid, high)

    def sort(self, data):
        print("归并排序")
        return self.merge_sort(data, 0, len(data) - 1)


class Context:
    def __init__(self, data, strategy=None):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        if self.strategy:
            self.strategy.sort(self.data)
        else:
            raise TypeError


li = list(range(100000))
random.shuffle(li)

context = Context(li, MergeSort())
context.do_strategy()
#print(context.data)

random.shuffle(context.data)

context.set_strategy(QuickSort())
context.do_strategy()
