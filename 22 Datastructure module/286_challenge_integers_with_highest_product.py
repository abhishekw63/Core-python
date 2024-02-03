

'''
This approach has a time complexity of O(n) as it only requires a single traversal of the array.'''
'''
import array

def max_product(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"

    x = y = float('-inf')  # Initialize to negative infinity
    min1 = min2 = float('inf')  # Initialize to positive infinity

    for num in arr:
        if num > x:
            y = x
            x = num
        elif num > y:
            y = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    if x * y > min1 * min2:
        return x, y
    else:
        return min1, min2

a1 = array.array('i', [4, 2, 5, 7, 8, 9, 2])
a2 = array.array('i', [4, 2, 5, 7, -8, 9, 2])
a3 = array.array('i', [-1, 4, 6, -2, -3, 5, 6, -9, 11, -12])

print(max_product(a1))
print(max_product(a2))
print(max_product(a3))

'''