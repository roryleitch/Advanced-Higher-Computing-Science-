def bubble_sort(array):
    length = len(array)
    count = 0
    while True:
        swapCycle = False
        for y in range(0, length - 1):
            if array[y][1] > array[y + 1][1]:
                array[y][1], array[y + 1][1] = array[y + 1][1], array[y][1]
                swapCycle = True
                count += 1     
        if swapCycle == False:
            return array,count
                
game = [["Anna", 72], ["Ben", 65], ["Cara", 80]]

sortedArray,count = bubble_sort(game)
print(sortedArray,count)  # Output: [['Ben', 65], ['Anna', 72], ['Cara', 80]]