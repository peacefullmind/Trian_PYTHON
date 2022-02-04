class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        str1=list(str(number))
        str1.reverse()
        str1="".join(str1)
        str1=int(str1)


        return str1

s=Solution()
res=s.reverseInteger(900)
print(res)