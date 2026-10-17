class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sentinel = set()
        for num in nums:
            if num in sentinel:
                return True
            sentinel.add(num)
        return False