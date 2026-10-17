class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sentinel = dict()
        for num in nums:
            if not num in sentinel:
                sentinel[num] = 0
                continue
            return True
        return False