from random import randint, random
from colorama import Fore, Back, Style, init
from Tkinter import *
from PIL import Image, ImageTk
from hero import Hero

init(autoreset=True)

def randList(list):
    return list[randint(0, len(list) - 1)]

def randDict(dict):
    rand = randList(dict.keys())
    return dict[rand]

colors = {"Red": Fore.RED, "Green": Fore.GREEN, "Blue": Fore.BLUE, "Colorless": Fore.RESET}

summonPool = {}
heroes = open("src/heroes.csv", 'r')
lines = heroes.read().split("\n")[:-1]
for line in lines:
    hero = line.split(",")
    name = hero[0]
    weaponType = hero[1]
    move = hero[2]
    weapon = hero[3]
    assist = hero[4]
    special = hero[5]
    a = hero[6]
    b = hero[7]
    c = hero[8]
    s = hero[9]
    summonPool[name] = Hero(name, weaponType, move, weapon, assist, special, a, b, c, s)
heroes.close()

focusPool = {}
focusHeroes = open("src/focus.csv", 'r')
lines = focusHeroes.read().split("\n")[:-1]
for line in lines:
    hero = line.split(",")
    name = hero[0]
    weaponType = hero[1]
    move = hero[2]
    weapon = hero[3]
    assist = hero[4]
    special = hero[5]
    a = hero[6]
    b = hero[7]
    c = hero[8]
    s = hero[9]
    focusPool[name] = Hero(name, weaponType, move, weapon, assist, special, a, b, c, s)
focusHeroes.close()

def summon():
    if len(focusPool) > 0:
        result = randDict({True: focusPool, False: summonPool}[random() < 0.05])
    else:
        result = randDict(summonPool)
    resultText = "You summoned " + result.name + "!"
    summoned.config(text=resultText)

    try:
        heroImg = Image.open("src/images/heroes/" + result.name + ".png")
        heroImg = heroImg.resize((250, 250), Image.ANTIALIAS)
        heroPic = ImageTk.PhotoImage(heroImg)

        heroImage.config(image=heroPic, text='')
        heroImage.image = heroPic
    except:
        heroImage.config(text="Image Not Found", image='')

    weapImg = Image.open("src/images/weapons/" + result.weaponType + ".png")
    weapImg = weapImg.resize((25, 25), Image.ANTIALIAS)
    heroWeap = ImageTk.PhotoImage(weapImg)

    moveImg = Image.open("src/images/movement/" + result.movementType + ".png")
    moveImg = moveImg.resize((25, 25), Image.ANTIALIAS)
    heroMove = ImageTk.PhotoImage(moveImg)

    weaponImage.config(image=heroWeap)
    weaponImage.image = heroWeap
    moveImage.config(image=heroMove)
    moveImage.image = heroMove
    print result.name + " "*(21-len(result.name)) + colors[result.color] + result.weaponType + Style.RESET_ALL + "\t" + result.movementType

root = Tk()
root.title("Summoning Screen")
root.geometry("400x400")

heroImage = Label(root)
heroImage.pack()

weapMove = Frame(root)
weapMove.pack(side=BOTTOM)

resultFrame = Frame(root)
resultFrame.pack(side=BOTTOM)

summonButton = Button(resultFrame, text="Summon", command=summon)
summonButton.pack()

summoned = Label(resultFrame)
summoned.pack()

weaponImage = Label(weapMove)
weaponImage.pack(side=LEFT)

moveImage = Label(weapMove)
moveImage.pack(side=RIGHT)

root.mainloop()
