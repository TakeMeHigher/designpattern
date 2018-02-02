# coding : utf-8
# create by ztypl on 2017/5/25

from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元" % money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元"%money)


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class ApplePayFactory(PaymentFactory):
    def create_payment(self):
        return ApplePay()




# 用户输入
# 支付宝，120

af = AlipayFactory()
ali = af.create_payment()
ali.pay(120)