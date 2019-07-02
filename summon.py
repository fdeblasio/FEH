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
    print result.name
    print colors[result.color] + Style.BRIGHT + result.weaponType + Style.RESET_ALL + "\t" + result.movementType

    try:
        imageA = Image.open("src/images/skills/" + result.A + ".png")
        imageA = imageA.resize((25, 25), Image.ANTIALIAS)
        ImageA = ImageTk.PhotoImage(imageA)

        AImage.config(image=ImageA)
        AImage.image = ImageA
    except:
        AImage.config(image=aImg)

    try:
        imageB = Image.open("src/images/skills/" + result.B + ".png")
        imageB = imageB.resize((25, 25), Image.ANTIALIAS)
        ImageB = ImageTk.PhotoImage(imageB)

        BImage.config(image=ImageB)
        BImage.image = ImageB
    except:
        BImage.config(image=bImg)

    try:
        imageC = Image.open("src/images/skills/" + result.C + ".png")
        imageC = imageC.resize((25, 25), Image.ANTIALIAS)
        ImageC = ImageTk.PhotoImage(imageC)

        CImage.config(image=ImageC)
        CImage.image = ImageC
    except:
        CImage.config(image=cImg)

    weaponName.config(text=result.weapon + " "*(20-len(result.weapon)))
    AName.config(text=result.A + " "*(20-len(result.A)))
    print "Weapon:  " + result.weapon + " "*(20-len(result.weapon)) + "A: " + result.A
    assistName.config(text=result.assist + " "*(20-len(result.assist)))
    BName.config(text=result.B + " "*(20-len(result.B)))
    print "Assist:  " + result.assist + " "*(20-len(result.assist)) + "B: " + result.B
    specialName.config(text=result.special + " "*(20-len(result.special)))
    CName.config(text=result.C + " "*(20-len(result.C)))
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

weaponImg = Image.open("src/images/skills/Weapon.png")
weaponImg = weaponImg.resize((25, 25), Image.ANTIALIAS)
weapImg = ImageTk.PhotoImage(weaponImg)
weaponImage = Label(heroSkills, image=weapImg)
weaponImage.grid(row=0, column=0)
weaponImage.image = weapImg
weaponName = Label(heroSkills, text="-"+" "*19, font=("Fira Mono", 11))
weaponName.grid(row=0, column=1)

assistImg = Image.open("src/images/skills/Assist.png")
assistImg = assistImg.resize((25, 25), Image.ANTIALIAS)
asstImg = ImageTk.PhotoImage(assistImg)
assistImage = Label(heroSkills, image=asstImg)
assistImage.grid(row=1, column=0)
assistImage.image = asstImg
assistName = Label(heroSkills, text="-"+" "*19, font=("Fira Mono", 11))
assistName.grid(row=1, column=1)

specialImg = Image.open("src/images/skills/Special.png")
specialImg = specialImg.resize((25, 25), Image.ANTIALIAS)
specImg = ImageTk.PhotoImage(specialImg)
specialImage = Label(heroSkills, image=specImg)
specialImage.grid(row=2, column=0)
specialImage.image = specImg
specialName = Label(heroSkills, text="-"+" "*19, font=("Fira Mono", 11))
specialName.grid(row=2, column=1)

AImg = Image.open("src/images/skills/A.png")
AImg = AImg.resize((25, 25), Image.ANTIALIAS)
aImg = ImageTk.PhotoImage(AImg)
AImage = Label(heroSkills, image=aImg)
AImage.grid(row=0, column=2)
AImage.image = aImg
AName = Label(heroSkills, text="-"+" "*19, font=("Fira Mono", 11))
AName.grid(row=0, column=3)

BImg = Image.open("src/images/skills/B.png")
BImg = BImg.resize((25, 25), Image.ANTIALIAS)
bImg = ImageTk.PhotoImage(BImg)
BImage = Label(heroSkills, image=bImg)
BImage.grid(row=1, column=2)
BImage.image = bImg
BName = Label(heroSkills, text="-"+" "*19, font=("Fira Mono", 11))
BName.grid(row=1, column=3)

CImg = Image.open("src/images/skills/C.png")
CImg = CImg.resize((25, 25), Image.ANTIALIAS)
cImg = ImageTk.PhotoImage(CImg)
CImage = Label(heroSkills, image=cImg)
CImage.grid(row=2, column=2)
CImage.image = cImg
CName = Label(heroSkills, text="-"+" "*19, font=("Fira Mono", 11))
CName.grid(row=2, column=3)

root.mainloop()
