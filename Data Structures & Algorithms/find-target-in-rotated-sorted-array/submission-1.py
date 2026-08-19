class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1


        while l <= r:

            m = (l+r)//2
            if nums[m] == target: return m

            # LEFT half check (L - M)
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1

            # RIGHT half check (R - M)
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m-1
        
        return -1

# we check == m early
# we check = r or = l later
# we dont do <= with mid as it changes and = m alredy done