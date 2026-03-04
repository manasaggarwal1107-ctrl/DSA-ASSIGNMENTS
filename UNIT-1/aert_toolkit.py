class StackADT:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

def factorial(n):
    
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

fib_calls_naive = 0

def fib_naive(n):
    global fib_calls_naive
    fib_calls_naive += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

fib_memo = {}
fib_calls_memo = 0

def fib_memoized(n):
    global fib_calls_memo, fib_memo
    fib_calls_memo += 1

    if n in fib_memo:
        return fib_memo[n]
    
    if n <= 1:
        fib_memo[n] = n
        return n
    
    fib_memo[n] = fib_memoized(n-1) + fib_memoized(n-2)
    return fib_memo[n]

def hanoi(n, source, auxiliary, destination):

    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    hanoi(n-1, source, destination, auxiliary)

    print(f"Move disk {n} from {source} to {destination}")

    hanoi(n-1, auxiliary, source, destination)

def binary_search(arr, key, low, high):

    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    
    else:
        return binary_search(arr, key, mid + 1, high)


if __name__ == "__main__":
    print("=== Factorial Tests ===")
    print("factorial(0):", factorial(0))
    print("factorial(1):", factorial(1))
    print("factorial(5):", factorial(5))
    print("factorial(10):", factorial(10))

    print("\n=== Fibonacci Tests Naive ===")

    for n in [5, 10, 20, 30]:

        fib_calls_naive = 0    
        res = fib_naive(n)
        print(f"fib_naive({n}): {res}, calls: {fib_calls_naive}")

    print("\n=== Fibonacci Tests Memoized ===")

    for n in [5, 10, 20, 30]:

        fib_memo = {}            
        fib_calls_memo = 0       
        res = fib_memoized(n)
        print(f"fib_memo({n}): {res}, calls: {fib_calls_memo}")

    print("\n=== Tower of Hanoi N=3 ===")
    hanoi(3, 'A', 'B', 'C')

    print("\n=== Binary Search Tests ===")
    
    
    arr = [1, 3, 5, 7, 9, 11, 13]

    print("arr =", arr)
    print("search 7:", binary_search(arr, 7, 0, len(arr)-1))
    print("search 1:", binary_search(arr, 1, 0, len(arr)-1))
    print("search 13:", binary_search(arr, 13, 0, len(arr)-1))
    print("search 2:", binary_search(arr, 2, 0, len(arr)-1))
    print("empty arr:", binary_search([], 5, 0, -1))

    print("\n=== StackADT Demo - Hanoi Trace ===")
    stack = StackADT()

    def hanoi_trace(n, src, aux, dst):
       
        if n == 1:
            stack.push(f"Move disk 1 from {src} to {dst}")
            return
        
        hanoi_trace(n-1, src, dst, aux)
       
        stack.push(f"Move disk {n} from {src} to {dst}")
        hanoi_trace(n-1, aux, src, dst)

    hanoi_trace(3, 'A', 'B', 'C')

    print("Hanoi moves in stack (popping):")

    while not stack.is_empty():

        print(stack.pop())

    print("Stack size after:", stack.size())
