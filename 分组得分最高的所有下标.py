from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        N = len(nums)
        my_score_max = -1
        i_max=0
        keep_i = []
        for i in range(N + 1):
            nums_left = nums[0:i]
            nums_right = nums[i:N]
            N_left = len(nums_left)
            my_score = N_left - sum(nums_left) + sum(nums_right)
            if (my_score > my_score_max):
                my_score_max = my_score
                i_max=i
                keep_i=[]
                keep_i.append(i_max)
            elif(my_score==my_score_max):
                keep_i.append(i)
            else:pass

        return keep_i

if __name__=='__main__':
    s=Solution()
    res=s.maxScoreIndices(nums)
    print(res)


