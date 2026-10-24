# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        is_balanced = True
        def get_height(node):
            nonlocal is_balanced
            if not node:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)
            if is_balanced:
                is_balanced = (left_height - right_height) ** 2 <= 1

            return max(left_height, right_height) + 1

        get_height(root)

        return is_balanced