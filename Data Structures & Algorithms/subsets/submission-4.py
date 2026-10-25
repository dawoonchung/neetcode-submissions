class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            for subset in res.copy():
                res += [subset + [num]]

        return res