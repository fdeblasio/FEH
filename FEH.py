#coding: utf-8
from random import randint

#for accessing stats in the list
HP = 0
Atk = 1
Spd = 2
Def = 3
Res = 4

weaponTypes = ["Sword", "Axe", "Lance", "Colorless Bow", "Fire", "Wind", "Thunder", "Staff", "Dagger", "Dark", "Light", "Red Breath", "Green Breath", "Blue Breath", "Colorless Breath", "Red Bow", "Green Bow", "Blue Bow"]
movementTypes = ["Infantry", "Cavalry", "Flier", "Armored"]

swords = {"Silver Sword": 15, "Slaying Edge": 14, "Brave Sword": 8, "Ruby Sword": 12, "Armorsmasher": 14, "Zanbato": 14, "Wo Dao": 13, "Firesweep Sword": 15, "Safeguard": 14, "Kadomatsu": 14}
axes = {"Silver Axe": 15, "Slaying Axe": 14, "Brave Axe": 8, "Emerald Axe": 12, "Slaying Hammer": 14, "Poleaxe": 14, "Wo Gùn": 14, "Legion's Axe": 14, "Carrot Axe": 13, "Melon Crusher": 14, "Lilith Floatie": 14, "Sack o' Gifts": 14, "Handbell": 14, "Hagoita": 14, "Giant Spoon": 13, "Ardent Service": 14, "Beach Banner": 14}
#Firesweep Axe
lances = {"Silver Lance": 15, "Slaying Lance": 14, "Brave Lance": 8, "Sapphire Lance": 12, "Slaying Spear": 14, "Ridersbane": 14, "Firesweep Lance": 15, "Harmonic Lance": 13, "Reprisal Lance": 14, "Berkut's Lance": 14, "Carrot Lance": 13, "First Bite": 14, "Deft Harpoon": 14, "Tannenboom!": 14, "Casa Blanca": 14, "Shell Lance": 14}
bows = {"Silver Bow": 13, "Slaying Bow": 12, "Brave Bow": 7, "Firesweep Bow": 11, "Assassin's Bow": 11, "Guard Bow": 12, "Clarisse's Bow": 11, "Cupid Arrow": 11, "Refreshing Bolt": 12, "Monstrous Bow": 12, "Hama Ya": 12, "Gratia": 12, "Cocobow": 12, "Fishie Bow": 12}
daggers = {"Silver Dagger": 10, "Rogue Dagger": 7, "Smoke Dagger": 9, "Poison Dagger": 5, "Barb Shuriken": 12, "The Cleaner": 12, "Seashell": 10, "Dancer's Fan": 10, "Kitty Paddle": 8, "Kagami Mochi": 12, "Lethal Carrot": 12, "Starfish": 12}
fires = {"Bolganone": 13}
winds = {"Rexcalibur": 13, "Gronnblade": 13, "Gronnraven": 11, "Keen Gronnwolf": 12, "Gronnowl": 10, "Green Egg": 11, "Hibiscus Tome": 12, "Dancer's Ring": 12, "Spectral Tome": 12, "Green Gift": 12}
#Gronnserpent
thunders = {"Thoron": 13}
staffs = {"Absorb": 7, "Fear": 12, "Gravity": 10, "Pain": 10, "Panic": 11, "Slow": 12, "Trilemma": 12, "Candlelight": 11}
darks = {"Fenrir": 13}
lights = {"Shine": 13}
breaths = {"Dark Breath": 13, "Flametongue": 15, "Light Breath": 13, "Lightning Breath": 11, "Water Breath": 14}

reds = {"Rauðrblade": 13, "Rauðrraven": 11, "Keen Rauðrwolf": 12, "Rauðrowl": 10, "Tomato Tome": 12, "Candelabra": 12}
#Rauðrserpent
blues = {"Blárblade": 13, "Blárraven": 11, "Keen Blárwolf": 12, "Blárowl": 10, "Blue Egg": 11, "Blessed Bouquet": 12, "Sealife Tome": 12, "Dancer's Score": 12, "Blue Gift": 12, "Fresh Bouquet": 12, "Blárserpent": 12, "Juicy Wave": 12}

fires.update(reds)
darks.update(reds)
thunders.update(blues)
lights.update(blues)

