#coding: utf-8
from random import randint
from colorama import Fore, Back, Style, init

#for accessing stats in the list
HP = 0
Atk = 1
Spd = 2
Def = 3
Res = 4

weaponTypes = ["Sword", "Axe", "Lance", "Bow", "Fire", "Wind", "Thunder", "Staff", "Dagger", "Dark", "Light"]
movementTypes = ["Infantry", "Armored", "Cavalry", "Flier"]

swords = {"Silver Sword": 15, "Brave Sword": 8, "Slaying Edge": 14, "Wo Dao": 13, "Armorsmasher": 14, "Zanbato": 14, "Ruby Sword": 12, "Firesweep Sword": 15, "Safeguard": 14, "Barrier Blade": 14}
#Firesweep Axe
axes = {"Silver Axe": 15, "Brave Axe": 8, "Slaying Axe": 14, "Wo Gùn": 14, "Slaying Hammer": 14, "Poleaxe": 14, "Emerald Axe": 12, "Legion's Axe": 14}
lances = {"Silver Lance": 15, "Brave Lance": 8, "Slaying Lance": 14, "Harmonic Lance": 13, "Slaying Spear": 14, "Ridersbane": 14, "Sapphire Lance": 12, "Firesweep Lance": 15, "Reprisal Lance": 14, "Vanguard": 14, "Barrier Lance": 14, "Berkut's Lance": 14}
bows = {"Silver Bow": 13, "Brave Bow": 7, "Slaying Bow": 12, "Short Bow": 12, "Assassin's Bow": 11, "Guard Bow": 12, "Firesweep Bow": 11, "Shining Bow": 12, "Clarisse's Bow": 11}
daggers = {"Silver Dagger": 10, "Smoke Dagger": 9, "Poison Dagger": 5, "Rogue Dagger": 7, "Barb Shuriken": 12, "The Cleaner": 12}
fires = {"Bolganone": 13}
winds = {"Rexcalibur": 13, "Gronnblade": 13, "Keen Gronnwolf": 12, "Gronnraven": 11, "Gronnowl": 10, "Gronnserpent": 12}
thunders = {"Thoron": 13}
staffs = {"Absorb": 7, "Fear": 12, "Slow": 12, "Gravity": 10, "Pain": 10, "Panic": 11, "Trilemma": 12, "Flash": 11}
darks = {"Fenrir": 13}
lights = {"Shine": 13}
breaths = {"Flametongue": 15, "Light Breath": 13, "Dark Breath": 13, "Lightning Breath": 11, "Water Breath": 14}
#beasts = {"Adult": 9} (Flier), (Infantry), (Cavalry), (Armored)

reds = {"Rauðrblade": 13, "Keen Rauðrwolf": 12, "Rauðrraven": 11, "Rauðrowl": 10}
#Rauðrserpent
blues = {"Blárblade": 13, "Keen Blárwolf": 12, "Blárraven": 11, "Blárowl": 10, "Blárserpent": 12}

fires.update(reds)
darks.update(reds)
thunders.update(blues)
lights.update(blues)

seasonalSwords = {"Kadomatsu": 14, "Geishun": 14, "Heart's Blade": 14, "Cake Cutter": 14}
seasonalAxes = {"Carrot Axe": 13, "Melon Crusher": 14, "Lilith Floatie": 14, "Sack o' Gifts": 14, "Handbell": 14, "Hagoita": 14, "Giant Spoon": 13, "Ardent Service": 14, "Beach Banner": 14, "Hack-o'Lantern": 14, "Faithful Axe": 14}
seasonalLances = {"Carrot Lance": 13, "First Bite": 14, "Deft Harpoon": 14, "Tannenboom!": 14, "Casa Blanca": 14, "Shell Lance": 14, "Wagasa": 14, "Flashing Carrot": 14, "Luncheon Lance": 14, "Lofty Blossoms": 14}
seasonalBows = {"Cupid Arrow": 11, "Refreshing Bolt": 12, "Monstrous Bow": 12, "Hama Ya": 12, "Gratia": 12, "Cocobow": 12, "Fishie Bow": 12, "Devilish Bow": 12, "Kabura Ya": 12, "Beguiling Bow": 12, "Bouquet Bow": 12}
seasonalDaggers = {"Seashell": 10, "Dancer's Fan": 10, "Kitty Paddle": 8, "Kagami Mochi": 12, "Lethal Carrot": 12, "Starfish": 12, "Sky Maiougi": 12, "Cloud Maiougi": 12, "Dusk Uchiwa": 12, "Bottled Juice": 12, "Goodie Boot": 12, "Red Hot Ducks": 12, "Splashy Bucket": 12, "Ouch Pouch": 12, "Pegasus Carrot": 12}
seasonalFires = {}
seasonalWinds = {"Green Egg": 11, "Hibiscus Tome": 12, "Dancer's Ring": 12, "Spectral Tome": 12, "Green Gift": 12, "Gronnblooms": 12, "Sandwiches": 12}
seasonalThunders = {}
seasonalStaffs = {"Candlelight": 11, "Witchy Wand": 12, "Joyous Lantern": 12, "Kumade": 12, "Ovoid Staff": 12, "Toasty Skewer": 12}
seasonalDarks = {}
seasonalLights = {}
seasonalBreaths = {"Glittering Breath": 14}

seasonalReds = {"Tomato Tome": 12, "Candelabra": 12, "Loyal Wreath": 12}
#Rauðrblooms
seasonalBlues = {"Blue Egg": 11, "Blessed Bouquet": 12, "Sealife Tome": 12, "Dancer's Score": 12, "Blue Gift": 12, "Fresh Bouquet": 12, "Juicy Wave": 12, "Blárblooms": 12, "Vessel of Cheer": 12}

