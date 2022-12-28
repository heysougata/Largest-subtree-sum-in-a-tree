# Largest subtree sum in a tree
from typing import Optional
from collections import deque

#definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution : 
    def findLargestSubtreeSum(self, root : Optional['Node']) -> int:
        res = -1e+7
        def recur(root):
            nonlocal res
            if root:
                lef_sum = recur(root.left)
                righ_sum = recur(root.right)
                cur = root.data + lef_sum + righ_sum
                res = max(res, cur)
                return cur
            return 0
        recur(root)
        return res
        # code here
        

