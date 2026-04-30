class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} 
        
        for i, num in enumerate(numbers):
            complement = target - num
            
            if complement in seen:
                # The problem asks for 1-based indexing, so we add 1
                return [seen[complement] + 1, i + 1]
            
            # Store the current number and its 0-based index
            seen[num] = i