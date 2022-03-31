# Loop Variables
from random import randint



state = "starting"
ended = False

inventory = []

mainTexts = [
    "The actions you can take are:\nSearch: Gives information about your surroundings.\nCollect: Take an item your are viewing and store it in your inventory.\nInspect: Get a closer look at an object\nWalk: Walk in a direction, north, east, south, or west.\nScream: Call for help.\nOpen: Open something that is closed.\nInventory: See the items in your inventory.\n",
]

def takeInput(acceptableInputs):
    newInput = None
    while True:
        newInput = input("").lower()
        if acceptableInputs.get(newInput):
            return newInput
        else:
            print("Please Input A Valid Input")

def helpFunction():
    print(mainTexts[0])
    pass

def searchFunction():
    randomNumber = randint(1,5)
    if randomNumber == 5:
        print("You Found A Scrap Of Paper")
        print("Would you like to pick it up? (y/n)")
        newInput = takeInput({"y": True, "n": True})
        if newInput == "y":
            inventory.append("paper")
        elif newInput == "n":
            pass
    else:
        print("You find nothing.")
    pass

def collectFunction():
    pass

def inspectFunction():
    pass

def walkFunction():
    pass

def screamFunction():
    pass

def inventoryFunction():
    itemsDict = {}
    if len(inventory) > 0:
        print("Inventory:\n")
        for item in inventory:
            if itemsDict.get(item):
                itemsDict[item] += 1
            else:
                itemsDict[item] = 1
        
        for item in itemsDict:
            print(item + ": " + str(itemsDict[item]) + "\n")
    else:
        print("You Have nothing in your inventory.")
    pass


validInputs = {
        "search": searchFunction,
        "collect": collectFunction,
        "inspect": inspectFunction,
        "walk": walkFunction,
        "scream": screamFunction,
        "inventory": inventoryFunction,
        "help": helpFunction,
    }



print("A throbbing pain eminates from the back of your skull. As you regain conciousness you open your eyes to take in your surroundings. It's dark. You can barely make out your own hand in front of your face.")
# Main Gameplay Loop
while True:
    if ended:
        break
        
    newInput = takeInput(validInputs)

    validInputs[newInput]()


