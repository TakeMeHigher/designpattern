# coding : utf-8
# create by ztypl on 2017/5/24

from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def __init__(self, enable_yuebao=False):
        self.enable_yuebao = enable_yuebao

    def pay(self, money):
        if self.enable_yuebao:
            print("余额宝支付%s元" % money)
        else:
            print("支付宝支付%s元" % money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元" % money)


class PaymentFactory:  # 工厂类 封装了对象创建的细节
    def create_payment(self, method):
        if method == "alipay":
            return Alipay()
        elif method == "applepay":
            return ApplePay()
        elif method == "yuebao":
            return Alipay(True)
        else:
            raise NameError(method)

factory = PaymentFactory()
payment = factory.create_payment("yuebao")
payment.pay(100)