seasonalFires.update(seasonalReds)
seasonalDarks.update(seasonalReds)
seasonalThunders.update(seasonalBlues)
seasonalLights.update(seasonalBlues)

exclusiveSwords = {"Fólkvangr": 16, "Falchion": 16, "Ragnell": 16, "Raijinto": 16, "Alondite": 16, "Amiti": 11, "Durandal": 16, "Blazing Durandal": 16, "Audhulma": 16, "Arya's Blade": 16, "Binding Blade": 16, "Tyrfing": 16, "Divine Tyrfing": 16, "Dark Greatsword": 16, "Eckesachs": 16, "Laevatein": 16, "Mystletainn": 16, "Regal Blade": 16, "Resolute Blade": 16, "Siegfried": 16, "Sieglinde": 16, "Sol Katti": 16, "Yato": 16, "Wing Sword": 16, "Beloved Zofia": 16, "Níu": 16, "Sealed Falchion": 16, "Nameless Blade": 16, "Light Brand": 16, "Meisterschwert": 11, "Dark Mystletainn": 16, "Vassal's Blade": 16, "Skuld": 16, "Royal Sword": 16, "Exalted Falchion": 16, "Solitary Blade": 16, "Missiletainn": 16, "Storm Sieglinde": 16, "Golden Dagger": 16, "Gjöll": 16, "Gladiator's Blade": 16, "Scarlet Sword": 16, "Whitewing Blade": 16, "Sökkvabekkr": 16, "Hikami": 16, "Silverbrand": 16, "Hinata's Katana": 16, "Dragonbind": 16, "Hana's Katana": 16, "Bull Blade": 16, "Panther Sword": 16, "Shadow Sword": 16}
exclusiveAxes = {"Armads": 16, "Basilikos": 16, "Hauteclere": 16, "Nóatún": 16, "Sinmara": 16, "Stout Tomahawk": 16, "Urvan": 16, "Urðr": 16, "Berserk Armads": 16, "Camilla's Axe": 16, "Býleistr": 16, "Thunder Armads": 16, "Draconic Poleax": 16, "Wolf Berg": 16, "Garm": 16, "Cherche's Axe": 11, "Axe of Virility": 16, "Hel Scythe": 16, "Grado Poleax": 16, "Glitnir": 16, "Eldhrímnir": 16}
exclusiveLances = {"Fensalir": 16, "Leiptr": 16, "Siegmund": 16, "Gradivus": 16, "Cursed Lance": 16, "Geirskögul": 16, "Vidofnir": 16, "Bright Naginata": 16, "Hinoka's Spear": 16, "Flame Siegmund": 16, "Rhomphaia": 16, "Dauntless Lance": 16, "Maltet": 16, "Gáe Bolg": 16, "Shanna's Lance": 16, "Florina's Lance": 16, "Whitewing Lance": 16, "Whitewing Spear": 16, "Festive Siegmund": 16, "Oboro's Spear": 16, "Panther Lance": 16, "Bull Spear": 16, "Daybreak Lance": 16, "Kriemhild": 16, "Loyal Greatlance": 16}
exclusiveBows = {"Fujin Yumi": 14, "Mulagir": 14, "Nidhogg": 14, "Parthia": 14, "Skadi": 14, "Warrior Princess": 14, "Swift Mulagir": 14, "Thögn": 14, "Niles's Bow": 14, "Argent Bow": 8, "Luna Arc": 14, "Bow of Devotion": 14}
exclusiveDaggers = {"Deathly Dagger": 11, "Peshkatz": 14, "Felicia's Plate": 14, "Hoarfrost Knife": 14, "Sylgr": 14, "Lyfjaberg": 14, "Sæhrímnir": 14, "Saizo's Star": 14, "Kagero's Dart": 14}
exclusiveFires = {"Cymbeline": 14, "Valflame": 14, "Ragnarok": 14, "Forblaze": 14, "Múspell Fireposy": 14, "Fruit of Iðunn": 14, "Reese's Tome": 14, "Dawn Suzu": 14}
exclusiveWinds = {"Élivágar": 14, "Excalibur": 14, "Naga": 14, "Divine Naga": 14, "Dark Excalibur": 14, "Blizzard": 14, "Wind's Brand": 14, "Munnin's Egg": 14, "Thunderhead": 14, "Nifl Frostflowers": 14, "Giga Excalibur": 14, "Forseti": 14, "Book of Shadows": 14, "Tactical Gale": 14, "Ífingr": 14, "Iris's Tome": 14, "Chaos Manifest": 14, "Veðrfölnir's Egg": 14}
exclusiveThunders = {"Valaskjálf": 14, "Dire Thunder": 9, "Dark Aura": 14, "Weirding Tome": 14, "Huggin's Egg": 14, "Mjölnir": 14, "Odin's Grimoire": 14, "Missiletainn": 14, "Tactical Bolt": 14, "Tome of Thoron": 14, "Death": 14}
exclusiveStaffs = {"Thökk": 14, "Hliðskjálf": 14, "Gjallarbrú": 14}
exclusiveDarks = {"Brynhildr": 14, "Gleipnir": 14, "Naglfar": 14, "Grimoire": 14, "Grima's Truth": 14, "Loptous": 14, "Aversa's Night": 14, "Book of Dreams": 14, "Imhullu": 14, "Tharja's Hex": 14, "Eternal Tome": 14}
exclusiveLights = {"Aura": 14, "Thani": 14, "Ivaldi": 14, "Wargod's Tome": 14, "Sagittae": 14, "Prayer Wheel": 14}
exclusiveBreaths = {"Great Flame": 16, "Expiration": 16, "Breath of Fog": 16, "Summer Breath": 16, "Breath of Blight": 16, "Divine Mist": 16, "Spirit Breath": 16, "Draconic Rage": 16, "Fell Breath": 16, "Demonic Breath": 16, "Divine Breath": 16, "Savage Breath": 16, "Razing Breath": 16, "Oracle's Breath": 16}
exclusiveBeasts = {"Hawk King Claw": 14, "Heron Wing": 14, "Raven King Beak": 14, "Wolf Queen Fang": 14, "Wolfskin Fang": 9, "Kitsune Fang": 14, "Wolfpup Fang": 14, "Foxkit Fang": 14, "Taguel Fang": 14, "Lion King Fang": 14, "Sabertooth Fang": 14, "Covert Cat Fang": 14, "Brazen Cat Fang": 14, "Bunny Fang": 14}