exclusiveSwords = {"Fólkvangr": 16, "Falchion": 16, "Ragnell": 16, "Raijinto": 16, "Alondite": 16, "Amiti": 11, "Durandal": 16, "Blazing Durandal": 16, "Audhulma": 16, "Arya's Blade": 16, "Binding Blade": 16, "Tyrfing": 16, "Divine Tyrfing": 16, "Dark Greatsword": 16, "Eckesachs": 16, "Laevatein": 16, "Mystletainn": 16, "Regal Blade": 16, "Resolute Blade": 16, "Siegfried": 16, "Sieglinde": 16, "Sol Katti": 16, "Yato": 16, "Wing Sword": 16, "Beloved Zofia": 16, "Níu": 16, "Sealed Falchion": 16, "Nameless Blade": 16, "Light Brand": 16, "Meisterschwert": 11, "Dark Mystletainn": 16, "Vassal's Blade": 16, "Skuld": 16}
exclusiveAxes = {"Armads": 16, "Basilikos": 16, "Hauteclere": 16, "Nóatún": 16, "Sinmara": 16, "Stout Tomahawk": 16, "Urvan": 16, "Urðr": 16, "Berserk Armads": 16, "Camilla's Axe": 16, "Býleistr": 16, "Thunder Armads": 16, "Draconic Poleax": 16, "Wolf Berg": 16}
exclusiveLances = {"Fensalir": 16, "Leiptr": 16, "Siegmund": 16, "Gradivus": 16, "Cursed Lance": 16, "Geirskögul": 16, "Vidofnir": 16, "Bright Naginata": 16, "Hinoka's Spear": 16, "Flame Siegmund": 16, "Rhomphaia": 16, "Dauntless Lance": 16}
exclusiveBows = {"Fujin Yumi": 14, "Mulagir": 14, "Nidhogg": 14, "Parthia": 14, "Skadi": 14, "Warrior Princess": 14, "Swift Mulagir": 14}
exclusiveDaggers = {"Deathly Dagger": 11, "Peshkatz": 14, "Felicia's Plate": 14}
exclusiveFires = {"Cymbeline": 14, "Valflame": 14, "Ragnarok": 14, "Forblaze": 14, "Múspell Fireposy": 14, "Fruit of Iðunn": 14, "Reese's Tome": 14}
exclusiveWinds = {"Élivágar": 14, "Excalibur": 14, "Naga": 14, "Divine Naga": 14, "Dark Excalibur": 14, "Blizzard": 14, "Wind's Brand": 14, "Munnin's Egg": 14, "Thunderhead": 14, "Nifl Frostflowers": 14, "Giga Excalibur": 14}
exclusiveThunders = {"Valaskjálf": 14, "Dire Thunder": 9, "Dark Aura": 14, "Weirding Tome": 14, "Huggin's Egg": 14, "Mjölnir": 14}
exclusiveStaffs = {"Thökk": 14}
exclusiveDarks = {"Brynhildr": 14, "Gleipnir": 14, "Naglfar": 14, "Grimoire": 14, "Grima's Truth": 14, "Loptous": 14}
exclusiveLights = {"Aura": 14, "Thani": 14, "Ivaldi": 14, "Wargod's Tome": 14}
exclusiveBreaths = {"Great Flame": 16, "Expiration": 16, "Breath of Fog": 16, "Summer Breath": 16}

weapons = {"Sword": swords, "Axe": axes, "Lance": lances, "Colorless Bow": bows, "Dagger": daggers, "Fire": fires, "Wind": winds, "Thunder": thunders, "Dark": darks, "Light": lights, "Staff": staffs, "Red Breath": breaths, "Green Breath": breaths, "Blue Breath": breaths, "Colorless Breath": breaths, "Red Bow": bows, "Green Bow": bows, "Blue Bow": bows}

assists = ["Draw Back", "Pivot", "Reposition", "Swap", "Ardent Sacrifice", "Reciprocal Aid", "Shove", "Smite", "Harsh Command", "Rally Attack", "Rally Speed", "Rally Defense", "Rally Resistance", "Rally Attack/Speed", "Rally Attack/Defense", "Rally Attack/Resistance", "Rally Speed/Defense", "Rally Speed/Resistance", "Rally Defense/Resistance"]
heals = ["Martyr", "Physic", "Recover", "Rehabilitate", "Restore"]
exclusiveAssists = ["Dance", "Sing", "Sacrifice"]

normalSpecials = ["Sol", "Luna", "Astra", "Noontime", "Moonbow", "Glimmer", "Aether", "Dragon Fang", "Ignis", "Glacies", "Draconic Aura", "Bonfire", "Iceberg", "Vengeance", "Reprisal", "Blazing Flame", "Growing Flame", "Blazing Thunder", "Growing Thunder", "Blazing Wind", "Growing Wind", "Blazing Light", "Growing Light", "Miracle"]
meleeSpecials = ["Aegis", "Pavise", "Sacred Cowl", "Escutcheon"]
physicalMeleeSpecials = ["Galeforce"]
healSpecials = ["Imbue", "Kindled-Fire Balm", "Swift-Winds Balm", "Solid-Earth Balm", "Still-Water Balm", "Heavenly Light", "Miracle"]
exclusiveSpecials = ["Black Luna", "Ice Mirror", "Radiant Aether", "Regnal Astra"]

