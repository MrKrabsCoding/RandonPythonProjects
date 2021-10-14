# Tick Tack Toe

import random
from typing import cast

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
        if not board[i] == "-":
            continue
        Slots[i + 1] = i
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



def GetPlayerInput():
    OpenSlots = GetCurrentSlotsOpen()
    response = input("Choose a Slot")

    response = ConvertResponse(response)   


if __name__ == "__main__":
    board = CreateBoard()
    ClearOutput()
    DisplayBoard()
    GetCurrentSlotsOpen()