weapons = {"Sword": swords, "Axe": axes, "Lance": lances, "Bow": bows, "Dagger": daggers, "Fire": fires, "Wind": winds, "Thunder": thunders, "Dark": darks, "Light": lights, "Staff": staffs}
seasonalWeapons = {"Sword": seasonalSwords, "Axe": seasonalAxes, "Lance": seasonalLances, "Bow": seasonalBows, "Dagger": seasonalDaggers, "Fire": seasonalFires, "Wind": seasonalWinds, "Thunder": seasonalThunders, "Dark": seasonalDarks, "Light": seasonalLights, "Staff": seasonalStaffs}
exclusiveWeapons = {"Sword": exclusiveSwords, "Axe": exclusiveAxes, "Lance": exclusiveLances, "Bow": exclusiveBows, "Dagger": exclusiveDaggers, "Fire": exclusiveFires, "Wind": exclusiveWinds, "Thunder": exclusiveThunders, "Dark": exclusiveDarks, "Light": exclusiveLights, "Staff": exclusiveStaffs}

assists = ["Swap", "Shove", "Smite", "Draw Back", "Reposition", "Pivot", "Reciprocal Aid", "Rally Attack/Speed", "Rally Attack/Defense", "Rally Attack/Resistance", "Rally Speed/Defense", "Rally Speed/Resistance", "Rally Defense/Resistance", "Rally Up Attack", "Rally Up Resistance", "Ardent Sacrifice", "Harsh Command"]
#Harsh Command, Rally Atk/Spd, Atk/Def, Spd/Def, and Res/Def are the + versions
#Rally Up Speed, Defense
heals = ["Physic", "Recover", "Martyr", "Rehabilitate", "Restore"]
exclusiveAssists = ["Dance", "Sing", "Sacrifice", "Future Vision", "Gray Waves"]

normalSpecials = ["Noontime", "Sol", "Moonbow", "Luna", "Aether", "Glimmer", "Astra", "Reprisal", "Vengeance", "Draconic Aura", "Dragon Fang", "Bonfire", "Ignis", "Blue Flame", "Iceberg", "Glacies", "Growing Flame", "Blazing Flame", "Growing Thunder", "Blazing Thunder", "Growing Wind", "Blazing Wind", "Growing Light", "Blazing Light", "Miracle"]
meleeSpecials = ["Escutcheon", "Pavise", "Sacred Cowl", "Aegis"]
physicalMeleeSpecials = ["Galeforce"]
healSpecials = ["Miracle", "Imbue", "Heavenly Light", "Windfire Balm", "Earthfire Balm", "Fireflood Balm", "Earthwater Balm"]
exclusiveSpecials = ["Black Luna", "Ice Mirror", "Radiant Aether", "Regnal Astra", "Fire Emblem", "Lunar Flash"]

#Fury/Death Blow/Darting Blow/Steady Stance/Warding Stance/Distant Defense/Flashing Blade are 4
normalAs = ["HP +5", "Attack +3", "Speed +3", "Defense +3", "Resistance +3", "HP/Attack", "HP/Speed", "HP/Defense", "HP/Resistance", "Attack/Speed +2", "Attack/Defense +2", "Attack/Resistance +2", "Speed/Defense +2", "Speed/Resistance +2", "Defense/Resistance +2", "Fortress Defense/Resistance", "Defiant Attack", "Defiant Speed", "Defiant Defense", "Defiant Resistance", "Brazen Attack/Speed", "Brazen Attack/Defense", "Brazen Attack/Resistance", "Brazen Defense/Resistance", "Close Defense", "Distant Defense", "Fire Boost", "Wind Boost", "Earth Boost", "Water Boost", "Attack/Speed Bond", "Attack/Defense Bond", "Attack/Resistance Bond", "Speed/Defense Bond", "Speed/Resistance Bond", "Defense/Resistance Bond", "Attack/Speed Push", "Attack/Defense Push", "Attack/Resistance Push", "Attack/Speed Solo", "Attack/Defense Solo", "Attack/Resistance Solo", "Speed/Defense Solo", "Defense/Resistance Solo"]
#Brazen Spd/Def, Brazen Spd/Res, Speed/Def Push, Speed/Res Push, Def/Res Push, Spd/Res Solo
noStaffAs = ["Fury", "Life and Death", "Death Blow", "Darting Blow", "Armored Blow", "Warding Blow", "Swift Sparrow", "Sturdy Blow", "Mirror Strike", "Steady Blow", "Swift Strike", "Bracing Blow", "Fierce Stance", "Darting Stance", "Steady Stance", "Warding Stance", "Kestrel Stance", "Sturdy Stance", "Mirror Stance", "Steady Posture", "Swift Stance", "Bracing Stance", "Heavy Blade"]
meleeAs = ["Distant Counter"]
rangedAs = ["Close Counter"]
infantryAs = ["Bonus Doubler"]
cavalryAs = ["Grani's Shield"]
flierAs = ["Iote's Shield"]
armoredAs = ["Svalinn Shield"]
noColorlessAs = ["Triangle Adept"]
infantryArmoredNoStaffAs = ["Flashing Blade"]
infantryFlierNoStaffAs = ["Sturdy Impact"]
meleeInfantryArmoredAs = ["Fierce Breath", "Steady Breath", "Warding Breath"]
infantryPhysicalNoBeastAs = ["Sorcery Blade"]
redFlierAs = ["Red Duel Flying"]
greenInfantryAs = ["Green Duel Infantry"]
greenFlierAs = ["Green Duel Flying"]
blueFlierAs = ["Blue Duel Flying"]
colorlessInfantryAs = ["Colorless Duel Infantry"]
aetherRaidAs = ["AR-O Attack/Speed", "AR-O Attack/Defense", "AR-D Attack/Resistance", "AR-D Speed/Defense", "AR-D Defense/Resistance"]
exclusiveAs = ["Dragonskin", "Laws of Sacae", "Ostian Counter"]