normalAs = ["HP +5", "Attack +3", "Speed +3", "Defense +3", "Resistance +3", "HP/Attack", "HP/Speed", "HP/Defense", "HP/Resistance", "Attack/Speed +2", "Attack/Defense +2", "Attack/Resistance +2", "Speed/Defense +2", "Speed/Resistance +2", "Defiant Attack", "Defiant Speed", "Defiant Defense", "Defiant Resistance", "Fortress Defense", "Fortress Resistance", "Steady Stance", "Warding Stance", "Bracing Stance", "Fire Boost", "Wind Boost", "Earth Boost", "Water Boost", "Attack/Speed Bond", "Attack/Defense Bond", "Attack/Resistance Bond", "Speed/Defense Bond", "Speed/Resistance Bond", "Brazen Attack/Speed", "Brazen Attack/Defense", "Brazen Attack/Resistance", "Brazen Defense/Resistance", "Close Defense", "Distant Defense", "Attack/Speed Push"]
#Def/Res Bond, Brazen Atk/Res, Brazen Spd/Def, Brazen Spd/Res, Pushes
meleeAs = ["Distant Counter"]
rangedAs = ["Close Counter"]
noStaffAs = ["Fury", "Life and Death", "Heavy Blade", "Death Blow", "Darting Blow", "Armored Blow", "Warding Blow", "Swift Sparrow", "Sturdy Blow", "Mirror Strike", "Steady Blow", "Swift Strike", "Bracing Blow", "Fierce Stance", "Darting Stance", "Kestrel Stance", "Sturdy Stance", "Mirror Stance", "Swift Stance"]
#Spd/Def Stance, Spd/Res Stance, Def/Res Stance
cavalryAs = ["Grani's Shield"]
flierAs = ["Iote's Shield"]
armoredAs = ["Svalinn Shield"]
noColorlessAs = ["Triangle Adept"]
infantryArmoredNoStaffAs = ["Flashing Blade"]
meleeInfantryArmoredAs = ["Steady Breath", "Warding Breath"]
exclusiveAs = ["Dragonskin", "Laws of Sacae"]

normalBs = ["Vantage", "Quick Riposte", "Desperation", "Brash Assault", "Daggerbreaker", "Wings of Mercy", "Escape Route", "Renewal", "Guard", "Obstruct", "Chill Attack", "Chill Speed", "Chill Defense", "Chill Resistance", "Dull Ranged"]
meleeBs = ["Drag Back", "Hit and Run", "Knock Back", "Lunge", "Dull Close"]
staffBs = ["Live to Serve", "Dazzling Staff", "Wrathful Staff"]
noStaffBs = ["Seal Attack", "Seal Speed", "Seal Defense", "Seal Resistance", "Seal Attack/Speed", "Seal Attack/Defense", "Seal Defense/Resistance", "Poison Strike", "Watersweep", "Windsweep", "Speed Feint", "Defense Feint", "Attack/Defense Link", "Defense/Resistance Link"]
#Seal Atk/Res, Seal Spd/Def, Seal Spd/Res, Atk/Res Feint, Links
noRedBs = ["Lancebreaker", "Blue Tomebreaker"]
noGreenBs = ["Swordbreaker", "Red Tomebreaker"]
noBlueBs = ["Axebreaker", "Green Tomebreaker"]
noFlierBs = ["Bowbreaker"]
flierBs = ["Flier Formation", "Aerobatics"]
armoredBs = ["Bold Fighter", "Vengeful Fighter", "Wary Fighter"]
noArmoredBs = ["Pass"]
noTomeNoStaffBs = ["Cancel Affinity"]
meleeInfantryArmoredBs = ["Shield Pulse", "Wrath"]
singDanceBs = ["Blaze Dance", "Gale Dance", "Earth Dance", "Torrent Dance", "Firestorm Dance", "Geyser Dance"]
#Atk/Def Dance, Atk/Res Dance, Spd/Def Dance, Spd/Res Dance
exclusiveBs = ["Follow-Up Ring", "Recover Ring", "Beorc's Blessing", "Crusader's Ward", "Sacae's Blessing", "Warp Powder", "Chilling Seal", "Solar Brace", "S Drink", "Bushido"]

