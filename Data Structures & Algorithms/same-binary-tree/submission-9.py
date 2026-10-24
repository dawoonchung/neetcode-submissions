# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False

        def flatten(stack):
            order = []
            while stack:
                curr = stack.pop()
                order.append(curr)

                if curr:
                    stack.append(curr.left)
                    stack.append(curr.right)
            
            return order

        flattened_p = flatten([p])
        flattened_q = flatten([q])

        if len(flattened_p) != len(flattened_q):
            return False
        
        for i in range(len(flattened_p)):
            if not flattened_p[i] and flattened_q[i]:
                return False
            if not flattened_q[i] and flattened_p[i]:
                return False
            if flattened_p[i] and flattened_q[i]:
                if flattened_p[i].val != flattened_q[i].val:
                    return False

        return True