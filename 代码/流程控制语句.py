#if语句
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
if a + b <= c or a + c <= b or b + c <= a:
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
#match语句
day =input("今天星期几")
match day:
    case "1":
        print("工作")
    case "2":
        print("出差")
    case "3"|"4":
        print("加班")
    case "5":
        print("采购")
    case "6"|"7":
        print("休息")
    case _:
        print("输入错误")

#小案例:简易计算器
num1 = float(input("请输入第一个数字: "))
oper = input("请输入运算符 (+, -, *, /): ")
num2 = float(input("请输入第二个数字: "))
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2}= {num1 * num2}")
    case "/"if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("无效的运算符")
print("---------------------------------")


#while循环
i=0
while(i<10):
    print("hello world")
    i+=1
else:
    print("MAN")

#案例：1-100之间的偶数和
i=1
sum=0
while(i<=100):
    if i%2==0:
        sum+=i
    i+=1
else:
    print("1-100之间的偶数和为：",sum)
print("---------------------------------")

#for循环
msg = "hello-world"
for i in msg:
    print(i)
else:
    print('MAN')

for i in range(1,10):
    print(i)
#案例：1-100之间的奇数和
sum=0
for i in range(1,101,2):
    sum+=i
print("1-100之间的奇数和为：",sum)