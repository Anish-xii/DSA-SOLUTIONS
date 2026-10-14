class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return mid

            # sorted (L - M)
            if nums[l] <= nums[mid]:
                # target in the half
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                # target not avalable (-1) -> opt out L-M
                else:
                    l = mid+1
            # sorted (M - R)
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        
        return -1

# we use <= where we have alredy checked target