normalBs = ["Obstruct", "Wings of Mercy", "Escape Route", "Vantage", "Desperation", "Brash Assault", "Quick Riposte", "Renewal", "Chill Attack", "Chill Speed", "Chill Defense", "Chill Resistance", "Sabotage Attack", "Sabotage Resistance", "Daggerbreaker", "Guard", "Dull Ranged"]
#Sabotage Speed, Defense
meleeBs = ["Knock Back", "Lunge", "Drag Back", "Hit and Run", "Dull Close"]
staffBs = ["Live to Serve", "Wrathful Staff", "Dazzling Staff"]
noStaffBs = ["Poison Strike", "Seal Attack", "Seal Speed", "Seal Defense", "Seal Resistance", "Seal Attack/Speed", "Seal Attack/Defense", "Seal Speed/Defense", "Seal Defense/Resistance", "Windsweep", "Watersweep", "Attack/Speed Link", "Attack/Defense Link", "Attack/Resistance Link", "Speed/Defense Link", "Speed/Resistance Link", "Defense/Resistance Link", "Attack Feint", "Speed Feint", "Defense Feint", "Resistance Feint", "Mystic Boost"]
#Seal Atk/Res, Seal Spd/Res
noRedBs = ["Lancebreaker", "Blue Tomebreaker"]
noGreenBs = ["Swordbreaker", "Red Tomebreaker"]
noBlueBs = ["Axebreaker", "Green Tomebreaker"]
noFlierBs = ["Bowbreaker"]
infantryBs = ["Null Follow-Up", "Null C-Disrupt"]
flierBs = ["Flier Formation", "Aerobatics"]
armoredBs = ["Wary Fighter", "Bold Fighter", "Vengeful Fighter", "Special Fighter"]
noArmoredBs = ["Pass"]
noStaffNoColoredRangeBs = ["Cancel Affinity"]
infantryArmoredNoStaffBs = ["Special Spiral"]
infantryFlierBs = ["Sudden Panic"]
meleeInfantryArmoredBs = ["Shield Pulse", "Wrath"]
singDanceBs = ["Blaze Dance", "Gale Dance", "Earth Dance", "Torrent Dance", "Firestorm Dance", "Fireflood Dance", "Rockslide Dance", "Deluge Dance", "Geyser Dance"]
#Atk/Def Dance
daggerAetherRaidBs = ["Disarm Trap"]
uselessBs = ["Live for Honor", "Live for Bounty"]
exclusiveBs = ["Follow-Up Ring", "Recover Ring", "Beorc's Blessing", "Crusader's Ward", "Sacae's Blessing", "Warp Powder", "Chilling Seal", "Solar Brace", "S Drink", "Bushido", "Double Lion", "Binding Shield", "Lunar Brace", "Freezing Seal"]

#Hone Attack/Hone Speed are 4
normalCs = ["Breath of Life", "Savage Blow", "Spur Attack", "Spur Speed", "Spur Defense", "Spur Resistance", "Spur Attack/Speed", "Spur Attack/Defense", "Spur Attack/Resistance", "Spur Speed/Defense", "Spur Speed/Resistance", "Spur Defense/Resistance", "Drive Attack", "Drive Speed", "Drive Defense", "Drive Resistance", "Close Guard", "Distant Guard", "Hone Attack", "Hone Speed", "Fortify Defense", "Fortify Resistance", "Joint Hone Speed", "Attack Tactic", "Speed Tactic", "Defense Tactic", "Resistance Tactic", "Threaten Attack", "Threaten Speed", "Threaten Defense", "Threaten Resistance", "Attack Ploy", "Speed Ploy", "Defense Ploy", "Resistance Ploy", "Panic Ploy", "Odd Attack Wave", "Odd Speed Wave", "Odd Defense Wave", "Odd Resistance Wave", "Even Attack Wave", "Even Speed Wave", "Even Defense Wave", "Even Resistance Wave", "Attack Opening", "Speed Opening", "Defense Opening", "Resistance Opening"]
noStaffCs = ["Attack Smoke", "Speed Smoke", "Defense Smoke", "Resistance Smoke", "Pulse Smoke"]
infantryCs = ["Infantry Pulse", "Infantry Rush", "Infantry Flash", "Infantry Breath"]
armoredCs = ["Goad Armor", "Ward Armor", "Hone Armor", "Fortify Armor", "Armor March"]
cavalryCs = ["Goad Cavalry", "Ward Cavalry", "Hone Cavalry", "Fortify Cavalry"]
flierCs = ["Goad Fliers", "Ward Fliers", "Hone Fliers", "Fortify Fliers", "Guidance", "Flier Guidance", "Air Orders", "Ground Orders"]
dragonCs = ["Goad Dragons", "Ward Dragons", "Hone Dragons", "Fortify Dragons", "Dragon Valor"]
#Dragon Experience
beastCs = ["Goad Beasts", "Ward Beasts", "Hone Beast", "Fortify Beasts", "Beast Experience", "Beast Valor"]
#Beast Experience
axeCs = ["Axe Experience", "Axe Valor"]
blueTomeCs = ["Blue Tome Experience", "Blue Tome Valor"]
bowCs = ["Bow Experience", "Bow Valor"]
daggerCs = ["Dagger Valor"]
#Dagger Experience
greenTomeCs = ["Green Tome Experience", "Green Tome Valor"]
lanceCs = ["Lance Valor"]
#Lance Experience
redTomeCs = ["Red Tome Experience", "Red Tome Valor"]
swordCs = ["Sword Experience", "Sword Valor"]
staffCs = ["Staff Valor"]
#Staff Experience
exclusiveCs = ["Ostia's Pulse", "With Everyone!", "Surtr's Menace", "Sparkling Boost", "Glare", "Upheaval", "Human Virtue", "Chaos Named", "Solitary Dream", "Divine Fang"]

