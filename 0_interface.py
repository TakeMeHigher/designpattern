# coding : utf-8
# create by ztypl on 2017/5/24

from abc import abstractmethod, ABCMeta

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元"%money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元"%money)

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%s元"%money)



payment = Alipay()
payment.pay(100)
