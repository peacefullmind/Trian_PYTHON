class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    # 你正在和朋友玩一个游戏：桌子上有一堆石头，每一次你们都会从中拿出1到3个石头。拿走最后一个石头的人赢得游戏。游戏开始时，你是先手。
    #
    # 假设两个人都绝对理性，都会做出最优决策。给定石头的数量，判断你是否会赢得比赛。
    #
    # 举例：有四个石头，那么你永远不会赢得游戏。不管拿几个，最后一个石头一定会被你的朋友拿走。
    def canWinBash(self, n):
        # Write your code here
        if(n==1):
            return False
        if(n==2):
            return True
        if(n==3):
            return True
        if(n==4):
            return False
        pre_pre_pre=1
        pre_pre=1
        pre=0
        for i in range (5,n+1):
            if pre==0 or pre_pre==0 or pre_pre_pre==0:
                temp=1
            else:
                temp=0
            pre_pre_pre=pre_pre
            pre_pre=pre
            pre=temp

        return temp==1

        # 拿一个，拿两个，或者拿三个，只要有一种情况，能将对方置于 False的境地，就说明我应该如此做，从而赢下比赛
        # if self.canWinBash(n-1)==False or self.canWinBash(n-2)==False or self.canWinBash(n-3)==False:
        #     return True
        # else:
        #     return False




n=40000000
s=Solution()
res=s.canWinBash(n)
print(res)

