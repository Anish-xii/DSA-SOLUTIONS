class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        if len(position) == 1: return 1
        p_speed = {}
        for i in range(len(position)):
            p_speed[position[i]] = speed[i]
        position.sort(reverse=True)  
        stk = []

        for p in position:
            stk.append((target-p)/p_speed[p]) # time to target
            # if last added was >= new, no need of new
            if len(stk)>=2 and stk[-2] >= stk[-1]:
                stk.pop()

        return len(stk) 