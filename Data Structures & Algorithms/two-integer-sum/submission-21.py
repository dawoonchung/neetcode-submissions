class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         next = nums[j]
        #         if curr + next == target:
        #             return [i, j]

        sorted_nums = sorted(nums)

        i = 0
        j = len(sorted_nums) - 1

        while True:
            a = sorted_nums[i]
            b = sorted_nums[j]
            sum = a + b
            if sum == target:
                index_a = nums.index(a)
                index_b = nums.index(b, index_a + 1 if a == b else 0)

                return sorted([index_a, index_b])
                
            if sum > target:
                j -= 1
            
            if sum < target:
                i += 1
                