class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxLength = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxLength:
            self.stack.append(x)
        
    def pop(self) -> int:
        if len(self.stack) >0:
            return self.stack.pop()
        return -1
    
    def increment(self, k: int, val: int) -> None:
        n = min(k,len(self.stack))
        for i in range(n):
            self.stack[i] += val