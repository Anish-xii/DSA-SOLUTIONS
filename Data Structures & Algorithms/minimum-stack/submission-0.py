class MinStack:

    def __init__(self):
        self.stack = []
        self.minstk = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstk:
            self.minstk.append(val)
        elif val < self.minstk[-1]:
            self.minstk.append(val)
        else: self.minstk.append(self.minstk[-1])    
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstk.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstk[-1]
        
