def bubble_sort(array):
    length = len(array)
    count = 0
    print(array)
    while True:
        swapCycle = False
        for y in range(0, length - 1):
            if array[y] > array[y + 1]:
                array[y], array[y + 1] = array[y + 1], array[y]
                print(array)
                swapCycle = True
                count += 1     
        if swapCycle == False:
            return array,count
                
numbers = [5, 2, 9, 1, 5, 6]
numbers,count = bubble_sort(numbers)
print(numbers,count)  # Output: [1, 2, 5, 5, 6, 9]