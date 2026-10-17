class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            curr = nums[i]

            for j in range(i + 1, len(nums)):
                next = nums[j]

                if curr + next == target:
                    return [i, j]

