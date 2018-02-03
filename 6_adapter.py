# coding : utf-8
# create by ctz on 2017/5/25

from abc import abstractmethod, ABCMeta

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元"%money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元"%money)

#------待适配类------

class WechatPay:
    def huaqian(self, a, b):
        print("微信支付%s元"%(a+b))

#------类适配器------

class RealWeChatPay(Payment, WechatPay):
    def pay(self, money):
        return self.huaqian(money, 0)


#------对象适配器------
class PayAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        return self.payment.huaqian(money, 0)


#RealWeChatPay().pay(100)
PayAdapter(WechatPay()).pay(1000)