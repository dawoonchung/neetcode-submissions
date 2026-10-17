class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr: List[int] = []
        for num in nums:
            if num in curr:
                return True
            curr.append(num)
        return False