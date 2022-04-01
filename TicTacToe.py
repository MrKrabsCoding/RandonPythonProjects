# Tick Tack Toe

import random
import os



global board


def CreateBoard():
    NewBoard = {}
    for i in range(9):
        NewBoard[i] = "-"
    return NewBoard



def DisplayBoard():
    displayString = ""
    for index in range(3):
        for i in range(3):
            i += index * 3
            displayString += board[i] 
            if not (i  - index * 3) % 2 == 0 or (i  - index * 3) == 0:
                displayString += "|"
        displayString += "\n"
    print("Board:")
    print(displayString)

def ClearOutput():
    for i in range(5):
        print("\n")

def GetCurrentSlotsOpen():
    Slots = {}
    for i in range(len(board)):
        #print(i)
        #print(board)
        #print(len(board))
        if board[i] != "-":
            continue
        Slots[i + 1] = True
    return Slots

def ChoosePlayerLetter():
    pass

def ConvertResponse(Convert):
    NewConvert = Convert
    try:
        NewConvert = int(NewConvert)
        pass
    except Exception as inst:
        print(Exception)
        NewConvert = False

    return NewConvert
         

def GetPlayerInput(type):
    OpenSlots = GetCurrentSlotsOpen()
    while True:
        response = input("Choose a Slot")
        NewResponse = ConvertResponse(response)

        if NewResponse == False:
            print("\"" + response + "\" is not a valid response. Please try again.")
            continue
        else:
            if NewResponse > 9:
                print("That value is higher than the acceptable range. Please try again.")
                continue
            elif NewResponse < 1:
                print("That value is lower than the acceptable range. Please try again.")
                continue
            elif not NewResponse in OpenSlots.keys():
                print("That slot has already been taken. Please try again.") 
                continue
            board[NewResponse - 1] = type
            return response

# Deprecated
def GetPlayerInputs(type):
    OpenSlots = GetCurrentSlotsOpen()
    response = input("Choose a Slot")

    NewResponse = ConvertResponse(response)
    if NewResponse == False:
        print("\"" + response + "\" is not a valid response. Please try again.")
        return GetPlayerInput()
    else:
        if NewResponse > 9 :
            print("That value is higher than the acceptable range. Please try again.")
            return GetPlayerInput()
        
        elif NewResponse < 1 :
            print("That value is lower than the acceptable range. Please try again.")
            return GetPlayerInput()
        
        elif not NewResponse in OpenSlots.keys():
            print("That slot has already been taken. Please try again.")
            return GetPlayerInput(type)

        print("Valid Response")
        board[NewResponse - 1] = type
        return response

def CheckIfEnd():
    if board[0] == board[1] == board[2]  != "-": # Top Across
        return board[0]
    elif board[3] == board[4] == board[5] != "-": # Middle Across
        return board[3]
    elif board[6] == board[7] == board[8] != "-": # Bottom Across
        return board[6]
    elif board[0] == board[3] == board[6]!= "-": # Left Down
        return board[0]
    elif board[1] == board[4] == board[7] != "-": # Middle Down
        return board[1]
    elif board[2] == board[5] == board[8] != "-": # Right Down
        return board[2]
    elif board[0] == board[4] == board[8] != "-": # Diagnol
        return board[0]
    elif board[2] == board[4] == board[6] != "-": # Diagnol
        return board[2]
    elif not "-" in board.values(): # Tie
        return False
    else: # No Win
        return " " 

def GetLengthOfKeys(key):
    count = 0
    for i in key:
        count += 1
    return count

def GetValueInArray(array, index):
    RealIndex = 0
    for value in array:
        if index == RealIndex:
            return value
        RealIndex += 1
        

def DoAiMove(type):
    SlotsOpen = GetCurrentSlotsOpen()
    SlotsArray = SlotsOpen.keys()
    Length = GetLengthOfKeys(SlotsArray) - 1
    
    Aimove = GetValueInArray(SlotsArray,random.randint(0,Length))
    print(Aimove)
    board[Aimove - 1] = type
    pass


def StartXGame():
    global board
    board = CreateBoard()
    ClearOutput()
    DisplayBoard()
    while True:
        GetPlayerInput("X")
        DisplayBoard()
        win1 = CheckIfEnd()
        if win1 != " " and win1 != False:
            print(win1 + " has won!")
            break
        elif win1 == False:
            print("Tie")
            break

            
        DoAiMove("O")
        DisplayBoard()
        win2 = CheckIfEnd()
        if win2 != " " and win2 != False:
            print(win2 + " has won!")
            break
        elif win2 == False:
            print("Tie")
            break

def StartYGame():
    global board
    board = CreateBoard()
    ClearOutput()
    while True:
        DoAiMove("X")
        DisplayBoard()
        win1 = CheckIfEnd()
        if win1 != " " and win1 != False:
            print(win1 + " has won!")
            break
        elif win1 == False:
            print("Tie")
            break
            
        GetPlayerInput("O")
        DisplayBoard()
        win2 = CheckIfEnd()
        if win2 != " " and win2 != False:
            print(win2 + " has won!")
            break
        elif win2 == False:
            print("Tie")
            break
    pass

def ChooseXOrO():
    Response = input("Do You Want To Be X's Or O's? (x/o)")

    Response = Response.lower()

    if Response == "x":
        return "X"
    elif Response == "o":
        return "O"
    else:
        print("That Was Not A Valid Response. Try Again")
        return ChooseXOrO()

def AskForGame():
    Response = input("Want To Play A Game Of Tic Tac Toe? (y/n)")

    Response = Response.lower()
    if Response == "y":
        
        XorO = ChooseXOrO()
        if XorO == "X":
            StartXGame()
        elif XorO == "O":
            StartYGame()
            pass
        return AskForGame()
    elif Response == "n":
        return
    else:
        print("Invalid Input. Try Again.")
        return AskForGame()
    

if __name__ == "__main__":
    ClearOutput()
    AskForGame()
