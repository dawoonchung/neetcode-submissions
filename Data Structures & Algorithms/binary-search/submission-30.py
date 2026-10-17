class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0

        num_map = dict()
        for i, v in enumerate(nums):
            num_map[v] = i

        first = nums[:len(nums)//2]
        second = nums[len(nums)//2:]

        while first and second:
            if len(first) == 1 and first[0] == target:
                return num_map[first[0]]

            if len(second) == 1 and second[0] == target:
                return num_map[second[0]]
            
            if target <= first[-1]:
                new_first = first[:len(first)//2]
                new_second = first[len(first)//2:]
                first = new_first
                second = new_second
            else:
                new_first = second[:len(second)//2]
                new_second = second[len(second)//2:]
                first = new_first
                second = new_second

        return -1
