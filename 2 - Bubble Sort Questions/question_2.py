def bubble_sort(array):
    length = len(array)
    for x in range(length):
        for y in range(0, length - x - 1):
            if array[y] < array[y + 1]:
                array[y], array[y + 1] = array[y + 1], array[y]
                
numbers = [5, 2, 9, 1, 5, 6]
bubble_sort(numbers)
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]