class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            rem = target - n
            if rem in d: return [d[rem], i]
            d[n] = i
  