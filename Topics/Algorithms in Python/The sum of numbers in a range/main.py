def range_sum(numbers, start, end):
    total = 0
    for n in numbers:
        if start <= n <= end:
            total = total + n
    return total


input_numbers = [int(num) for num in input().split()]
a, b = [int(i) for i in input().split()]
print(range_sum(input_numbers, a, b))
