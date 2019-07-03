from random import randint, random
from colorama import Fore, Back, Style, init
from Tkinter import *
from PIL import Image, ImageTk
from FEH import Hero

init(autoreset=True)

def randList(list):
    return list[randint(0, len(list) - 1)]

def randDict(dict):
    rand = randList(dict.keys())
    return dict[rand]

colors = {"Red": Back.RED, "Green": Back.GREEN, "Blue": Back.BLUE, "Colorless": Back.WHITE}

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

    weapTypeImg = Image.open("src/images/weapons/" + result.weaponType + ".png")
    weapTypeImg = weapTypeImg.resize((25, 25), Image.ANTIALIAS)
    heroWeapType = ImageTk.PhotoImage(weapTypeImg)

    moveImg = Image.open("src/images/movement/" + result.movementType + ".png")
    moveImg = moveImg.resize((25, 25), Image.ANTIALIAS)
    heroMove = ImageTk.PhotoImage(moveImg)

    weaponTypeImage.config(image=heroWeapType)
    weaponTypeImage.image = heroWeapType
    moveImage.config(image=heroMove)
    moveImage.image = heroMove
    print result.name
    print colors[result.color] + Style.BRIGHT + result.weaponType + Style.RESET_ALL + "\t" + result.movementType

    passives = ["A", "B", "C"]
    resultSkills = {"Weapon": result.weapon, "Assist": result.assist, "Special": result.special, "A": result.A, "B": result.B, "C": result.C}
    passiveImgs = {}
    tkPassImgs = {}
    for passive in passives:
        try:
            passiveImgs[passive] = Image.open("src/images/skills/" + resultSkills[passive] + ".png")
            passiveImgs[passive] = passiveImgs[passive].resize((25, 25), Image.ANTIALIAS)
            tkPassImgs[passive] = ImageTk.PhotoImage(passiveImgs[passive])
            image[passive].config(image=tkPassImgs[passive])
            image[passive].image = tkPassImgs[passive]
        except:
            image[passive].config(image=tkImage[passive])

    for skill in skills:
        name[skill].config(text=resultSkills[skill] + " "*(20-len(resultSkills[skill])))

    print "Weapon:  " + result.weapon + " "*(20-len(result.weapon)) + "A: " + result.A
    print "Assist:  " + result.assist + " "*(20-len(result.assist)) + "B: " + result.B
    print "Special: " + result.special + " "*(20-len(result.special)) + "C: " + result.C
    print

root = Tk()
root.title("Summoning Screen")
root.geometry("500x500")

heroImage = Label(root)
heroImage.pack()

heroSkills = Frame(root)
heroSkills.pack(side=BOTTOM)

weapMove = Frame(root)
weapMove.pack(side=BOTTOM)

resultFrame = Frame(root)
resultFrame.pack(side=BOTTOM)

summonButton = Button(resultFrame, text="Summon", command=summon, font=("nintendoP_Skip-D_003",8))
summonButton.grid(columnspan=2, row=0)

summoned = Label(resultFrame, text="Ready for summoning", font=("nintendoP_Skip-D_003",12))
summoned.grid(columnspan=2, row=1)

weaponTypeImage = Label(resultFrame)
weaponTypeImage.grid(row=2, column=0, sticky=E)
moveImage = Label(resultFrame)
moveImage.grid(row=2, column=1, sticky=W)

skills = ["Weapon", "Assist", "Special", "A", "B", "C"]
origPng = {}
tkImage = {}
image = {}
name = {}
for skill in skills:
    origPng[skill] = Image.open("src/images/skills/" + skill + ".png")
    origPng[skill] = origPng[skill].resize((25, 25), Image.ANTIALIAS)
    tkImage[skill] = ImageTk.PhotoImage(origPng[skill])
    image[skill] = Label(heroSkills, image=tkImage[skill])
    image[skill].image = tkImage[skill]
    name[skill] = Label(heroSkills, text="-"+" "*19, font=("Fira Mono", 11))
    image[skill].grid(row=skills.index(skill)%3, column=2*(skills.index(skill)/3))
    name[skill].grid(row=skills.index(skill)%3, column=2*(skills.index(skill)/3)+1)

root.mainloop()
