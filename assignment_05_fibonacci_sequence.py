def print_fibonacci(n):
    if n <= 0:
        print("N must be a positive integer.")
        return
    
    a = 0
    b = 1
    sequence = []
    
    for i in range(n):
        sequence.append(str(a))
        a, b = b, a + b
    
    print("Fibonacci sequence:", " ".join(sequence))

def is_fibonacci(num):
    if num < 0:
        return False
    
    a = 0
    b = 1
    
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    
    return False


print("PART A: PRINT FIRST N TERMS")
n = int(input("How many terms? "))
print_fibonacci(n)

print("\n
