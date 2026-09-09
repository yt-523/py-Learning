score = int(input('请输入你的分数：'))
if score > 680:
    print("欢迎来读书")
print("---------------------------------")

"""
小案例
账号密码
"""
user = int(input('请输入你的账号：'))
password = int(input('请输入你的密码：'))
if user == 1888888888 and password ==666888:
    print('登陆成功')
elif user != 1888888888 and password ==666888:
    print('账号错误')
elif user == 1888888888 and password != 666888:
    print('密码错误')
else:
    print('账号密码错误')
print("---------------------------------")

"""
小案例
整数判断
"""
n = int(input('请输入一个整数：'))
if n > 0:
    print('你输入的是正数')
elif n < 0:
    print('你输入的是负数')
else:
    print('你输入的是零')
print("---------------------------------")


"""
小案例
三角形判断
"""
a = int(input('请输入三角形的第一条边：'))
b = int(input('请输入三角形的第二条边：'))
c = int(input('请输入三角形的第三条边：'))
if a + b <= c or a + c <= b and b + c <= a:
    print('不能构成三角形')
elif a == b and b == c:
    print('等边三角形')
elif a == b or a == c or b == c:
    print('等腰三角形')
else:
    print('普通三角形')

#或者
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print('等边三角形')
    elif a == b or a == c or b == c:
        print('等腰三角形')
    else:
        print('普通三角形')
else:
    print('不能构成三角形')

print("---------------------------------")

