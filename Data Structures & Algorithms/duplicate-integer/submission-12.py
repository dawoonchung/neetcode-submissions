class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sentinel = set()
        for num in nums:
            if not num in sentinel:
                sentinel.add(num)
                continue
            return True
        return False