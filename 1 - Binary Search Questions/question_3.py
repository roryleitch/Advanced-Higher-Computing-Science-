StudentNumbers = [1001,1004,1009,1012,1016,1021,1027,1033]   
StudentNames = ["Amir","Beth","Carla","David" "Ella","Faisal","Georgia","Holly"]

item = int(input("Enter the number of the student you want to search for: "))

found = False
startPos = 0
endPos = len(StudentNumbers) - 1

while found == False and startPos <= endPos:
    middle = (startPos+endPos)//2
    if StudentNumbers[middle] == item:
        found = True
    elif StudentNumbers[middle] < item:
        startPos = middle + 1
    else:
        endPos = middle - 1

if found == True:
    print(f"The name of the student with number {item}, is {StudentNames[middle]}")
else:
    print(f"That student number does not exist.")