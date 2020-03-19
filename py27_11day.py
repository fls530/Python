import random

print('------------第一题------------------')
li = ['石头', '剪刀', '布']
print('---石头剪刀布游戏开始---')
print('请按下面提示出拳:')
print('【1】石头【2】剪刀【3】布【4】结束游戏')
x = True
while x:
    try:
        i = int(input('请输入你的选项:'))
    except Exception as e:
        print('输入有误请重新输入!,错误信息:{}'.format(e))
    else:
        if i == 4:
            print('结束游戏!')
            x = False
        elif 1 <= i <= 3:
            r = random.randint(1, 3)
            if i == r:
                print('您出:{0},电脑出:{1},平局!'.format(li[i - 1], li[r - 1]))
            elif i == 1 and r == 2:
                print('您出:{0},电脑出:{1},您胜利了!'.format(li[i - 1], li[r - 1]))
            elif i == 2 and r == 3:
                print('您出:{0},电脑出:{1},您胜利了!'.format(li[i - 1], li[r - 1]))
            elif i == 3 and r == 1:
                print('您出:{0},电脑出:{1},您胜利了!'.format(li[i - 1], li[r - 1]))
            else:
                print('您出:{0},电脑出:{1},您失败了!'.format(li[i - 1], li[r - 1]))
        else:
            print('请按规则输入!')

print('------------第二题------------------')
print('try:        对有可能出错的代码进行捕获异常.'
      'except:     try里代码出现异常时,执行except里的代码.'
      'else:       try里代码正常运行时,执行else里的代码.'
      'finally:    不管try里的代码是否出现异常,finally里的代码始终执行')

print('------------第三题------------------')
"""
用户输入一个数值，打印1到这个数值之间所有的偶数、及其偶数个数、及其它们的平均值（如果输入非数值，请让用户重新输入）
"""


# 定义获取平均值函数
def ave(a):
    sum1 = 0
    for i in a:
        sum1 += i
    average = sum1 / len(a)
    return average


# 主函数
def num():
    b = True
    while b:
        try:
            n = int(input('请输入一个数:'))
        except Exception as e:
            print('输入有误,请重新输入!,错误信息:{}'.format(e))
        else:
            b = False
            # print(list(x for x in range(1, n) if x % 2 == 0))
            list1 = []
            for a in range(1, n):
                if a % 2 == 0:
                    list1.append(a)
            av = ave(list1)
            print('偶数集合:{},偶数个数:{},集合平均值:{}'.format(list1, len(list1), av))


num()
