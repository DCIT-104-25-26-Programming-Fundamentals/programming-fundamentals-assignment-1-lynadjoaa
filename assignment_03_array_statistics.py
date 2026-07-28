def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)

def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


n = int(input("How many numbers? "))

if n <= 0:
    print("Error: N must be a positive integer.")
else:
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    print("\nResults:")
    print(f"Sum: {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {find_maximum(numbers)}")
    print(f"Minimum: {find_minimum(numbers)}")
