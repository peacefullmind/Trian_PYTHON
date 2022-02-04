# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 23:12
# @Author  : taoji
# @Email   : tao13131265081@163.com
# @File    : 斐波拉数列.py
# @Software: PyCharm

#=============================最基本的，；暴力递归======================================================
# 最基本的，；暴力递归
def f(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return f(n-1)+f(n-2)

res=f(10)
print(res)


#===========================带备忘录的========================================================
# 带备忘录的，这种带备忘录的解法就是我们经常说的“剪枝”操作，以下把一颗非常冗余的树修剪的很干净，或者说就是减少了重叠子问题
def back(memory,n):
    if(n==1):
        memory[1]=1
        return 1
    if(n==2):
        memory[2] = 1
        return 1
    if(memory[n]!=0):
        return memory[n]
    res=back(memory,n-1)+back(memory,n-2)
    memory[n]=res
    return res

def fib(n):
    if(n==0):
        return 0
    memory=[0]*(n+1)
    return back(memory,n)

res=fib(10)
print(res)
#===========================自底向上========================================================
# 带备忘录的,自底向上
def fib_low(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    if(n==2):
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return  dp[n]
n=10
res=fib_low(n)
print(res)
#==============================================迭代===================================
#迭代也是自底向上,当前状态仅仅和前两个状态有关，而前面无关，所以我们可以优化空间，不采用数组，直接两个变量，交替保存。
def fib_d(n):
    if(n==1):
        return 1
    if(n==2):
        return 1
    pre_pre=1
    pre=1
    for i in range(3,n+1):
        temp=pre+pre_pre
        pre_pre=pre
        pre=temp
    return temp
n=10
res=fib_d(n)
print(res)