#NOTE: reorder to be like in-game order
normalSeals = ["HP +5", "Attack +3", "Speed +3", "Defense +3", "Resistance +3", "HP/Speed", "HP/Resistance", "Attack/Speed +2", "Attack/Defense +2", "Speed/Defense +2", "Speed/Resistance +2", "Fortress Defense", "Fortress Resistance", "Warding Stance", "Brazen Attack/Speed", "Brazen Attack/Defense", "Brazen Attack/Resistance", "Close Defense", "Distant Defense", "Fire Boost", "Wind Boost", "Water Boost", "Attack/Speed Bond", "Attack/Defense Bond", "Speed/Resistance Bond", "Obstruct", "Brash Assault", "Quick Riposte", "Renewal", "Chill Attack", "Breath of Life", "Savage Blow", "Spur Attack", "Spur Speed", "Spur Defense", "Spur Resistance", "Spur Defense/Resistance", "Drive Attack", "Drive Speed", "Drive Defense", "Drive Resistance", "Hone Attack", "Hone Speed", "Fortify Defense", "Fortify Resistance", "Defense Tactic", "Resistance Tactic", "Threaten Attack", "Threaten Speed", "Threaten Defense", "Threaten Resistance", "Attack Ploy", "Speed Ploy", "Defense Ploy", "Resistance Ploy", "Panic Ploy", "Even Defense Wave", "Even Resistance Wave", "Quickened Pulse", "Phantom Speed", "Hardy Bearing", "Deflect Missile", "Deflect Magic", "Initiate Seal HP", "Initiate Seal Attack", "Initiate Seal Speed", "Initiate Seal Defense", "Initiate Seal Resistance", "Squad Ace A", "Squad Ace B", "Squad Ace C", "Squad Ace D", "Squad Ace E", "Squad Ace F", "Squad Ace G", "Squad Ace H", "Squad Ace I", "Squad Ace J", "Squad Ace K", "Squad Ace L", "Squad Ace M", "Squad Ace N", "Squad Ace O", "Squad Ace P", "Squad Ace Q", "Squad Ace R", "Squad Ace S", "Squad Ace T", "Squad Ace U", "Squad Ace V", "Squad Ace W"]
noStaffSeals = ["Darting Blow", "Fierce Stance", "Darting Stance", "Heavy Blade", "Poison Strike", "Seal Attack", "Seal Speed", "Attack Smoke", "Speed Smoke"]
staffSeals = ["Live to Serve"]
singDanceSeals = ["Blaze Dance", "Gale Dance", "Earth Dance", "Torrent Dance"]
meleeSeals = ["Deflect Melee"]
flierSeals = ["Iote's Shield", "Flier Formation", "Aerobatics", "Guidance"]
armoredSeals = ["Armored Boots"]
infantryArmoredNoStaffSeals = ["Flashing Blade"]
exclusiveSeals = ["Embla's Ward", "Múspellflame"]

def randList(list):
    return list[randint(0, len(list) - 1)]

init(autoreset=True)
colors = {"Red": Back.RED, "Green": Back.GREEN, "Blue": Back.BLUE, "Colorless": Back.WHITE}

