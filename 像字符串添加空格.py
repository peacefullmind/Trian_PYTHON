from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        #字符串截取
        istart=0
        i_s = istart
        my_list = []
        for i in range(len(spaces)):
            sp=spaces[i]
            i_end=sp
            temp=s[i_s:i_end]
            i_s=i_end
            my_list.append(temp)
        i_s=spaces[-1]
        N=len(s)
        temp=s[i_s:N]
        my_list.append(temp)

        # 字符串拼接
        newStr = " ".join(my_list)
        return newStr


s = "spacing"
spaces = [0,1,2,3,4,5,6]
ss=Solution()
re=ss.addSpaces(s,spaces)
print(re)
