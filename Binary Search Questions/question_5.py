ExamNumbers = [11,22,33,44,55,66,77,88,99]   
ExamResults = ["Pass","Fail","Pass","Pass","Fail","Pass","Pass","Fail","Pass"]

item = 66
found = False
startPos = 0
endPos = len(ExamNumbers) - 1

while found == False and startPos <= endPos:
    middle = (startPos+endPos)//2
    if ExamNumbers[middle] == item:
        found = True
    elif ExamNumbers[middle] < item:
        startPos = middle + 1
    else:
        endPos = middle - 1

if found == True:
    print(f"The result of the exam with number {item}, is a {ExamResults[middle]}")
else:
    print(f"That exam number does not exist.")