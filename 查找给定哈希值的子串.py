# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 17:43
# @Author  : taoji
# @Email   : tao13131265081@163.com
# @File    : 查找给定哈希值的子串.py
# @Software: PyCharm


def TurnInt(s):
    return  ord(s)-ord('a')+1

def hash(s,p,m):
    N=len(s)
    my_sum=0
    for i in range(N):
        temp=TurnInt(s[i])*pow(p,i)
        my_sum=my_sum+temp
    res=my_sum%m

    return res

def findSub(s,k):
    N=len(s)
    my_list=[]
    for i in range(N):
        if i+k>N:
            break
        sub_string=s[i:i+k]
        my_list.append(sub_string)
    return my_list

def subStrHash(s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    mylists=findSub(s,k)
    for sub_string in mylists:
        my_hash=hash(sub_string,power,modulo)
        if my_hash==hashValue:
            return  sub_string



s = "fbxzaad"
power = 31
modulo = 100
k = 3
hashValue = 32
res=subStrHash(s,power,modulo,k,hashValue)
print(res)



