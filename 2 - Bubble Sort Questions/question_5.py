def bubble_sort(array):
    length = len(array)
    count = 0
    while True:
        swapCycle = False
        for y in range(0, length - 1):
            if array[y] > array[y + 1]:
                array[y], array[y + 1] = array[y + 1], array[y]
                swapCycle = True
                count += 1     
        if swapCycle == False:
            return array,count
                
numbers = ["wolf", "apple","aapple", "zebra", "banana", "cherry","date"]
numbers,count = bubble_sort(numbers)
print(numbers,count)  # Output: [1, 2, 5, 5, 6, 9]