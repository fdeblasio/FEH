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
    print result.name + " "*(21-len(result.name)) + colors[result.color] + Style.BRIGHT + result.weaponType + Style.RESET_ALL + "\t" + result.movementType

    weaponImg = Image.open("src/images/skills/Weapon.png")
    weaponImg = weaponImg.resize((25, 25), Image.ANTIALIAS)
    weapImg = ImageTk.PhotoImage(weaponImg)

    assistImg = Image.open("src/images/skills/Assist.png")
    assistImg = assistImg.resize((25, 25), Image.ANTIALIAS)
    asstImg = ImageTk.PhotoImage(assistImg)

    specialImg = Image.open("src/images/skills/Special.png")
    specialImg = specialImg.resize((25, 25), Image.ANTIALIAS)
    specImg = ImageTk.PhotoImage(specialImg)

    weaponImage.config(image=weapImg)
    weaponImage.image = weapImg
    weaponName.config(text=result.weapon)
    assistImage.config(image=asstImg)
    assistImage.image = asstImg
    assistName.config(text=result.assist)
    specialImage.config(image=specImg)
    specialImage.image = specImg
    specialName.config(text=result.special)
    print result.weapon, result.assist, result.special

root = Tk()
root.title("Summoning Screen")
root.geometry("500x500")

heroImage = Label(root)
heroImage.pack()

heroSkills = Frame(root)
heroSkills.pack(side=BOTTOM)
weaponFrame = Frame(heroSkills)
weaponFrame.pack()
assistFrame = Frame(heroSkills)
assistFrame.pack()
specialFrame = Frame(heroSkills)
specialFrame.pack()

weapMove = Frame(root)
weapMove.pack(side=BOTTOM)

resultFrame = Frame(root)
resultFrame.pack(side=BOTTOM)

summonButton = Button(resultFrame, text="Summon", command=summon)
summonButton.pack()

summoned = Label(resultFrame)
summoned.pack()

weaponTypeImage = Label(weapMove)
weaponTypeImage.pack(side=LEFT)
moveImage = Label(weapMove)
moveImage.pack(side=RIGHT)

weaponImage = Label(weaponFrame)
weaponImage.pack(side=LEFT)
weaponName = Label(weaponFrame)
weaponName.pack(side=RIGHT)
assistImage = Label(assistFrame)
assistImage.pack(side=LEFT)
assistName = Label(assistFrame)
assistName.pack(side=RIGHT)
specialImage = Label(specialFrame)
specialImage.pack(side=LEFT)
specialName = Label(specialFrame)
specialName.pack(side=RIGHT)

root.mainloop()
