class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}

        for i in range(len(nums)):
            exces = target - nums[i]
            if exces in remainder:
                return [remainder[exces], i]
            remainder[nums[i]] = i
                