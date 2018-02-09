#coding: utf-8
from random import randint

def randList(list):
    return list[randint(0, len(list) - 1)]

def randHero():
    weaponTypes = ["Sword", "Axe", "Lance", "Bow", "Fire", "Wind", "Thunder", "Staff", "Dagger", "Dark", "Light", "Red Breath", "Green Breath", "Blue Breath"]
    movementTypes = ["Infantry", "Cavalry", "Flier", "Armored"]
    movements = {"Infantry" : 2, "Cavalry": 3, "Flier": 2, "Armored": 1}
    weaponType = randList(weaponTypes)
    movementType = randList(movementTypes)
    movement = movements[movementType]
    if weaponType in ["Sword", "Fire", "Dark", "Red Breath"]:
        color = "Red"
    elif weaponType in ["Axe", "Wind", "Green Breath"]:
        color = "Green"
    elif weaponType in ["Lance", "Thunder", "Light", "Blue Breath"]:
        color = "Blue"
    elif weaponType in ["Bow", "Dagger", "Staff"]:
        color = "Colorless"

    if weaponType in ["Red Breath", "Green Breath", "Blue Breath"]:
        dragon = True
    else:
        dragon = False
    if weaponType in ["Sword", "Axe", "Lance", "Bow", "Dagger"]:
        physical = True
    elif weaponType in ["Fire", "Wind", "Thunder", "Dark", "Light", "Staff", "Red Breath", "Green Breath", "Blue Breath"]:
        physical = False
    if weaponType in ["Sword", "Axe", "Lance", "Red Breath", "Green Breath", "Blue Breath"]:
        melee = True
    elif weaponType in ["Bow", "Dagger", "Fire", "Wind", "Thunder", "Dark", "Light", "Staff"]:
        melee = False

    damage = {True: "Physical", False: "Magical"}[physical]
    distance = {True: "Melee", False: "Ranged"}[melee]

    swords = [("Armorsmasher", 14), ("Brave Sword", 8), ("Firesweep Sword", 15), ("Kadomatsu", 14), ("Ruby Sword", 12), ("Silver Sword", 15), ("Slaying Edge", 14), ("Wo Dao", 13), ("Zanbato", 14)]
    axes = [("Brave Axe", 8), ("Carrot Axe", 13), ("Emerald Axe", 12), ("Hagoita", 14), ("Handbell", 14), ("Legion's Axe", 14), ("Lilith Floatie", 14), ("Melon Crusher", 14), ("Sack o' Gifts", 14), ("Silver Axe", 15), ("Slaying Axe", 14), ("Slaying Hammer", 14)]
    lances = [("Berkut's Lance", 14), ("Brave Lance", 8), ("Carrot Lance", 13), ("Deft Harpoon", 14), ("Firesweep Lance", 15), ("First Bite", 14), ("Ridersbane", 14), ("Sapphire Lance", 12), ("Silver Lance", 15), ("Slaying Lance", 14), ("Slaying Spear", 14), ("Tannenboom!", 14), ("Casa Blanca", 12)]
    bows = [("Assassin's Bow", 11), ("Brave Bow", 7), ("Clarisse's Bow", 11), ("Cupid Arrow", 11), ("Firesweep Bow", 11), ("Guard Bow", 12), ("Hama Ya", 12), ("Monstrous Bow", 12), ("Refreshing Bolt", 12), ("Silver Bow", 13), ("Slaying Bow", 12), ("Gratia", 12)]
    daggers = [("Dancer's Fan", 10), ("Kagami Mochi", 12), ("Kitty Paddle", 8), ("Poison Dagger", 5), ("Rogue Dagger", 7), ("Seashell", 10), ("Silver Dagger", 10), ("Smoke Dagger", 9)]
    fires = [("Bolganone", 13), ("Candelabra", 12)]
    winds = [("Dancer's Ring", 12), ("Green Egg", 11), ("Gronnblade", 13), ("Gronnowl", 10), ("Gronnraven", 11), ("Keen Gronnwolf", 12), ("Rexcalibur", 13), ("Spectral Tome", 12), ("Green Gift", 12)]
    thunders = [("Thoron", 13)]
    staffs = [("Absorb", 7), ("Candlelight", 11), ("Fear", 12), ("Gravity", 10), ("Pain", 10), ("Panic", 11), ("Slow", 12)]
    darks = [("Fenrir", 13)]
    lights = [("Shine", 13), ("Blue Egg", 11), ("Blessed Bouqet", 12), ("Blue Gift", 12)]
    breaths = [("Dark Breath", 13), ("Flametongue", 15), ("Light Breath", 13), ("Lightning Breath", 11)]

    reds = [("Keen Rauðrwolf", 12), ("Rauðrblade", 13), ("Rauðrowl", 10), ("Rauðrraven", 11), ("Tomato Tome", 12)]
    blues = [("Blárblade", 13), ("Blárowl", 10), ("Blárraven", 11), ("Keen Blárwolf", 12), ("Dancer's Score", 12), ("Sealife Tome", 12)]

    fires.extend(reds)
    darks.extend(reds)
    thunders.extend(blues)
    lights.extend(blues)

    exclusiveSwords = [("Fólkvangr", 16), ("Falchion", 16), ("Ragnell", 16), ("Raijinto", 16), ("Alondite", 16), ("Amiti", 11), ("Durandal", 16), ("Blazing Durandal", 16), ("Audhulma", 16), ("Arya's Blade", 16), ("Binding Blade", 16), ("Tyrfing", 16), ("Divine Tyrfing", 16), ("Dark Greatsword", 16), ("Eckesachs", 16), ("Laevatein", 16), ("Mystletainn", 16), ("Regal Blade", 16), ("Resolute Blade", 16), ("Siegfried", 16), ("Sieglinde", 16), ("Sol Katti", 16), ("Yato", 16), ("Wing Sword", 16)]
    exclusiveAxes = [("Armads", 16), ("Basilikos", 16), ("Hauteclere", 16), ("Nóatún", 16), ("Sinmara", 16), ("Stout Tomahawk", 16), ("Urvan", 16), ("Urðr", 16), ("Berserk Armads", 16)]
    exclusiveLances = [("Fensalir", 16), ("Leiptr", 16), ("Siegmund", 16), ("Gradivus", 16), ("Cursed Lance", 16), ("Geirskögul", 16), ("Vidofnir", 16), ("Bright Naginata", 16), ("Hinoka's Spear", 16)]
    exclusiveBows = [("Fujin Yumi", 14), ("Mulagir", 14), ("Nidhogg", 14), ("Parthia", 14)]
    exclusiveDaggers = [("Deathly Dagger", 11), ("Peshkatz", 14), ("Felicia's Plate", 14)]
    exclusiveFires = [("Cymbeline", 14), ("Valflame", 14), ("Ragnarok", 14)]
    exclusiveWinds = [("Élivágar", 14), ("Excalibur", 14), ("Naga", 14), ("Divine Naga", 14), ("Dark Excalibur", 14), ("Blizzard", 14)]
    exclusiveThunders = [("Valaskjálf", 14), ("Dire Thunder", 9), ("Dark Aura", 14), ("Weirding Tome", 14)]
    exclusiveStaffs = [("Thökk", 14)]
    exclusiveDarks = [("Brynhildr", 14), ("Gleipnir", 14), ("Naglfar", 14), ("Grimoire", 0)]
    exclusiveLights = [("Aura", 14), ("Thani", 14), ("Ivaldi", 14)]
    exclusiveBreaths = [("Great Flame", 16)]

    weapons = {"Sword": swords, "Axe": axes, "Lance": lances, "Bow": bows, "Dagger": daggers, "Fire": fires, "Wind": winds, "Thunder": thunders, "Dark": darks, "Light": lights, "Staff": staffs, "Red Breath": breaths, "Green Breath": breaths, "Blue Breath": breaths}
    effective = []

    assists = ["Ardent Sacrifice", "Draw Back", "Harsh Command", "Pivot", "Reciprocal Aid", "Reposition", "Shove", "Smite", "Swap", "Rally Attack", "Rally Speed", "Rally Defense", "Rally Resistance", "Rally Attack/Speed", "Rally Attack/Defense", "Rally Attack/Resistance", "Rally Speed/Defense", "Rally Speed/Resistance", "Rally Defense/Resistance"]
    heals = ["Martyr", "Physic", "Recover", "Rehabilitate"]
    exclusiveAssists = ["Dance", "Sing", "Sacrifice"]

    normalSpecials = ["Sol", "Luna", "Astra", "Noontime", "Moonbow", "Glimmer", "Aether", "Dragon Fang", "Ignis", "Glacies", "Draconic Aura", "Bonfire", "Iceberg", "Vengeance", "Reprisal", "Blazing Flame", "Growing Flame", "Blazing Thunder", "Growing Thunder", "Blazing Wind", "Growing Wind", "Blazing Light", "Growing Light", "Miracle"]
    meleeSpecials = ["Aegis", "Pavise", "Sacred Cowl", "Escutcheon"]
    physicalMeleeSpecials = ["Galeforce"]
    healSpecials = ["Imbue", "Kindled-Fire Balm", "Swift-Winds Balm", "Solid-Earth Balm", "Still-Water Balm", "Heavenly Light", "Miracle"]
    exclusiveSpecials = ["Black Luna", "Ice Mirror", "Radiant Aether", "Regnal Astra"]

    weaponTuple = randList(weapons[weaponType])

    weapon = weaponTuple[0]
    MT = weaponTuple[1]
    #Assist
    if weaponType == "Staff":
        assist = randList(heals)
    else:
        assist = randList(assists)
    #Special
    if weaponType == "Staff":
        special = randList(healSpecials)
    else:
        specials = normalSpecials[:]
        if melee:
            specials.extend(meleeSpecials)
            if physical:
                specials.extend(physicalMeleeSpecials)
        special = randList(specials)

    normalAs = ["HP +5", "Attack +3", "Speed +3", "Defense +3", "Resistance +3", "HP/Attack", "HP/Speed", "HP/Defense", "HP/Resistance", "Attack/Speed +2", "Attack/Defense +2", "Attack/Resistance +2", "Speed/Defense +2", "Speed/Resistance +2", "Defiant Attack", "Defiant Speed", "Defiant Defense", "Defiant Resistance", "Fortress Defense", "Fortress Resistance", "Steady Stance", "Warding Stance", "Fire Boost", "Wind Boost", "Earth Boost", "Water Boost", "Attack/Speed Bond", "Attack/Defense Bond", "Attack/Resistance Bond", "Speed/Defense Bond", "Brazen Attack/Speed", "Brazen Attack/Def", "Close Defense", "Distant Defense"]
    #Def/Res, Spd/Res Bond, Def/Res Bond, #Brazen Atk/Res, Brazen Spd/Def, Brazen Spd/Res, Brazen Def/Res
    meleeAs = ["Distant Counter"]
    rangedAs = ["Close Counter"]
    noStaffAs = ["Death Blow", "Darting Blow", "Armored Blow", "Warding Blow", "Swift Sparrow", "Sturdy Blow", "Mirror Strike", "Steady Blow", "Swift Strike", "Bracing Blow", "Fierce Stance", "Fury", "Life and Death", "Flashing Blaze"]
    #Speed Stance
    cavalryAs = ["Grani's Shield"]
    flierAs = ["Iote's Shield"]
    armoredAs = ["Svalinn Shield"]
    noColorlessAs = ["Triangle Adept"]
    infantryArmoredNoStaffAs = ["Flashing Blaze"]
    meleeInfantryArmoredAs = ["Steady Breath", "Warding Breath"]

    normalBs = ["Brash Assault", "Daggerbreaker", "Desperation", "Guard", "Obstruct", "Pass", "Vantage", "Escape Route", "Quick Riposte", "Renewal"]
    meleeBs = ["Drag Back", "Hit and Run", "Knock Back", "Lunge", "Wings of Mercy"]
    staffBs = ["Live to Serve", "Dazzling Staff", "Wrathful Staff"]
    noStaffBs = ["Seal Attack", "Seal Speed", "Seal Defense", "Seal Resistance", "Seal Attack/Speed", "Seal Attack/Defense", "Poison Strike", "Watersweep", "Windsweep"]
    #Seal Atk/Res, Seal Spd/Def, Seal Spd/Res, Seal Def/Res
    noRedBs = ["Blue Tomebreaker", "Lancebreaker"]
    noGreenBs = ["Red Tomebreaker", "Swordbreaker"]
    noBlueBs = ["Axebreaker", "Green Tomebreaker"]
    noFlierBs = ["Bowbreaker"]
    flierBs = ["Flier Formation"]
    armoredBs = ["Bold Fighter", "Vengeful Fighter", "Wary Fighter"]
    noTomeNoStaffBs = ["Cancel Affinity"]
    #no (magic AND ranged)
    meleeInfantryArmoredBs = ["Shield Pulse", "Wrath"]
    singDanceBs = ["Blaze Dance", "Earth Dance", "Gale Dance", "Geyser Dance"]
    exclusiveBs = ["Follow-Up Ring", "Recover Ring", "Beorc's Blessing", "Crusader's Ward", "Sacae's Blessing", "Warp Powder"]

    normalCs = ["Breath of Life", "Hone Attack", "Hone Speed", "Fortify Defense", "Fortify Resistance", "Savage Blow", "Spur Attack", "Spur Speed", "Spur Defense", "Spur Resistance", "Drive Attack", "Spur Attack/Speed", "Spur Speed/Defense", "Spur Defense/Resistance", "Drive Speed", "Drive Defense", "Drive Resistance", "Threaten Attack", "Threaten Speed", "Threaten Defense", "Threaten Resistance", "Attack Ploy", "Speed Ploy", "Defense Ploy", "Resistance Ploy", "Panic Ploy", "Attack Tactic", "Defense Tactic", "Resistance Tactic"]
    #Speed Tactic, Spur Attack/Defense, Spur Attack/Resistance, Spur Speed/Resistance
    noStaffCs = ["Attack Smoke", "Speed Smoke"]
    #Defense Smoke, Resistance Smoke
    infantryCs = ["Infantry Pulse"]
    armoredCs = ["Hone Armor", "Fortify Armor", "Goad Armor", "Ward Armor", "Armor March"]
    cavalryCs = ["Hone Cavalry", "Fortify Cavalry", "Goad Cavalry", "Ward Cavalry"]
    flierCs = ["Hone Fliers", "Fortify Fliers", "Goad Fliers", "Ward Fliers", "Guidance"]
    dragonCs = ["Hone Dragons", "Fortify Dragons"]
    #Goad Dragons, Ward Dragons
    axeCs = ["Axe Experience", "Axe Valor"]
    blueTomeCs = ["Blue Tome Experience", "Blue Tome Valor"]
    bowCs = ["Bow Experience", "Bow Valor"]
    daggerCs = ["Dagger Valor"]
    #Dagger Experience
    greenTomeCs = ["Green Tome Valor"]
    #Green Tome Experience
    lanceCs = ["Lance Valor"]
    #Lance Experience
    redTomeCs = ["Red Tome Experience", "Red Tome Valor"]
    swordCs = ["Sword Experience", "Sword Valor"]

    normalSeals = ["Attack Ploy", "Attack +3", "Brash Assault", "Breath of Life", "Close Defense", "Defense Ploy", "Defense +3", "Deflect Magic", "Deflect Missile", "Distant Defense", "Drive Defense", "Fortify Defense", "Fortify Res", "Hardy Bearing", "Hone Attack", "Hone Speed", "HP +5", "Initiate Seal Attack", "Initiate Seal Defense", "Initiate Seal HP", "Initiate Seal Res", "Initiate Seal Speed", "Panic Ploy", "Phantom Speed", "Quick Riposte", "Quickened Pulse", "Resistance +3", "Savage Blow", "Seal Attack", "Speed +3", "Spur Attack", "Spur Defense", "Spur Resistance", "Spur Speed", "Squad Ace A", "Squad Ace B", "Squad Ace C", "Squad Ace D", "Squad Ace E", "Squad Ace F", "Threaten Speed"]
    noStaffSeals = ["Attack Smoke", "Heavy Blade", "Poison Strike"]
    meleeSeals = ["Deflect Melee"]
    flierSeals = ["Guidance", "Iote's Shield"]
    exclusiveSeals = ["Embla's Ward", "Múspellflame"]

    #A Skill
    As = normalAs[:]
    if weaponType != "Staff":
        As.extend(noStaffAs)
        if color != "Colorless":
            As.extend(noColorlessAs)
        if movementType == "Infantry" or movementType == "Armored":
            As.extend(infantryArmoredNoStaffAs)
    if melee:
        As.extend(meleeAs)
        if movementType == "Infantry" or movementType == "Armored":
            As.extend(meleeInfantryArmoredAs)
    elif not melee:
        As.extend(rangedAs)
    if movementType == "Cavalry":
        As.extend(cavalryAs)
    elif movementType == "Armored":
        As.extend(armoredAs)
    elif movementType == "Flier":
        As.extend(flierAs)
    A = randList(As)

    #B Skill
    Bs = normalBs[:]
    if weaponType == "Staff":
        Bs.extend(staffBs)
    else:
        Bs.extend(noStaffBs)
        if melee:
            Bs.extend(meleeBs)
            Bs.extend(noTomeNoStaffBs)
            if movementType == "Infantry" or movementType == "Armored":
                Bs.extend(meleeInfantryArmoredBs)
        elif not melee:
            if physical:
                Bs.extend(noTomeNoStaffBs)
    if movementType == "Flier":
        Bs.extend(flierBs)
    else:
        Bs.extend(noFlierBs)
        if movementType == "Armored":
            Bs.extend(armoredBs)
    if color != "Red":
        Bs.extend(noRedBs)
    if color != "Green":
        Bs.extend(noGreenBs)
    if color != "Blue":
        Bs.extend(noBlueBs)
    B = randList(Bs)

    #C Skill
    Cs = normalCs[:]
    weaponCs = {"Sword": swordCs, "Axe": axeCs, "Lance": lanceCs, "Bow": bowCs, "Dagger": daggerCs, "Fire": redTomeCs, "Wind": greenTomeCs, "Thunder": blueTomeCs, "Dark": redTomeCs, "Light": blueTomeCs}
    movementCs = {"Infantry": infantryCs, "Cavalry": cavalryCs, "Armored": armoredCs, "Flier": flierCs}
    if weaponType != "Staff":
        Cs.extend(noStaffCs)
        if dragon:
            Cs.extend(dragonCs)
        else:
            Cs.extend(weaponCs[weaponType])
    Cs.extend(movementCs[movementType])
    C = randList(Cs)

    #Sacred Seal
    seals = normalSeals[:]
    if weaponType != "Staff":
        seals.extend(noStaffSeals)
        if melee:
            seals.extend(meleeSeals)
    if movementType == "Flier":
        seals.extend(flierSeals)
    S = randList(seals)

    if (weaponType == "Bow" and weapon != "-") or weapon == "Excalibur":
        effective.append("Fliers")

    #not implemeneted from skills yet besides weapon MT
    #neutral IVs for now

    #47 - 1 for each stat
    BST = 42
    #31 - 1 for each stat
    GP = 26
    if assist == "Dance" or assist == "Sing":
        BST -= 8
    if not melee:
        BST -= 3
        GP -= 3
    if movementType == "Cavalry":
        BST -= 1
        GP -= 1
    elif movementType == "Armored":
        BST += 7
        GP += 2

    OGBST = BST + 5
    OGGP = GP + 5

    baseStats = [1, 1, 1, 1, 1]
    statGrowths = [1, 1, 1, 1, 1]

    for i in range(BST):
        baseStat = randint(1, 5) - 1
        baseStats[baseStat] += 1

    for j in range(GP):
        while True:
            statGrowth = randint(1, 5) - 1
            if statGrowths[statGrowth] < 12:
                statGrowths[statGrowth] += 1
                break

    growthValues = {1: 10, 2: 13, 3: 15, 4: 17, 5: 19, 6: 22, 7: 24, 8: 26, 9: 28, 10: 30, 11: 33, 12: 35}
    #1: 10, 2-5: 2x+9, 6-10: 2x+10, 11-12: 2x+11

    stats = []
    for i in range(5):
        stats.append(baseStats[i] + growthValues[statGrowths[i]])

    #for accessing stats in the list
    HP = 0
    Atk = 1
    Spd = 2
    Def = 3
    Res = 4

    #Adds weapon MT
    stats[Atk] += MT

    name = ""
    if weaponType in ["Sword", "Axe", "Lance"]:
        name += weaponType + " " + {"Infantry": "Fighter", "Armored": "Knight", "Cavalry": "Cavalier", "Flier": "Flier"}[movementType]
    else:
        if movementType == "Armored":
            name += movementType + " "
        elif movementType == "Flier":
            name += "Flying "
        elif movementType == "Cavalry":
            name += "Horseback "
        if dragon:
            name += color + " Dragon"
        elif weaponType == "Staff":
            name += "Cleric"
            if movementType == "Cavalry":
                name = "Troubadour"
        elif weaponType == "Dagger":
            name += "Thief"
        elif not physical:
            name += weaponType + " Mage"
            if movementType == "Cavalry":
                name = name.replace("Horseback ", "") + " Cavalier"
        elif weaponType == "Bow":
            name += "Archer"
            if movementType == "Cavalry":
                name = "Bow Knight"

    cooldown = 7
    if special == "Imbue" or special.endswith("Balm"):
        cooldown = 1
    elif special in ["Escutcheon", "Glimmer", "Heavenly Light", "Moonbow", "Noontime", "Reprisal", "Sacred Cowl", "Ice Mirror", "Regnal Astra"]:
        cooldown = 2
    elif special in ["Aegis", "Bonfire", "Draconic Aura", "Iceberg", "Luna", "Pavise", "Sol", "Vengeance", "Black Luna"]:
        cooldown = 3
    elif special in ["Astra", "Dragon Fang", "Ignis", "Glacies", "Radiant Aether"] or special.startswith("Blazing") or special.startswith("Growing"):
        cooldown = 4
    elif special in ["Aether", "Galeforce", "Miracle"]:
        cooldown = 5
    if weapon in ["Rauðrblade", "Gronnblade", "Blárblade", "Lightning Breath"]:
        cooldown += 1
    elif weapon in ["Slaying Edge", "Slaying Axe", "Slaying Lance", "Slaying Bow", "Hauteclere", "Mystletainn", "Cursed Lance", "Urvan", "Audhulma", "Kagami Mochi", "Berserk Armads"]:
        cooldown -= 1
    special += " (Cooldown: %d)" % cooldown

    skills = [weapon, assist, special, A, B, C, S]
    skillString = ["Weapon", "Assist", "Special", "A", "B", "C", "S"]
    statString = ["HP: ", "Atk:", "Spd:", "Def:", "Res:"]

    print
    print name
    print
    print "Color:", color
    print "Movement:", movement
    print "Damage Type:", distance, damage
    print
    for i in range(len(skills)):
        print skillString[i] + ":", skills[i]
    print
    for i in range(len(stats)):
        print statString[i], stats[i]
    print
    print baseStats
    print statGrowths

if __name__== "__main__":
    randHero()
