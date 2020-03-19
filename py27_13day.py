# -------------------------------不使用继承实现的需求代码-------------------------
# 需求1:V1大哥大


class PhoneV1(object):
    def phone(self):
        print('打电话的功能')


# 需求二:V2:功能机
class PhoneV2(object):
    def phone(self):
        print('打电话的功能')

    def music(self):
        print('听音乐的功能')

    def send_msg(self):
        print('发信息的功能')


# 需求三:V3:智能机
class PhoneV3(object):
    def phone(self):
        print('打电话的功能')

    def music(self):
        print('听音乐的功能')

    def send_msg(self):
        print('发送信息的功能')

    def pay(self):
        print('手机支付的功能')

    def game(self):
        print('玩游戏的功能')


# -------------------------------使用继承实现的需求代码-------------------------
class Cls_PhoneV1(object):
    def phone(self):
        print('打电话的功能')


class Cls_PhoneV2(Cls_PhoneV1):
    def music(self):
        print('听音乐的功能')

    def send_msg(self):
        print('发送信息的功能')


class Cls_PhoneV3(Cls_PhoneV2):
    def pay(self):
        print('支付功能')

    def game(self):
        print('完游戏的功能')


# 实例化三个类
v1 = Cls_PhoneV1()
v2 = Cls_PhoneV2()
v3 = Cls_PhoneV3()

# 用实例化对象调用phone方法
v1.phone()
v2.phone()
v3.phone()

# v2 实例化后调用自身方法
v2.music()
v2.send_msg()

# v3 实例化后调用自身方法
v3.pay()
v3.game()

# v3继承v2和v1的方法
v3.phone()
v3.music()
v3.send_msg()

print('--------------------------------第二题-------------------------------')

# 2、有一组数据，如下格式：
# {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
# 定义一个如下的类，请通过setattr将上面字典中的键值对，分别设置为类的属性和属性值，键作为属性名，对应的值作为属性值
# class CaseData:
#     pass

dic = {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'}


# 定义一个类
class CaseData:
    pass


# 定义一个动态设置类属性的方法
def attr():
    for key, value in dic.items():
        setattr(CaseData, key, value)
    return CaseData


attr()
