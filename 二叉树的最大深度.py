
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #深度优先遍历，树高为root的左子树和右子树中最高的高度加1
        if root==None:
            return 0
        left_high=self.maxDepth(root.left)
        right_high=self.maxDepth(root.right)
        return max(left_high,right_high)+1



    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        # 广度优先算法
        #使用队列实现BFS，循环时把当前层的节点出队，下一层节点入队
        # 为了记录层数，要嵌套一个弹出树当前层的所有节点的循环，内部循环结束后depth + 1
        # 当队列为空时，已遍历完树的所有节点，循环结束，返回depth
        # 代码
        if not root:
            return 0
        queue = deque([root])
        depth=0
        while queue:
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
        return depth




tn1=TreeNode(15)
tn2=TreeNode(7)
tn3=TreeNode(20,tn1,tn2)
tn4=TreeNode(9)
tn5=TreeNode(3,tn4,tn3)

s=Solution()
res2=s.maxDepth2(tn5)
print(res2)