normalCs = ["Breath of Life", "Savage Blow", "Hone Attack", "Hone Speed", "Fortify Defense", "Fortify Resistance", "Spur Attack", "Spur Speed", "Spur Defense", "Spur Resistance", "Spur Attack/Speed", "Spur Attack/Defense", "Spur Attack/Resistance", "Spur Speed/Defense", "Spur Defense/Resistance", "Drive Attack", "Drive Speed", "Drive Defense", "Drive Resistance", "Threaten Attack", "Threaten Speed", "Threaten Defense", "Threaten Resistance", "Attack Ploy", "Speed Ploy", "Defense Ploy", "Resistance Ploy", "Panic Ploy", "Attack Tactic", "Speed Tactic", "Defense Tactic", "Resistance Tactic", "Odd Attack Wave", "Even Speed Wave", "Odd Resistance Wave"]
#Spur Speed/Resistance, Even Attack Wave, Odd Speed Wave, Odd/Even Defense Wave, Even Resistance Wave
noStaffCs = ["Attack Smoke", "Speed Smoke", "Defense Smoke", "Resistance Smoke"]
infantryCs = ["Infantry Pulse", "Infantry Rush"]
armoredCs = ["Hone Armor", "Fortify Armor", "Goad Armor", "Ward Armor", "Armor March"]
cavalryCs = ["Hone Cavalry", "Fortify Cavalry", "Goad Cavalry", "Ward Cavalry"]
flierCs = ["Hone Fliers", "Fortify Fliers", "Goad Fliers", "Ward Fliers", "Guidance", "Flier Guidance"]
exclusiveCs = ["Ostia's Pulse"]
dragonCs = ["Hone Dragons", "Fortify Dragons", "Goad Dragons", "Ward Dragons", "Dragon Valor"]
axeCs = ["Axe Experience", "Axe Valor"]
blueTomeCs = ["Blue Tome Experience", "Blue Tome Valor"]
bowCs = ["Bow Experience", "Bow Valor"]
daggerCs = ["Dagger Valor"]
#Dagger Experience
greenTomeCs = ["Green Tome Valor", "Green Tome Experience"]
lanceCs = ["Lance Valor"]
#Lance Experience
redTomeCs = ["Red Tome Experience", "Red Tome Valor"]
swordCs = ["Sword Experience", "Sword Valor"]
staffCs = ["Staff Valor"]
#Staff Experience

normalSeals = ["HP +5", "Attack +3", "Speed +3", "Defense +3", "Resistance +3", "Attack/Defense +2", "HP/Resistance", "Attack Ploy", "Speed Ploy", "Defense Ploy", "Resistance Ploy", "Panic Ploy",  "Brash Assault", "Breath of Life", "Close Defense", "Distant Defense", "Deflect Magic", "Deflect Missile", "Drive Attack", "Drive Defense", "Hone Attack", "Hone Speed", "Fortify Defense", "Fortify Resistance", "Fortress Defense", "Fortress Resistance", "Hardy Bearing", "Phantom Speed", "Quick Riposte", "Quickened Pulse", "Savage Blow", "Spur Attack", "Spur Speed", "Spur Defense", "Spur Resistance", "Threaten Attack", "Threaten Speed", "Obstruct", "Defense Tactic", "Resistance Tactic", "Initiate Seal Attack", "Initiate Seal Defense", "Initiate Seal HP", "Initiate Seal Resistance", "Initiate Seal Speed", "Squad Ace A", "Squad Ace B", "Squad Ace C", "Squad Ace D", "Squad Ace E", "Squad Ace F", "Squad Ace G", "Squad Ace H", "Squad Ace I", "Squad Ace J", "Squad Ace K", "Squad Ace L"]
noStaffSeals = ["Attack Smoke", "Speed Smoke", "Heavy Blade", "Poison Strike", "Seal Attack", "Seal Speed"]
staffSeals = ["Live to Serve"]
singDanceSeals = ["Earth Dance"]
meleeSeals = ["Deflect Melee"]
flierSeals = ["Guidance", "Iote's Shield", "Flier Formation"]
armoredSeals = ["Armored Boots"]
infantryArmoredNoStaffSs = ["Flashing Blade"]
exclusiveSeals = ["Embla's Ward", "Múspellflame"]

growthValues = {1: 10, 2: 13, 3: 15, 4: 17, 5: 19, 6: 22, 7: 24, 8: 26, 9: 28, 10: 30, 11: 33, 12: 35}
#1: 10, 2-5: 2x+9, 6-10: 2x+10, 11-12: 2x+11

def randList(list):
    return list[randint(0, len(list) - 1)]

