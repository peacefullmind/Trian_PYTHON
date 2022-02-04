# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 18:18
# @Author  : taoji
# @Email   : tao13131265081@163.com
# @File    : 打折购买糖果的最小开销.py
# @Software: PyCharm
from typing import List


def minimumCost(cost: List[int]) -> int:
    # 升序排列
    cost.sort()
    N=len(cost)
    if N<=2:
        return sum(cost)
    elif N==3:
        return sum(cost[N-2:N])
    else:
        list_mx=cost[N-3:N]
        list_pre=cost[0:N-3]
        return  minimumCost(list_pre)+minimumCost(list_mx)




cost = [5,5]
res=minimumCost(cost)


print(res)