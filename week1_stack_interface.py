#python3
import sys

class MaxVal:
    def __init__(self, num, max_val, last_max):
        self.num = num
        self.max_val = max_val
        self.last_max = last_max

class StackWithMax():
    
    def __init__(self):
        self._stack = [] 
        self._max  = 0
        self._last_max = None

    def Push(self, a):
        if self._max < a:
            self._last_max = self._max
            self._max = a
        else:
            self._last_max = self._max
        
        self._stack.append(MaxVal(a, self._max, self._last_max))

    def Pop(self):
        assert(len(self._stack))
        pop = self._stack.pop()
        
        if self._max != pop.last_max :
            self._max = pop.last_max
        

    def Max(self):
        assert(len(self._stack))
        return self._max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