class Hero:
    def __init__(self, weaponType, movementType, name):
        self.weaponType = weaponType
        self.movementType = movementType
        self.name = name
        if self.name == "":
            self.customName = False
        else:
            self.customName = True
        self.experience = ""
        if self.weaponType in {"Sword", "Fire", "Dark", "Red Breath", "Red Bow"}:
            self.color = "Red"
        elif self.weaponType in {"Axe", "Wind", "Green Breath", "Green Bow"}:
            self.color = "Green"
        elif self.weaponType in {"Lance", "Thunder", "Light", "Blue Breath", "Blue Bow"}:
            self.color = "Blue"
        elif self.weaponType in {"Colorless Bow", "Dagger", "Staff", "Colorless Breath"}:
            self.color = "Colorless"

        if self.weaponType in {"Red Breath", "Green Breath", "Blue Breath", "Colorless Breath"}:
            self.dragon = True
            self.bow = False
        elif self.weaponType in {"Colorless Bow", "Red Bow", "Green Bow", "Blue Bow"}:
            self.dragon = False
            self.bow = True
        else:
            self.dragon = False
            self.bow = False
        if self.weaponType in {"Sword", "Axe", "Lance", "Colorless Bow", "Dagger", "Red Bow", "Green Bow", "Blue Bow"}:
            self.physical = True
        elif self.weaponType in {"Fire", "Wind", "Thunder", "Dark", "Light", "Staff", "Red Breath", "Green Breath", "Blue Breath", "Colorless Breath"}:
            self.physical = False
        if self.weaponType in {"Sword", "Axe", "Lance", "Red Breath", "Green Breath", "Blue Breath", "Colorless Breath"}:
            self.melee = True
        elif self.weaponType in {"Colorless Bow", "Dagger", "Fire", "Wind", "Thunder", "Dark", "Light", "Staff", "Red Bow", "Green Bow", "Blue Bow"}:
            self.melee = False

        #Weapon
        self.weapon = randList(weapons[self.weaponType].keys())

        #Assist
        if self.weaponType == "Staff":
            self.assists = heals[:]
        else:
            self.assists = assists[:]
        self.assist = randList(self.assists)

        #Special
        if self.weaponType == "Staff":
            self.specials = healSpecials[:]
        else:
            self.specials = normalSpecials[:]
            if self.melee:
                self.specials.extend(meleeSpecials)
                if self.physical:
                    self.specials.extend(physicalMeleeSpecials)
        self.special = randList(self.specials)

        #A Skill
        self.As = normalAs[:]
        if self.weaponType != "Staff":
            self.As.extend(noStaffAs)
            if self.color != "Colorless":
                self.As.extend(noColorlessAs)
            if self.movementType == "Infantry" or self.movementType == "Armored":
                self.As.extend(infantryArmoredNoStaffAs)
        if self.melee:
            self.As.extend(meleeAs)
            if self.movementType == "Infantry" or self.movementType == "Armored":
                self.As.extend(meleeInfantryArmoredAs)
        elif not self.melee:
            self.As.extend(rangedAs)
        if self.movementType == "Cavalry":
            self.As.extend(cavalryAs)
        elif self.movementType == "Armored":
            self.As.extend(armoredAs)
        elif self.movementType == "Flier":
            self.As.extend(flierAs)
        self.A = randList(self.As)

        #B Skill
        self.Bs = normalBs[:]
        if self.weaponType == "Staff":
            self.Bs.extend(staffBs)
        else:
            self.Bs.extend(noStaffBs)
            if self.melee:
                self.Bs.extend(meleeBs)
                self.Bs.extend(noTomeNoStaffBs)
                if self.movementType == "Infantry" or self.movementType == "Armored":
                    self.Bs.extend(meleeInfantryArmoredBs)
            elif not self.melee:
                if self.physical:
                    self.Bs.extend(noTomeNoStaffBs)
        if self.movementType == "Flier":
            self.Bs.extend(flierBs)
            self.Bs.extend(noArmoredBs)
        else:
            self.Bs.extend(noFlierBs)
            if self.movementType == "Armored":
                self.Bs.extend(armoredBs)
            else:
                self.Bs.extend(noArmoredBs)
        if self.color != "Red":
            self.Bs.extend(noRedBs)
        if self.color != "Green":
            self.Bs.extend(noGreenBs)
        if self.color != "Blue":
            self.Bs.extend(noBlueBs)
        if self.assist == "Dance" or self.assist == "Sing":
            self.Bs.extend(singDanceBs)
        self.B = randList(self.Bs)

        #C Skill
        self.Cs = normalCs[:]
        self.weaponCs = {"Sword": swordCs, "Axe": axeCs, "Lance": lanceCs, "Dagger": daggerCs, "Fire": redTomeCs, "Wind": greenTomeCs, "Thunder": blueTomeCs, "Dark": redTomeCs, "Light": blueTomeCs, "Staff": staffCs}
        self.movementCs = {"Infantry": infantryCs, "Cavalry": cavalryCs, "Armored": armoredCs, "Flier": flierCs}
        if self.weaponType != "Staff":
            self.Cs.extend(noStaffCs)
        if self.dragon:
            self.Cs.extend(dragonCs)
        elif self.bow:
            self.Cs.extend(bowCs)
        else:
            self.Cs.extend(self.weaponCs[weaponType])
        self.Cs.extend(self.movementCs[movementType])
        self.C = randList(self.Cs)

        #Sacred Seal
        self.seals = normalSeals[:]
        if self.weaponType != "Staff":
            self.seals.extend(noStaffSeals)
            if self.movementType == "Infantry" or self.movementType == "Armored":
                self.seals.extend(infantryArmoredNoStaffSs)
            if self.melee:
                self.seals.extend(meleeSeals)
        else:
            self.seals.extend(staffSeals)
        if self.movementType == "Flier":
            self.seals.extend(flierSeals)
        elif self.movementType == "Armored":
            self.seals.extend(armoredSeals)
        if self.assist == "Dance" or self.assist == "Sing":
            self.Ss.extend(singDanceSeals)
        self.S = randList(self.seals)

        #neutral IVs for now
        #47 - 1 for each stat
        self.BST = 42
        #31 - 1 for each stat
        self.GP = 26
        if self.assist == "Dance" or self.assist == "Sing":
            self.BST -= 8
        if not self.melee:
            self.BST -= 3
            self.GP -= 3
        if self.movementType == "Cavalry":
            self.BST -= 1
            self.GP -= 1
        elif self.movementType == "Armored":
            self.BST += 7
            self.GP += 2
        if self.experience == "Trainee":
            self.BST -= 8
            self.GP += 6
        elif self.experience == "Veteran":
            self.BST += 8
            self.GP -= 6

        self.OGBST = self.BST + 5
        self.OGGP = self.GP + 5

        self.baseStats = [1, 1, 1, 1, 1]
        self.statGrowths = [1, 1, 1, 1, 1]

        for i in range(self.BST):
            self.baseStat = randint(1, 5) - 1
            self.baseStats[self.baseStat] += 1

        for j in range(self.GP):
            while True:
                self.statGrowth = randint(1, 5) - 1
                if self.statGrowths[self.statGrowth] < 12:
                    self.statGrowths[self.statGrowth] += 1
                    break

    def effectiveness(self):
        self.effective = set()
        if self.weapon in bows or self.weapon in exclusiveBows or self.weapon == "Excalibur":
            self.effective.add("Flier")
        elif (self.weapon.startswith("Keen") and self.weapon.endswith("wolf")) or self.weapon in {"Zanbato", "Poleaxe", "Ridersbane"}:
            self.effective.add("Calvary")
        elif self.weapon in {"Armorsmasher", "Slaying Hammer", "Slaying Spear", "Dauntless Lance"}:
            self.effective.add("Armored")
        elif self.weapon in {"Falchion", "Naga", "Divine Naga", "Sealed Falchion", "Breath of Fog", "Summer Breath"}:
            self.effective.add("Dragon")
        elif self.weapon == "Poison Dagger":
            self.effective.add("Infantry")
        elif self.weapon == "Kitty Paddle":
            self.effective.add("Mage")
        elif self.weapon in {"Thani", "Wing Sword", "Rhomphaia"}:
            self.effective.add("Calvary")
            self.effective.add("Armored")
        elif self.weapon == "Warrior Princess":
            self.effective.add("Flier")
            self.effective.add("Armored")

    def calcStats(self):
        self.stats = []
        for i in range(5):
            self.stats.append(self.baseStats[i] + growthValues[self.statGrowths[i]])

    def statBonuses(self):
        #Adds weapon MT
        self.statAdd = [0, 0, 0, 0, 0, 0]
        self.MT = weapons[self.weaponType][self.weapon]
        self.statAdd[Atk] += self.MT

        if self.weapon in {"Brave Sword", "Brave Axe", "Brave Lance", "Brave Bow", "Dire Thunder", "Meisterschwert"}:
            self.statAdd[Spd] -= 5
        elif self.weapon == "Amiti":
            self.statAdd[Spd] -= 2
        elif self.weapon in {"Blazing Durandal", "Great Flame", "Laevatein", "Resolute Blade", "Flame Siegmund", "Nifl Frostflowers"}:
            self.statAdd[Atk] += 3
        elif self.weapon in {"Arya's Blade", "Mulagir", "Weirding Tome", "Skadi", "Níu", "Warrior Princess", "Múspell Fireposy", "Giga Excalibur", "Fruit of Iðunn"}:
            self.statAdd[Spd] += 3
        elif self.weapon in {"Geirskögul", "Ivaldi", "Sinmara", "Beloved Zofia", "Thunder Armads", "Summer Breath", "Wolf Berg"}:
            self.statAdd[Def] += 3
        elif self.weapon in {"Blizzard", "Divine Tyrfing", "Gleipnir", "Thani", "Grima's Truth", "Swift Mulagir", "Loptous"}:
            self.statAdd[Res] += 3
        elif self.weapon == "Audhulma":
            self.statAdd[Res] += 5
        elif self.weapon == "Cursed Lance":
            self.statAdd[Atk] += 2
            self.statAdd[Spd] += 2

        if self.A == "HP +5":
            self.statAdd[HP] += 5
        elif self.A == "Attack +3":
            self.statAdd[Atk] += 3
        elif self.A == "Speed +3":
            self.statAdd[Spd] += 3
        elif self.A == "Defense +3":
            self.statAdd[Def] += 3
        elif self.A == "Resistance +3":
            self.statAdd[Res] += 3
        elif self.A == "HP/Attack":
            self.statAdd[HP] += 4
            self.statAdd[Atk] += 2
        elif self.A == "HP/Speed":
            self.statAdd[HP] += 4
            self.statAdd[Spd] += 2
        elif self.A == "HP/Defense":
            self.statAdd[HP] += 4
            self.statAdd[Def] += 2
        elif self.A == "HP/Resistance":
            self.statAdd[HP] += 4
            self.statAdd[Res] += 2
        elif self.A == "Attack/Speed +2":
            self.statAdd[Atk] += 2
            self.statAdd[Spd] += 2
        elif self.A == "Attack/Defense +2":
            self.statAdd[Atk] += 2
            self.statAdd[Def] += 2
        elif self.A == "Attack/Resistance +2":
            self.statAdd[Atk] += 2
            self.statAdd[Res] += 2
        elif self.A == "Speed/Defense +2":
            self.statAdd[Spd] += 2
            self.statAdd[Def] += 2
        elif self.A == "Speed/Resistance +2":
            self.statAdd[Spd] += 2
            self.statAdd[Res] += 2
        elif self.A == "Fortress Defense":
            self.statAdd[Def] += 5
            self.statAdd[Atk] -= 3
        elif self.A == "Fortress Resistance":
            self.statAdd[Res] += 5
            self.statAdd[Atk] -= 3
        elif self.A == "Fury":
            self.statAdd[Atk] += 3
            self.statAdd[Spd] += 3
            self.statAdd[Def] += 3
            self.statAdd[Res] += 3
        elif self.A == "Life and Death":
            self.statAdd[Atk] += 5
            self.statAdd[Spd] += 5
            self.statAdd[Def] -= 5
            self.statAdd[Res] -= 5

        if self.S in {"HP +5", "Initiate Seal HP", "Squad Ace A", "Squad Ace F", "Squad Ace K"}:
            self.statAdd[HP] += 5
        elif self.S in {"Attack +3", "Initiate Seal Attack", "Squad Ace E", "Squad Ace J"}:
            self.statAdd[Atk] += 3
        elif self.S in {"Speed +3", "Initiate Seal Speed", "Squad Ace D", "Squad Ace I"}:
            self.statAdd[Spd] += 3
        elif self.S in {"Defense +3", "Initiate Seal Defense", "Squad Ace B", "Squad Ace G", "Squad Ace L"}:
            self.statAdd[Def] += 3
        elif self.S in {"Resistance +3", "Initiate Seal Resistance", "Squad Ace C", "Squad Ace H"}:
            self.statAdd[Res] += 3
        elif self.S == "Fortress Defense":
            self.statAdd[Def] += 5
            self.statAdd[Atk] -= 3
        elif self.S == "Fortress Resistance":
            self.statAdd[Res] += 5
            self.statAdd[Atk] -= 3
        elif self.S == "Attack/Defense +2":
            self.statAdd[Atk] += 2
            self.statAdd[Def] += 2
        elif self.S == "HP/Resistance":
            self.statAdd[HP] += 4
            self.statAdd[Res] += 2

    def Name(self):
        if not self.customName:
            self.name = ""
            if self.weaponType in {"Sword", "Axe", "Lance"}:
                self.name += self.weaponType + " " + {"Infantry": "Fighter", "Armored": "Knight", "Cavalry": "Cavalier", "Flier": "Flier"}[self.movementType]
            else:
                if self.movementType == "Armored":
                    self.name += self.movementType + " "
                elif self.movementType == "Flier":
                    self.name += "Flying "
                elif self.movementType == "Cavalry":
                    self.name += "Horseback "
                if self.dragon:
                    self.name += self.color + " Dragon"
                elif self.weaponType == "Staff":
                    self.name += "Cleric"
                    if self.movementType == "Cavalry":
                        self.name = "Troubadour"
                elif self.weaponType == "Dagger":
                    self.name += "Thief"
                elif not self.physical:
                    self.name += self.weaponType + " Mage"
                    if self.movementType == "Cavalry":
                        self.name = self.name.replace("Horseback ", "") + " Cavalier"
                elif self.bow:
                    self.name += self.color + " Archer"
                    if self.movementType == "Cavalry":
                        self.name = self.color + " Bow Knight"

    def Cooldown(self):
        if self.special == "Imbue" or self.special.endswith("Balm"):
            self.cooldown = 1
        elif self.special in {"Escutcheon", "Glimmer", "Heavenly Light", "Moonbow", "Noontime", "Reprisal", "Sacred Cowl", "Ice Mirror", "Regnal Astra"}:
            self.cooldown = 2
        elif self.special in {"Aegis", "Bonfire", "Draconic Aura", "Iceberg", "Luna", "Pavise", "Sol", "Vengeance", "Black Luna"}:
            self.cooldown = 3
        elif self.special in {"Astra", "Dragon Fang", "Ignis", "Glacies", "Radiant Aether"} or self.special.startswith("Blazing") or self.special.startswith("Growing"):
            self.cooldown = 4
        elif self.special in {"Aether", "Galeforce", "Miracle"}:
            self.cooldown = 5
        if self.weapon in {"Rauðrblade", "Gronnblade", "Blárblade", "Lightning Breath"}:
            self.cooldown += 1
        elif self.weapon in {"Slaying Edge", "Slaying Axe", "Slaying Lance", "Slaying Bow", "Hauteclere", "Mystletainn", "Cursed Lance", "Urvan", "Audhulma", "Basilikos", "Kagami Mochi", "Berserk Armads", "Nameless Blade", "Barb Shuriken", "Dark Mystletainn", "Mjölnir", "Vassal's Blade", "Dauntless Lance"}:
            self.cooldown -= 1
        self.special += " (Cooldown: %d)" % self.cooldown

    def counter(self):
        if self.A in {"Distant Counter", "Close Counter"} or self.weapon in {"Lightning Breath", "Raijinto", "Siegfried", "Gradivus", "Ragnell", "Alondite", "Stout Tomahawk", "Leiptr", "Expiration"}:
            self.allCounter = True
        else:
            self.allCounter = False

    def update(self):
        self.effectiveness()
        self.Name()
        self.calcStats()
        self.statBonuses()
        self.Cooldown()
        self.counter()
        self.movement = {"Infantry" : 2, "Cavalry": 3, "Flier": 2, "Armored": 1}[self.movementType]
        self.damage = {True: "Physical", False: "Magical"}[self.physical]
        self.distance = {True: "Melee", False: "Ranged"}[self.melee]

    def toString(self):
        self.update()
        self.skills = [self.weapon, self.assist, self.special, self.A, self.B, self.C, self.S]
        self.skillString = ["Weapon", "Assist", "Special", "A", "B", "C", "S"]
        self.statString = ["HP: ", "Atk:", "Spd:", "Def:", "Res:"]
        print self.name
        print
        print "Color:", self.color
        print "Movement:", self.movement
        print "Damage Type:", self.distance, self.damage
        print
        for i in range(len(self.skills)):
            print self.skillString[i] + ":", self.skills[i]
        print
        for i in range(len(self.stats)):
            print self.statString[i], self.stats[i], "\tBase:", self.baseStats[i], "\tGrowth:", self.statGrowths[i], "\tTotal:", self.stats[i] + self.statAdd[i], "(" + str(self.statAdd[i]) +  ")"
        if len(self.effective) > 0:
            print
            eff = ""
            for effect in self.effective:
                eff += effect + ", "
            eff = eff[:-2]
            print "Effective Against:", eff

def randHero(weap = "", move = "", name = ""):
    weaponType = randList(weaponTypes)
    movementType = randList(movementTypes)

    if weap in weaponTypes:
        weaponType = weap
    if move in movementTypes:
        movementType = move

    return Hero(weaponType, movementType, name)

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