class Hero:
    def __init__(self, name, weaponType, movementType, weapon, assist, special, A, B, C, S):
        self.name = name
        if self.name in {"", "-"}:
            self.customName = False
        else:
            self.customName = True
        self.weaponType = weaponType
        self.movementType = movementType

        self.tempWeapon = weapon
        self.tempAssist = assist
        self.tempSpecial = special
        self.tempA = A
        self.tempB = B
        self.tempC = C
        self.tempS = S

        if self.tempAssist in {"Sing", "Dance", "Gray Waves"}:
            self.assist = self.tempAssist
            self.refresher = True
        else:
            self.refresher = False

        self.experience = ""
        if self.weaponType in {"Sword", "Fire", "Dark"}:
            self.color = "Red"
        elif self.weaponType in {"Axe", "Wind"}:
            self.color = "Green"
        elif self.weaponType in {"Lance", "Thunder", "Light"}:
            self.color = "Blue"
        elif self.weaponType in {"Bow", "Dagger", "Staff"}:
            self.color = "Colorless"

        self.bow = False
        self.dagger = False
        if self.weaponType in {"Bow"}:
            self.bow = True
        elif self.weaponType in {"Dagger"}:
            self.dagger = True

        if self.weaponType in {"Sword", "Axe", "Lance", "Bow", "Dagger"}:
            self.physical = True
        elif self.weaponType in {"Fire", "Wind", "Thunder", "Dark", "Light", "Staff"}:
            self.physical = False
        if self.weaponType in {"Sword", "Axe", "Lance"}:
            self.melee = True
        elif self.weaponType in {"Bow", "Dagger", "Fire", "Wind", "Thunder", "Dark", "Light", "Staff"}:
            self.melee = False

        #Weapon
        if self.tempWeapon in weapons[self.weaponType] or self.tempWeapon in seasonalWeapons[self.weaponType] or self.tempWeapon in exclusiveWeapons[self.weaponType]:
            self.weapon = self.tempWeapon
        else:
            self.weapon = "-"

        #Assist
        if self.weaponType == "Staff":
            self.assists = heals[:]
        else:
            self.assists = assists[:]
        if not self.refresher:
            if self.tempAssist in self.assists:
                self.assist = self.tempAssist
            else:
                self.assist = "-"

        #Special
        if self.weaponType == "Staff":
            self.specials = healSpecials[:]
        else:
            self.specials = normalSpecials[:]
            if self.melee:
                self.specials.extend(meleeSpecials)
                if self.physical:
                    self.specials.extend(physicalMeleeSpecials)
        if self.tempSpecial in self.specials:
            self.special = self.tempSpecial
        else:
            self.special = "-"

        #A Skill
        self.As = normalAs[:]
        if self.weaponType != "Staff":
            self.As.extend(noStaffAs)
            if self.color != "Colorless":
                self.As.extend(noColorlessAs)
            if self.movementType == "Infantry" or self.movementType == "Armored":
                self.As.extend(infantryArmoredNoStaffAs)
            if self.movementType == "Infantry" or self.movementType == "Flier":
                self.As.extend(infantryFlierNoStaffAs)
                self.As.remove("Armored Blow")
                self.As.remove("Sturdy Blow")
        if self.melee:
            self.As.extend(meleeAs)
            if self.movementType == "Infantry" or self.movementType == "Armored":
                self.As.extend(meleeInfantryArmoredAs)
        elif not self.melee:
            self.As.extend(rangedAs)
        if self.movementType == "Infantry":
            self.As.extend(infantryAs)
        elif self.movementType == "Cavalry":
            self.As.extend(cavalryAs)
        elif self.movementType == "Armored":
            self.As.extend(armoredAs)
        elif self.movementType == "Flier":
            self.As.extend(flierAs)
        if self.color == "Green" and self.movementType == "Infantry":
            self.As.extend(greenInfantryAs)
            self.As.remove("HP +5")
        elif self.color == "Colorless" and self.movementType == "Infantry":
            self.As.extend(colorlessInfantryAs)
            self.As.remove("HP +5")
        elif self.color == "Red" and self.movementType == "Flier":
            self.As.extend(redFlierAs)
            self.As.remove("HP +5")
        elif self.color == "Green" and self.movementType == "Flier":
            self.As.extend(greenFlierAs)
            self.As.remove("HP +5")
        elif self.color == "Blue" and self.movementType == "Flier":
            self.As.extend(blueFlierAs)
            self.As.remove("HP +5")
        if self.tempA in self.As:
            self.A = self.tempA
        else:
            self.A = "-"

        #B Skill
        self.Bs = normalBs[:]
        if self.weaponType == "Staff":
            self.Bs.extend(staffBs)
        else:
            self.Bs.extend(noStaffBs)
            if self.melee:
                self.Bs.extend(meleeBs)
                self.Bs.extend(noStaffNoColoredRangeBs)
                if self.movementType == "Infantry" or self.movementType == "Armored":
                    self.Bs.extend(meleeInfantryArmoredBs)
                    self.Bs.extend(infantryArmoredNoStaffBs)
            elif not self.melee:
                if self.movementType == "Infantry" or self.movementType == "Armored":
                    self.Bs.extend(infantryArmoredNoStaffBs)
                if self.physical and self.color == "Colorless":
                    self.Bs.extend(noStaffNoColoredRangeBs)
        if self.movementType == "Infantry":
            self.Bs.extend(infantryBs)
            self.Bs.extend(noFlierBs)
            self.Bs.extend(noArmoredBs)
            self.Bs.extend(infantryFlierBs)
        elif self.movementType == "Flier":
            self.Bs.extend(flierBs)
            self.Bs.extend(noArmoredBs)
            self.Bs.extend(infantryFlierBs)
        elif self.movementType == "Armored":
            self.Bs.extend(armoredBs)
            self.Bs.extend(noFlierBs)
        elif self.movementType == "Cavalry":
            self.Bs.extend(noArmoredBs)
            self.Bs.extend(noFlierBs)
        if self.color != "Red":
            self.Bs.extend(noRedBs)
        if self.color != "Green":
            self.Bs.extend(noGreenBs)
        if self.color != "Blue":
            self.Bs.extend(noBlueBs)
        if self.refresher:
            self.Bs.extend(singDanceBs)
        if self.tempB in self.Bs:
            self.B = self.tempB
        else:
            self.B = "-"

        #C Skill
        self.Cs = normalCs[:]
        self.weaponCs = {"Sword": swordCs, "Axe": axeCs, "Lance": lanceCs, "Fire": redTomeCs, "Wind": greenTomeCs, "Thunder": blueTomeCs, "Dark": redTomeCs, "Light": blueTomeCs, "Staff": staffCs}
        self.movementCs = {"Infantry": infantryCs, "Cavalry": cavalryCs, "Armored": armoredCs, "Flier": flierCs}
        if self.weaponType != "Staff":
            self.Cs.extend(noStaffCs)
        elif self.bow:
            self.Cs.extend(bowCs)
        elif self.dagger:
            self.Cs.extend(daggerCs)
        else:
            self.Cs.extend(self.weaponCs[weaponType])
        self.Cs.extend(self.movementCs[movementType])
        if self.tempC in self.Cs:
            self.C = self.tempC
        else:
            self.C = "-"

        #Sacred Seal
        self.seals = normalSeals[:]
        if self.weaponType != "Staff":
            self.seals.extend(noStaffSeals)
            if self.movementType == "Infantry" or self.movementType == "Armored":
                self.seals.extend(infantryArmoredNoStaffSeals)
            if self.melee:
                self.seals.extend(meleeSeals)
        else:
            self.seals.extend(staffSeals)
        if self.movementType == "Flier":
            self.seals.extend(flierSeals)
        elif self.movementType == "Armored":
            self.seals.extend(armoredSeals)
        if self.refresher:
            self.seals.extend(singDanceSeals)
        if self.tempS in self.seals:
            self.S = self.tempS
        else:
            self.S = "-"

    def effectiveness(self):
        self.effective = set()
        if self.weapon in bows or self.weapon in seasonalBows or self.weapon in exclusiveBows or self.weapon == "Excalibur":
            self.effective.add("Flier")
        elif (self.weapon.startswith("Keen") and self.weapon.endswith("wolf")) or self.weapon in {"Zanbato", "Poleaxe", "Ridersbane", "Dusk Uchiwa", "Taguel Fang", "Bunny Fang"}:
            self.effective.add("Calvary")
        elif self.weapon in {"Armorsmasher", "Slaying Hammer", "Slaying Spear", "Dauntless Lance", "Sky Maiougi", "Florina's Lance", "Axe of Virility", "Whitewing Spear", "Oboro's Spear", "Demonic Breath", "Hana's Katana"}:
            self.effective.add("Armored")
        elif self.weapon in {"Poison Dagger"}:
            self.effective.add("Infantry")
        elif self.weapon in {"Kitty Paddle"}:
            self.effective.add("Fire")
            self.effective.add("Wind")
            self.effective.add("Thunder")
            self.effective.add("Dark")
            self.effective.add("Light")
        elif self.weapon in {"Thani", "Wing Sword", "Rhomphaia", "Dawn Suzu"}:
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

        if self.weapon in {"Brave Sword", "Brave Axe", "Brave Lance", "Brave Bow", "Dire Thunder", "Meisterschwert", "Cherche's Axe", "Wolfskin Fang"}:
            self.statAdd[Spd] -= 5
        elif self.weapon in {"Amiti", "Argent Bow"}:
            self.statAdd[Spd] -= 2
        elif self.weapon in {"Blazing Durandal", "Great Flame", "Laevatein", "Resolute Blade", "Flame Siegmund", "Nifl Frostflowers", "Dawn Suzu", "Garm", "Storm Sieglinde", "Book of Dreams", "Gjöll", "Hawk King Claw", "Fell Breath", "Glitnir", "Divine Breath", "Lion King Fang", "Sæhrímnir", "Savage Breath", "Oracle's Breath"}:
            self.statAdd[Atk] += 3
        elif self.weapon in {"Arya's Blade", "Mulagir", "Weirding Tome", "Skadi", "Níu", "Warrior Princess", "Múspell Fireposy", "Giga Excalibur", "Fruit of Iðunn", "Thögn", "Royal Sword", "Exalted Falchion", "Forseti", "Book of Shadows", "Sylgr", "Hikami", "Prayer Wheel", "Heron Wing", "Raven King Beak", "Wolfpup Fang", "Luna Arc", "Veðrfölnir's Egg", "Brazen Cat Fang", "Eldhrímnir", "Bunny Fang"}:
            self.statAdd[Spd] += 3
        elif self.weapon in {"Geirskögul", "Ivaldi", "Sinmara", "Beloved Zofia", "Thunder Armads", "Summer Breath", "Wolf Berg", "Spirit Breath", "Sagittae", "Kitsune Fang", "Demonic Breath", "Sabertooth Fang", "Covert Cat Fang"}:
            self.statAdd[Def] += 3
        elif self.weapon in {"Blizzard", "Divine Tyrfing", "Gleipnir", "Thani", "Grima's Truth", "Swift Mulagir", "Loptous", "Aversa's Night", "Imhullu", "Lyfjaberg", "Foxkit Fang", "Chaos Manifest", "Death"}:
            self.statAdd[Res] += 3
        elif self.weapon == "Audhulma":
            self.statAdd[Res] += 5
        elif self.weapon == "Cursed Lance":
            self.statAdd[Atk] += 2
            self.statAdd[Spd] += 2

        if self.A in {"HP +5", "Green Duel Infantry", "Colorless Duel Infantry", "Red Duel Flying", "Green Duel Flying", "Blue Duel Infantry"}:
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
        elif self.A == "Defense/Resistance +2":
            self.statAdd[Def] += 2
            self.statAdd[Res] += 2
        elif self.A == "Fury":
            self.statAdd[Atk] += 4
            self.statAdd[Spd] += 4
            self.statAdd[Def] += 4
            self.statAdd[Res] += 4
        elif self.A == "Life and Death":
            self.statAdd[Atk] += 5
            self.statAdd[Spd] += 5
            self.statAdd[Def] -= 5
            self.statAdd[Res] -= 5
        elif self.A == "Fortress Defense/Resistance":
            self.statAdd[Def] += 6
            self.statAdd[Res] += 6
            self.statAdd[Atk] -= 2

        if self.S in {"HP +5", "Initiate Seal HP", "Squad Ace A", "Squad Ace F", "Squad Ace K", "Squad Ace P", "Squad Ace U"}:
            self.statAdd[HP] += 5
        elif self.S in {"Attack +3", "Initiate Seal Attack", "Squad Ace E", "Squad Ace J", "Squad Ace O", "Squad Ace T"}:
            self.statAdd[Atk] += 3
        elif self.S in {"Speed +3", "Initiate Seal Speed", "Squad Ace D", "Squad Ace I", "Squad Ace N", "Squad Ace S"}:
            self.statAdd[Spd] += 3
        elif self.S in {"Defense +3", "Initiate Seal Defense", "Squad Ace B", "Squad Ace G", "Squad Ace L", "Squad Ace Q", "Squad Ace V"}:
            self.statAdd[Def] += 3
        elif self.S in {"Resistance +3", "Initiate Seal Resistance", "Squad Ace C", "Squad Ace H", "Squad Ace M", "Squad Ace R", "Squad Ace W"}:
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
        elif self.S == "Speed/Defense +2":
            self.statAdd[Spd] += 2
            self.statAdd[Def] += 2
        elif self.S == "Speed/Resistance +2":
            self.statAdd[Spd] += 2
            self.statAdd[Res] += 2
        elif self.S == "HP/Speed":
            self.statAdd[HP] += 4
            self.statAdd[Spd] += 2
        elif self.S == "HP/Resistance":
            self.statAdd[HP] += 4
            self.statAdd[Res] += 2

    def Cooldown(self):
        if self.special == "Imbue" or self.special.endswith("Balm"):
            self.cooldown = 1
        elif self.special in {"Escutcheon", "Glimmer", "Heavenly Light", "Moonbow", "Noontime", "Reprisal", "Sacred Cowl", "Ice Mirror", "Regnal Astra", "Fire Emblem", "Lunar Flash"}:
            self.cooldown = 2
        elif self.special in {"Aegis", "Bonfire", "Draconic Aura", "Iceberg", "Luna", "Pavise", "Sol", "Vengeance", "Black Luna", "Blue Flame"}:
            self.cooldown = 3
        elif self.special in {"Astra", "Dragon Fang", "Ignis", "Glacies", "Radiant Aether"} or self.special.startswith("Growing") or self.special.startswith("Blazing"):
            self.cooldown = 4
        elif self.special in {"Aether", "Galeforce", "Miracle"}:
            self.cooldown = 5
        if self.weapon in {"Slaying Edge", "Slaying Axe", "Slaying Lance", "Slaying Bow", "Hauteclere", "Mystletainn", "Cursed Lance", "Urvan", "Audhulma", "Basilikos", "Kagami Mochi", "Berserk Armads", "Nameless Blade", "Barb Shuriken", "Dark Mystletainn", "Mjölnir", "Vassal's Blade", "Dauntless Lance", "Maltet", "Hoarfrost Knife", "Missiletainn", "Solitary Blade", "Shanna's Lance", "Golden Dagger", "Draconic Rage", "Scarlet Sword", "Whitewing Lance", "Festive Siegmund", "Hel Scythe", "Wolf Queen Fang", "Grado Poleax", "Niles's Bow", "Daybreak Lance", "Shadow Sword", "Loyal Greatlance"}:
            self.cooldown -= 1
        elif self.weapon in {"Rauðrblade", "Gronnblade", "Blárblade", "Lightning Breath"}:
            self.cooldown += 1
        if self.B == "Lunar Brace":
            self.cooldown += 1

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
                elif self.weaponType == "Staff":
                    self.name += "Cleric"
                    if self.movementType == "Cavalry":
                        self.name = "Troubadour"
                elif self.dagger:
                    self.name += self.color + " Thief"
                elif not self.physical:
                    self.name += self.weaponType + " Mage"
                    if self.movementType == "Cavalry":
                        self.name = self.name.replace("Horseback ", "") + " Cavalier"
                elif self.bow:
                    self.name += self.color + " Archer"
                    if self.movementType == "Cavalry":
                        self.name = self.color + " Bow Knight"

    def counter(self):
        if self.A in {"Distant Counter", "Close Counter", "Ostian Counter"} or self.weapon in {"Lightning Breath", "Raijinto", "Siegfried", "Gradivus", "Ragnell", "Alondite", "Stout Tomahawk", "Leiptr", "Expiration", "Divine Mist", "Dragonbind"}:
            self.allCounter = True
        else:
            self.allCounter = False

    def update(self):
        self.effectiveness()
        self.Name()
        self.Cooldown()
        self.counter()
        self.movement = {"Infantry" : 2, "Cavalry": 3, "Flier": 2, "Armored": 1}[self.movementType]
        self.damage = {True: "Physical", False: "Magical"}[self.physical]
        self.distance = {True: "Melee", False: "Ranged"}[self.melee]

    def toString(self):
        self.update()
        self.skills = [self.weapon, self.assist, self.special, self.A, self.B, self.C, self.S]
        self.skillString = ["Weapon", "Assist", "Special", "A", "B", "C", "S"]
        print self.name
        print
        print "Color: " + colors[self.color] + Style.BRIGHT + self.color + Style.RESET_ALL
        print "Movement:", self.movement
        print "Damage Type:", self.distance, self.damage
        print
        for i in range(len(self.skills)):
            print self.skillString[i] + ":", self.skills[i]
        print
        if len(self.effective) > 0:
            print
            eff = ""
            for effect in self.effective:
                eff += effect + ", "
            eff = eff[:-2]
            print "Effective Against:", eff

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
