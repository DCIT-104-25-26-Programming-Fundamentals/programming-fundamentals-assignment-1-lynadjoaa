def print_single_table(num):
    if num <= 0:
        print("Error: Number must be a positive integer.")
        return
    
    print(f"Multiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

def print_tables_to_n(n):
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
    
    for num in range(1, n + 1):
        print(f"Multiplication Table for {num}:")
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
        if num < n:
            print("--------------------")


print("PART A: SINGLE TABLE")
num = int(input("Enter a number: "))
print_single_table(num)

print("\nPART B: TABLES FROM 1 TO N")
n = int(input("Enter N: "))
print_tables_to_n(n)
