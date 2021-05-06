
# 1.1Fibonacci数列题
n = int(input("输入包含一个整数："))
# n = 10
fib = [1 for i in range(n+1)]
k = 3
while k <= n:
    fib[k] = (fib[k-1] +fib[k-2]) % 10007
    k += 1
print("第", n, "的数列除以10007余数为", fib[n])

# #1.2圆的面积
import math
r = int(input("输入圆的半径："))
s = math.pi * r * r
print("{:.7f}".format(s))

# 1.3序列求和
n = int(input("输入一个整数: "))
s = n * (n + 1) / 2 # 等差数列公式
print("序列和为: %d" %s)

# 1.4 A+B问题
a, b = map(int, input("输入两个整数").split())
print(a+b)


# 2.1数列排序 (即输入的第二行整数以空格间隔)
n = int(input("输入数列长度: "))
num = list(map(int, input("输入待排序整数，整数的绝对值小于10000：").split()))
num.sort()  #None是不可迭代的    或者sorted(num)
print(" ".join("{:d}".format(i) for i in num ))

# 方法二:
num = input("输入待排序整数，整数的绝对值小于10000：").split()
num = sorted(num)    #list类型
print(" ".join(num[:n]))
# 2.1 进制转化
#十六进制转八进制
n = int(input("输入需转换的行数: "))
for i in range(1,n+1):
    print("第", i, "行")
    m = input("输入十六进制正整数： ")
    ans = format(int(m, 16), 'o')
    print(ans)
#十六进制转二进制
ans = format(int(m, 16), 'b')

#十六进制转十进制
print(int(input("输入十六进制正整数: "), 16))

#十进制转十六进制
print(format(int(input("输入十进制正整数: ")), 'X'))

# 2.3 特殊回文数
n = int(input("输入需得到回文数之和的整数: "))
#先判断是否为回文数  （方法一：特点按顺序：从10000,10001,10002,...,999999）
for i in range(10000, 1000000):
    num_pd = str(i)  #回文数
    if num_pd == num_pd[::-1]:
        sum_pd = 0
        #在单独求各个 位数字之和
        for j in num_pd:
            sum_pd += int(j)
        if sum_pd == n:
            print(num_pd)

# ***** 绝绝子方法 *****
n = int(input())
for i in range(10000, 1000000):
    num_pd = str(i) #可能出现的回文数
#符合正序与倒序相等，同时将字符串以 + 分割并以eval()转化为表达式进行求值
    if num_pd == num_pd[::-1] and eval('+'.join(num_pd)) == n:
    #eval:***转化为有效的表达式 或 complie函数的代码对象（其可以创建函数compile(表达式,'','编译代码')）
        print(i)

# (方法二：按照回文数顺序遍历，如：10001,20002,...,999999)
my_list = []
for i in range(100, 1000):
    num_pd_half = str(i) #回文数的前半部分，复制，对称处理 ，从而减少运算
    #回文数是五位数
    if sum(map(int, num_pd_half + num_pd_half[:2][::-1])) == n:  #三位数 + 三位数的前2位数 倒序
        my_list.append(num_pd_half + num_pd_half[::-1])
    #回文数是六位数
    if sum(map(int, num_pd_half + num_pd_half[::-1])) == n:    #三位数 + 三位数的倒序
        my_list.append(num_pd_half + num_pd_half[::-1])

for i in sorted(map(int, my_list)):
    print(i)



# #输出四位数的回文
# import time
# start = time.time()
num_list = []
for i in range(10, 101):  #两位数
    num_list.append(str(i) + str(i)[::-1])  #两位数 + 两位数的倒序
for l in map(int, num_list):
    print(l)

# print(time.time()-start)

# 2.4 水仙花数
for i in range(100, 1000):
    # 个位十位百位数 各个立方，相加之和
    num_sum = int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3
    if num_sum == i:
        print(i)

# 2.5 杨辉三角
n = int(input("输入行数："))

old_line = [1]    #打印第一列 1
print(' '.join(str(i) for i in old_line))
for i in range(1, n):   #打印第一列之后，第二列开始(从[1,1]开始)
    new_line = []       #创建新列表
    for j in range(len(old_line)-1):  #打印第二列之后，第三列开始（从[1,2,1]开始）
        new_line.append(old_line[j] + old_line[j+1])  #添加的数据，(从[1]+[1]: 1+1 = 2开始)
    # 添加新列表中的参数   *表示：将列表解开成多个独立的参数
    new_line = [1, *new_line, 1]

    print(' '.join(str(i) for i in new_line))


# 2.6 查找整数， 输入含有n个整数的数列a，搜索整数m在a数列中的数量
n = int(input("输入数列中整数的数量: "))
a = input("输入数列: ").split()
m = input("输入待查的整数: ")
num = 0
##方法缺n值
for j in range(n):
    if a[j] == str(m):  #按顺序搜索数列中的整数
        num += 1
if num == 0:
    print(-1)
else:
    print("出现的次数为： ", num)

# 2.7 数列特征
n = int(input("输入整数的个数: "))
m = input("输入数列: ").split()
# max(),min()函数，对于列表取最大/小的数字,
# 对于字符串取最大/小的字母（如："1，2，3" --> 逗号最小）， 其他的与字符串同理

if n == len(m):
    print("最大数值为：", max(m))  #求最大数值
    print("最小数值为：", min(m))  #求最小数值
    print("最小值为：", eval("+".join(m))) #求和

# 2.8 字母图形 输出n行m列的字母图形
try:
    n, m = map(int, input("请输入需输出的行数 、列数: ").split())
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = letter[:m]    #初始为m列的第一行列表
    for i in range(1, n+1):
        print(output)
        output = letter[i] + output[:-1]  #重新赋值第二列列表之后的数列
        #为字母表第n个为字母列的首字母 + 前一行除最后一位数的字母列
except:
    pass

# 2.9 字串01

for i in range(32):
    print("{:0>5}".format(format(i, 'b')))

#数字0，向左边填充，宽度为5,以二进制格式输出

# 2.10 判断是否为闰年
n = int(input("输入年份: "))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("yes")
else:
    print("no")