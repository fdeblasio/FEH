from FEH import *

def randHero(name = "", weap = "", move = "", wep = "", asst = "", spec = "", a = "", b = "", c = "", s = ""):
    weaponType = randList(weaponTypes)
    movementType = randList(movementTypes)

    if weap in weaponTypes:
        weaponType = weap
    if move in movementTypes:
        movementType = move

    rand = Hero(name, weaponType, movementType, wep, asst, spec, a, b, c, s)
    if wep in {"", "-"}:
        rand.weapon = randList(weapons[rand.weaponType].keys())
    if asst in {"", "-"}:
        rand.assist = randList(rand.assists)
    if spec in {"", "-"}:
        rand.special = randList(rand.specials)
    if a in {"", "-"}:
        rand.A = randList(rand.As)
    if b in {"", "-"}:
        rand.B = randList(rand.Bs)
    if c in {"", "-"}:
        rand.C = randList(rand.Cs)
    if s in {"", "-"}:
        rand.S = randList(rand.seals)
    rand.update()

    return rand

def debug():
    for weaponType in weaponTypes:
        for movementType in movementTypes:
            rand = randHero(weaponType, movementType)
            rand.toString()
            print
    print "Done"

#debug()

rand = randHero()
#rand = randHero(weap = "Sword")
#rand = randHero(move = "Infantry")
#rand = randHero(name = "Ulmar Protagonist XV")
#rand = randHero(weap = "Sword", move = "Infantry")
rand.toString()
