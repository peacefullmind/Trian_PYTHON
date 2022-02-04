from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        N=len(prices)
        my_sum=0
        for n in range(N):
            if n==0:
                res=1
                pre=res
                my_sum=my_sum+res
            elif prices[n]-prices[n-1]==-1:
                res=pre+1
                pre=res
                my_sum=my_sum+res
            else:
                res=1
                pre=res
                my_sum=my_sum+res
        return my_sum

s=Solution()
prices = [3,2,1,4]
my_res=s.getDescentPeriods(prices)
print(my_res)









