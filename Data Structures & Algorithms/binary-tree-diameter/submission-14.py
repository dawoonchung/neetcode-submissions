# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = 0
        # def dfs(node):
        #     nonlocal diameter

        #     if not node:
        #         return 0

        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     diameter = max(diameter, left + right)

        #     return 1 + max(left, right)
        # dfs(root)
        # return diameter

        if not root:
            return 0
        
        stack = [root]
        tracker = {None: (0, 0)}
        
        while stack:
            curr = stack[-1]

            if curr.left and curr.left not in tracker:
                stack.append(curr.left)
            elif curr.right and curr.right not in tracker:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                
                leftHeight, leftDiameter = tracker[curr.left]
                rightHeight, rightDiameter = tracker[curr.right]

                tracker[curr] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))
        return tracker[root][1]