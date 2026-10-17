class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sentinel = list()
        for num in nums:
            if not num in sentinel:
                sentinel.append(num)
                continue
            return True
        return False