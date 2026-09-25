# gas[i]: how much gas we can get
# cost[i]: how much gas we need to go next pos 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if we have more distance than we have required oil
        if sum(gas) < sum(cost):
            return -1
        
        # be greedy, we asume 0 index is where  can we start
        start = 0  
        total = 0  # total gas intank from idx-start

        for i in range(len(gas)):
            # do we have enough gas
            total += (gas[i] - cost[i])

            # if we dont, rethink 'start'
            if total < 0:
                start = i + 1
                total = 0
            
        return start
