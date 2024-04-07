import math

def last_indexof_max(numbers):
    
    if len(numbers) <= 0:
        return -1
    
    max_num = max(numbers)
    
    return max([i for i, x in enumerate(numbers) if x == max_num])
