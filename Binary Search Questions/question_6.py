gamescores = [
              ["DanTDM","LazarBeam","Muselk","Ninja","TSM_Myth"],   #Names 0
              [9855,3973,7084,8741,7118],                           #Game  1
              [7371,5081,5936,3200,7928],                           #Game  2
              [6557,6990,7195,6247,2525],                           #Game  3
              [2340,4312,8587,6713,7405],                           #Game  4
              [7480,3763,4839,7811,4757]                            #Game  5
              ]   

item = "DanTDM"
found = False
startPos = 0
endPos = len(gamescores[0]) - 1

while found == False and startPos <= endPos:
    middle = (startPos+endPos)//2
    if gamescores[0][middle] == item:
        found = True
    elif gamescores[0][middle] < item:
        startPos = middle + 1
    else:
        endPos = middle - 1
        
playerScores = str(gamescores[1][middle])
for x in range(2,6):
    playerScores = f"{playerScores}, {str(gamescores[x][middle])}"

if found == True:
    print(f"The player {item}'s scores are {playerScores}.")
else:
    print(f"That player does not exist.")