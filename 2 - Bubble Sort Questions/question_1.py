debug = False # Set to True to enable debug prints, False to disable
def bubble_sort(array):
    length = len(array)
    for x in range(length):
        if debug == True: print(f"Pass {x + 1}:")
        for y in range(0, length - x - 1):
            if array[y] > array[y + 1]:
                if debug == True: temp = list(array)  # Temporary variable to hold the array state
                array[y], array[y + 1] = array[y + 1], array[y] # Swap if the element found is greater than the next element
                if debug == True: print(f"{temp} {array[y]} is being swapped with {array[y+1]} {array}") # Print the array after each swap for debugging

numbers = [5, 2, 9, 1, 5, 6]
bubble_sort(numbers)
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]