# Open Source Projects Assignment : Text-based Adventure Game : By Rhys, Kian & Darragh

print("\n\t| CONQUEST OF MUNSTER |\n")
print("Welcome to the world of Munster.\nYou are an adventurer, travelling the world seeking fame and fortune.\n")


# Creates character's name
def generateName():
    print("What is your name, Adventurer?")
    characterName = input("> ")
    print("Your name is " + characterName + ", is that right? (Yes|No)")
    confirm = input("> ")  # TODO Include a character limit (20 chars)
    if confirm.lower() == "no":
        generateName()
    elif confirm.lower() == "yes":
        print("Greetings, " + characterName + "! Let's get you prepared.")
        return characterName
    else:
        print("I didn't quite understand you.")
        generateName()


# Creates character's class
def generateClass(characterName):
    print("What class are you? (Warrior|Rogue|Mage)")
    characterClass = input("> ")
    if characterClass.lower() == "warrior":
        pass
    elif characterClass.lower() == "rogue":
        pass
    elif characterClass.lower() == "mage":
        pass
    else:
        generateClass(characterName)
    print("You're a " + characterClass.lower() + ", is that right? (Yes|No)")
    confirm = input("> ")
    if confirm.lower() == "no":
        generateClass(characterName)
    elif confirm.lower() == "yes":
        if characterClass.lower() == "warrior":
            print("That massive blade on your back gave it away. Well met, Warrior!")
        elif characterClass.lower() == "rogue":
            print("Hmm... I knew my coin purse felt lighter. Well met, Rogue!")
        elif characterClass.lower() == "mage":
            print("Those are some fine looking robes. Well met, Mage!")
        print("Well, " + characterName + " the " + characterClass.lower() + ", your adventure begins now. Good luck!")
        return characterClass
    else:
        print("I didn't quite understand you.")
        generateClass(characterName)


name = generateName()
role = generateClass(name)

# Warrior Storyline
if role == "warrior":
    # TODO Create storyline for the warrior
    pass

# Rogue Storyline
elif role == "rogue":
    # TODO Create storyline for the rogue
    pass

# Mage Storyline
elif role == "mage":
    # TODO Create storyline for the mage
    pass
