#1.认识字面量
print(100)#整数int
print(3.14)#浮点数
print(False)#布尔值首字母大写
print(None)#空值首字母大写
print("Hello ##")#字符串要引号


print(True+999)#布尔本质是整型
print(False-100)
print("---------------------------------------")


#2.变量

#初值
num = 1114.1
print(num)

#变化后
num = num + 1
print(num)

#改变数据类型
num = 'ok'
print(num)

#小练习
clas = 20.7
for month in (0, 1):
    clas = clas + 50
    print("未来第",month + 1,"个月的播放量：",clas)
print("---------------------------------------")

#3.标识符
true = True
age = 1#见名知意
my_name = "sfcedv"#多个单词用_连接

print("交换一")
a = 10
b = 20
print("a =",a)
print("b =",b)
c = a
a = b
b = c
print("a =",a)
print("b =",b)

print("交换二")
a = 100
b = 200
c = 300
print("a =",a)
print("b =",b)
print("c =",c)
d = a
a = b
b = c
c = d
print("a =",a)
print("b =",b)
print("c =",c)
print("---------------------------------------")

#4.数据类型
print(type("python"))
print(type(10086))
print(type(3.14))
print(type(True))
print(type(None))
print(type(a))#查看a这个变量所存储的数据的数据类型（a = 200）

print(isinstance("python",int))
print(isinstance(True,bool))
print("---------------------------------------")

#5.字符串
s1 = "\tHello\n\t你好 "
s2 = 'It\'s python'
s3 = """
hello
加油
哈哈
"""
print(s1)
print(s2,s3)

#字符串拼接
s1 = "一闪一闪""亮晶晶"
s2 = "一闪一闪"+"林俊杰"
print(s1)
print(s2)
print("我说：" + s1 + "，" + s2)

#小样例
name = "sb"
age = 20
pro = "网络空间安全"
hobby = "睡觉"
print("大家好，我是"+name+"，今年"+str(age)+"岁，学习的专业是"+pro+"，爱好"+hobby)

#字符串格式化
print("大家好，我是%s，今年%s岁，学习的专业是%s，爱好%s"%(name,age,pro,hobby))
print(f"大家好，我是{name}，今年{age}岁，学习的专业是{pro}，爱好{hobby}")#推荐
print("---------------------------------------")

#6.输入和输出
name = input("请输入你的名字：")
print(f"欢迎您，{name}")
age = input("请输入你的年龄：")
print(f"{name}今年{age}岁了")

#小案例
total = 10000
#输入密码
password = input('请输入密码：')
print(f"密码正确：{password}")
#输入取款金额
num = input(f"输入取款金额:")
#计算余额
#print(f"余额为：{total - int(num)}")
print("---------------------------------------")
