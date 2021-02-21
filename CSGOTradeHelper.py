from tkinter import *
import requests
import re
import json
import webbrowser

root = Tk()
root.geometry("700x350")
root.title("Trade Helper by AjaX")

mylabel = Label(root, text="Trade Helper by AjaX", font=("arial"))
mylabel.place(relx=0.35)

category = StringVar()
category.set("Category")
item = StringVar()
skin = StringVar()
wear = StringVar()
stattrak = StringVar()
wear.set("Wear")
stattrak.set("Non Stat-Trak")

empty = Label(root, text=" ")
empty.grid(row=0, column=0)
empty1 = Label(root, text=" ")
empty1.grid(row=1, column=0)

drop1 = OptionMenu(root, category, "Pistols", "Rifles", "SMGs", "Heavy", "Knives", "Gloves")
drop1.grid(row=2, column=0)

def show_items(*args):

    if category.get() == "Pistols":
        show_pistols()

    elif category.get() == "Rifles":
        show_rifles()

    elif category.get() == "SMGs":
        show_smgs()

    elif category.get() == "Heavy":
        show_heavy()

    elif category.get() == "Knives":
        show_knives()

    elif category.get() == "Gloves":
        show_gloves()

def show_pistols():
    item.set("Pistols")
    items = OptionMenu(root, item, "CZ75-Auto", "Desert Eagle", "Dual Berettas", "Five-SeveN", "Glock-18", "P2000", "P250", "R8 Revolver", "Tec-9", "USP-S")
    items.grid(row=2, column=1)

def show_rifles():
    item.set("Rifles")
    items = OptionMenu(root, item, "AK-47", "AUG", "AWP", "FAMAS", "G3SG1", "Galil AR", "M4A1-S", "M4A4", "SCAR-20", "SG 553", "SSG 08")
    items.grid(row=2, column=1)

def show_smgs():
    item.set("SMGs")
    items = OptionMenu(root, item, "MAC-10", "MP5-SD", "MP7", "MP9", "PP-Bizon", "P90", "UMP-45")
    items.grid(row=2, column=1)

def show_heavy():
    item.set("Heavy")
    items = OptionMenu(root, item, "MAG-7", "Nova", "Sawed-off", "XM1014")
    items.grid(row=2, column=1)

def show_knives():
    item.set("Knives")
    items = OptionMenu(root, item, "Bayonet", "Butterfly Knife", "Bowie Knife", "Flip Knife", "Karambit", "Gut Knife", "Falchion Knife", 
    "Huntsman Knife", "M9 Bayonet", "Navaja Knife", "Shadow Daggers", "Stiletto Knife", "Talon Knife", "Ursus Knife", "Classic Knife",
    "Paracord Knife", "Survival Knife", "Skeleton Knife", "Nomad Knife")
    items.grid(row=2, column=1)

def show_gloves():
    item.set("Gloves")
    items = OptionMenu(root, item, "Broken Fang Gloves", "Hydra Gloves", "Bloodhound Gloves", "Driver Gloves", "Hand Wraps",
    "Moto Gloves", "Specialist Gloves", "Sport Gloves")
    items.grid(row=2, column=1)


#PISTOLS
def show_skins(*args):
    
    skin.set("Skins")

    if item.get() == "CZ75-Auto":
        skins = OptionMenu(root, skin, "Army Sheen", "Chalice", "Crimson Web", "Distressed", "Eco", "Emerald", "Emerald Quartz", "Green Plaid", 
        "Hexane", "Imprint", "Indigo", "Jungle Dashed", "Nitro", "Poison Dart", "Pole Position", "Polymer", "Red Astor", "Silver", "Tacticat",
        "The Fuschia Is Now", "Tigris", "Tread Plate", "Tuxedo", "Twist", "Vendetta", "Victoria", "Xiangliu", "Yellow Jacket")
        skins.grid(row=2, column=2)

    elif item.get() == "Desert Eagle":
        skins = OptionMenu(root, skin, "Blaze", "Blue Ply", "Bronze Deco", "Cobalt Disruption", "Code Red", "Conspiracy", "Corinthian", 
        "Crimson Web", "Directive", "Emerald Jörmungandr", "Golden Koi", "Hand Cannon", "Heirloom", "Hypnotic", "Kumicho Dragon", "Light Rail",
        "Mecha Industries", "Meteorite", "Midnight Storm", "Mudder", "Naga", "Night", "Night Heist", "Oxide Blaze", "Pilot", "Printstream",
        "Sunset Storm 壱", "Sunset Storm 弐", "The Bronze", "Urban DDPAT", "Urban Rubble")
        skins.grid(row=2, column=2)

    elif item.get() == "Dual Berettas":
        skins = OptionMenu(root, skin, "Anodized Navy", "Balance", "Black Limba", "Briar", "Cartel", "Cobalt Quartz", "Cobra Strike", 
        "Colony", "Contractor", "Demolition", "Dezastre", "Dualing Dragons", "Duelist", "Elite 1.6", "Emerald", "Heist",
        "Hemoglobin", "Marina", "Moon in Libra", "Panther", "Pyre", "Retribution", "Royal Consorts", "Shred", "Stained", "Switch Board",
        "Twin Turbo", "Urban Shock", "Ventilators")
        skins.grid(row=2, column=2)

    elif item.get() == "Five-SeveN":
        skins = OptionMenu(root, skin, "Angry Mob", "Anodized Gunmetal", "Berries And Cherries", "Buddy", "Candy Apple", "Capillary", 
        "Case Hardened", "Contractor", "Coolant", "Copper Galaxy", "Crimson Blossom", "Fairy Tale", "Flame Test", "Forest Night", "Fowl Play", 
        "Hot Shot", "Hyper Beast", "Jungle", "Kami", "Monkey Business", "Neon Kimono", "Nightshade", "Nitro", "Orange Peel", "Retrobution", 
        "Scumbria", "Silver Quartz", "Triumvirate", "Urban Hazard", "Violent Daimyo")
        skins.grid(row=2, column=2)

    elif item.get() == "Glock-18":
        skins = OptionMenu(root, skin, "Blue Fissure", "Brass", "Bullet Queen", "Bunsen Burner", "Candy Apple", "Catacombs", 
        "Death Rattle", "Dragon Tattoo", "Fade", "Franklin", "Grinder", "Groundwater", "High Beam", "Ironwork", "Moonrise", 
        "Neo-Noir", "Night", "Nuclear Garden", "Off World", "Oxide Blaze", "Reactor", "Royal Legion", "Sacrifice", "Sand Dune", "Steel Disruption", 
        "Synth Leaf", "Twilight Galaxy", "Vogue", "Warhawk", "Wasteland Rebel", "Water Elemental", "Weasel", "Wraiths")
        skins.grid(row=2, column=2)

    elif item.get() == "P2000":
        skins = OptionMenu(root, skin, "Acid Etched", "Amber Fade", "Chainmail", "Coach Class", "Corticera", "Dispatch", 
        "Fire Elemental", "Gnarled", "Granite Marbleized", "Grassland", "Grassland Leaves", "Handgun", "Imperial", "Imperial Dragon", "Ivory", 
        "Obsidian", "Ocean Foam", "Oceanic", "Panther Camo", "Pathfinder", "Pulse", "Red FragCam", "Scorpion", "Silver", "Turf", 
        "Urban Hazard", "Woodsman")
        skins.grid(row=2, column=2)

    elif item.get() == "P250":
        skins = OptionMenu(root, skin, "Asiimov", "Bengal Tiger", "Bone Mask", "Boreal Forest", "Cartel", "Cassette", 
        "Contaminant", "Contamination", "Crimson Kimono", "Dark Filigree", "Exchanger", "Facets", "Facility Draft", "Forest Night", "Franklin", 
        "Gunsmoke", "Hive", "Inferno", "Iron Clad", "Mehndi", "Metallic DDPAT", "Mint Kimono", "Modern Hunter", "Muertos", "Nevermore", 
        "Nuclear Threat", "Red Rock", "Ripple", "Sand Dune", "See Ya Later", "Splash", "Steel Disruption", "Supernova", "Undertow", "Valence",
        "Verdigris", "Vino Primo", "Whiteout", "Wingshot", "X-Ray")
        skins.grid(row=2, column=2)

    elif item.get() == "R8 Revolver":
        skins = OptionMenu(root, skin, "Amber Fade", "Bone Forged", "Bone Mask", "Canal Spray", "Crimson Web", "Fade", 
        "Grip", "Llama Cannon", "Memento", "Night", "Nitro", "Phoenix Marker", "Reboot", "Skull Crusher", "Survivalist")
        skins.grid(row=2, column=2)

    elif item.get() == "Tec-9":
        skins = OptionMenu(root, skin, "Army Mesh", "Avalanche", "Bamboo Forest", "Bamboozle", "Blast From the Past", "Blue Titanium", "Brass", 
        "Brother", "Cracked Opal", "Cut Out", "Decimator", "Flash Out", "Fubar", "Fuel Injector", "Groundwater", "Hades",
        "Ice Cap", "Isaac", "Jambiya", "Nuclear Threat", "Orange Murano", "Ossified", "Phoenix Chalk", "Red Quartz", "Re-Entry", 
        "Remote Control", "Rust Leaf", "Sandstorm", "Snek-9", "Terrace", "Titanium Bit", "Tornado", "Toxic", "Urban DDPAT", "VariCamo")
        skins.grid(row=2, column=2)

    elif item.get() == "USP-S":
        skins = OptionMenu(root, skin, "Ancient Visions", "Blood Tiger", "Blueprint", "Business Class", "Caiman", "Check Engine", "Cortex", 
        "Cyrex", "Dark Water", "Flashback", "Forest Leaves", "Guardian", "Kill Confirmed", "Lead Conduit", "Monster Mashup", "Neo-Noir",
        "Night Ops", "Orion", "Overgrowth", "Para Green", "Pathfinder", "Road Rash", "Royal Blue", "Serum", "Stainless", 
        "Target Acquired", "Torque")
        skins.grid(row=2, column=2)


#RIFLES
    elif item.get() == "AK-47":
        skins = OptionMenu(root, skin, "Aquamarine Revenge", "Asiimov", "Baroque Purple", "Black Laminate", "Bloodsport", "Blue Laminate",
        "Cartel", "Case Hardened", "Elite Build", "Emerald Pinstripe", "Fire Serpent", "First Class", "Frontside Misty", "Fuel Injector", 
        "Hydroponic", "Jaguar", "Jet Set", "Jungle Spray", "Legion of Anubis", "Neon Revolution", "Neon Rider", "Orbit Mk01", "Panthera onca", 
        "Phantom Disruptor", "Point Disarray",  "Predator", "Rat Rod", "Red Laminate", "Redline", "Safari Mesh", "Safety Net", "The Empress",
        "Uncharted", "Vulcan", "Wasteland Rebel", "Wild Lotus", "X-Ray")
        skins.grid(row=2, column=2)

    elif item.get() == "AUG":
        skins = OptionMenu(root, skin, "Akihabara Accept", "Amber Slipstream", "Anodized Navy", "Arctic Wolf", "Aristocrat", "Bengal Tiger",
        "Carved Jade", "Chameleon", "Colony", "Condemned", "Contractor", "Copperhead", "Daedalus", "Death by Puppy", 
        "Flame Jörmungandr", "Fleet Flock", "Hot Rod", "Midnight Lily", "Momentum", "Navy Murano", "Radiation Hazard", "Random Access", 
        "Ricochet", "Storm", "Stymphalian",  "Surveillance", "Sweeper", "Syd Mead", "Tom Cat", "Torque", "Triqua", "Wings")
        skins.grid(row=2, column=2)

    elif item.get() == "AWP":
        skins = OptionMenu(root, skin, "Acheron", "Asiimov", "Atheris", "BOOM", "Capillary", "Containment Breach",
        "Corticera", "Dragon Lore", "Electric Hive", "Elite Build", "Exoskeleton", "Fade", "Fever Dream", "Graphite", 
        "Gungnir", "Hyper Beast", "Lightning Strike", "Man-o'-war", "Medusa", "Mortis", "Neo-Noir", "Oni Taiji", 
        "PAW", "Phobos", "Pink DDPAT",  "Pit Viper", "Redline", "Safari Mesh", "Silk Tiger", "Snake Camo", "Sun in Leo", "The Prince",
        "Wildfire", "Worm God")
        skins.grid(row=2, column=2)

    elif item.get() == "FAMAS":
        skins = OptionMenu(root, skin, "Afterimage", "Colony", "Commemoration", "Contrast Spray", "Crypsis", "Cyanospatter",
        "Dark Water", "Decommissioned", "Djinn", "Doomkitty", "Eye of Athena", "Hexane", "Macabre", "Mecha Industries", 
        "Neural Net", "Night Borre", "Prime Conspiracy", "Pulse", "Roll Cage", "Sergeant", "Spitfire", "Styx", 
        "Sundown", "Survivor Z", "Teardown",  "Valence")
        skins.grid(row=2, column=2)

    elif item.get() == "G3SG1":
        skins = OptionMenu(root, skin, "Ancient Ritual", "Arctic Camo", "Azure Zebra", "Black Sand", "Chronos", "Contractor",
        "Demeter", "Desert Storm", "Digital Mesh", "Flux", "Green Apple", "High Seas", "Hunter", "Jungle Dashed", 
        "Murky", "Orange Crash", "Orange Kimono", "Polar Camo", "Safari Mesh", "Scavenger", "Stinger", "The Executioner", 
        "VariCamo", "Ventilator", "Violet Murano")
        skins.grid(row=2, column=2)

    elif item.get() == "Galil AR":
        skins = OptionMenu(root, skin, "Akoben", "Aqua Terrace", "Black Sand" ,"Blue Titanium" ,"Cerberus" ,"Chatterbox", 
        "Cold Fusion", "Connexion", "Crimson Tsunami", "Dusk Ruins" ,"Eco", "Firefight", "Hunting Blind", "Kami", 
        "Orange DDPAT", "Phoenix Blacklight", "Rocket Pop", "Sage Spray", "Sandstorm", "Shattered" ,"Signal", "Stone Cold", 
        "Sugar Rush", "Tornado", "Tuxedo", "Urban Rubble", "Vandal", "VariCamo", "Winter Forest")
        skins.grid(row=2, column=2)

    elif item.get() == "M4A1-S":
        skins = OptionMenu(root, skin, "Atomic Alloy", "Basilisk", "Blood Tiger", "Blue Phosphor", "Boreal Forest", "Briefing", "Bright Water", "Chantico's Fire",
        "Control Panel", "Cyrex", "Dark Water", "Decimator", "Flashback", "Golden Coil", "Guardian", "Hot Rod", "Hyper Beast", "Icarus Fell",
        "Knight", "Leaded Glass", "Master Piece", "Mecha Industries", "Moss Quartz", "Nightmare", "Nitro", "Player Two", "Printstream", 
        "VariCamo", "Welcome to the Jungle")
        skins.grid(row=2, column=2)

    elif item.get() == "M4A4":
        skins = OptionMenu(root, skin, "Asiimov", "Bullet Rain", "Buzz Kill", "Converter", "Cyber Security", "Dark Blossom", "Daybreak", "Desert Storm",
        "Desert-Strike", "Desolate Space", "Evil Daimyo", "Faded Zebra", "Global Offensive", "Griffin", "Hellfire", 
        "Howl", "Jungle Tiger", "Magnesium", "Mainframe", "Modern Hunter", "Neo-Noir", "Poseidon", "Radiation Hazard", "Royal Paladin", 
        "The Battlestar", "The Emperor", "Tooth Fairy", "Tornado", "Urban DDPAT", "X-Ray", "Zirka", "龍王 (Dragon King)")
        skins.grid(row=2, column=2)

    elif item.get() == "SCAR-20":
        skins = OptionMenu(root, skin, "Army Sheen", "Assault", "Bloodsport", "Blueprint", "Brass", "Carbon Fiber", "Cardiac", "Contractor",
        "Crimson Web", "Cyrex", "Emerald", "Enforcer", "Green Marine", "Grotto", "Jungle Slipstream", "Magna Carta",
        "Outbreak", "Palm", "Powercore", "Sand Mesh", "Splash Jam", "Stone Mosaico", "Storm", "Torn")
        skins.grid(row=2, column=2)

    elif item.get() == "SG 553":

        skins = OptionMenu(root, skin, "Aerial", "Aloha", "Anodized Navy", "Army Sheen", "Atlas", "Barricade", "Bulldozer", "Candy Apple", "Colony IV",
        "Cyrex", "Damascus Steel", "Danger Close", "Darkwing", "Fallout Warning", "Gator Mesh", "Hypnotic", "Integrale",
        "Lush Ruins", "Ol' Rusty", "Phantom", "Pulse", "Tiger Moth", "Tornado", "Traveler", "Triarch", "Ultraviolet", "Waves Perforated",
        "Wave Spray")
        skins.grid(row=2, column=2)

    elif item.get() == "SSG 08":
        skins = OptionMenu(root, skin, "Abyss", "Acid Fade", "Big Iron", "Blood in the Water", "Bloodshot", "Blue Spruce", "Dark Water", "Death's Head",
        "Detour", "Dragonfire", "Fever Dream", "Ghost Crusader", "Hand Brake", "Jungle Dashed", "Lichen Dashed", "Mainframe 001",
        "Mayan Dreams", "Necropos", "Orange Filigree", "Parallax", "Red Stone", "Sand Dune", "Sea Calico", "Slashed", "Threat Detected", "Tropical Storm")
        skins.grid(row=2, column=2)


#SMGS
    elif item.get() == "MAC-10":
        skins = OptionMenu(root, skin, "Allure", "Aloha", "Amber Fade", "Calf Skin", "Candy Apple", "Carnivore", "Classic Crate", "Commuter",
        "Copper Borre", "Curse", "Disco Tech", "Fade", "Gold Brick", "Graven", "Heat", "Hot Snakes", "Indigo",
        "Lapis Gator", "Last Dive", "Malachite", "Neon Rider", "Nuclear Garden", "Oceanic", "Palm",
        "Pipe Down", "Rangeen", "Red Filigree", "Silver", "Stalker", "Surfwood", "Tatter", "Tornado", "Ultraviolet",
        "Urban DDPAT", "Whitefish")
        skins.grid(row=2, column=2)

    elif item.get() == "MP5-SD":
        skins = OptionMenu(root, skin, "Acid Wash", "Agent", "Bamboo Garden", "Condition Zero", "Co-Processor", "Desert Strike", "Dirt Drop",
        "Gauss", "Kitbash", "Lab Rats", "Nitro", "Phosphor")
        skins.grid(row=2, column=2)

    elif item.get() == "MP7":
        skins = OptionMenu(root, skin, "Whiteout", "Vault Heist", "Urban Hazard", "Teal Blossom", "Tall Grass", "Special Delivery", "Skulls", "Scorched",
        "Powercore", "Orange Peel", "Olive Plaid", "Ocean Foam", "Neon Ply", "Nemesis", "Motherboard", "Mischief", "Impire",
        "Gunsmoke", "Groundwater", "Full Stop", "Forest DDPAT", "Fade", "Cirrus", "Bloodsport", "Asterion", "Army Recon",
        "Armor Core", "Anodized Navy", "Akoben")
        skins.grid(row=2, column=2)

    elif item.get() == "MP9":
        skins = OptionMenu(root, skin, "Airlock", "Army Sheen", "Bioleak", "Black Sand", "Bulldozer", "Capillary", "Dark Age", "Dart",
        "Deadly Poison", "Dry Season", "Goo", "Green Plaid", "Hot Rod", "Hydra", "Hypnotic", "Modest Threat",
        "Orange Peel", "Pandora's Box", "Rose Iron", "Ruby Poison Dart", "Sand Dashed", "Sand Scale", "Setting Sun",
        "Slide", "Stained Glass", "Storm", "Wild Lily")
        skins.grid(row=2, column=2)

    elif item.get() == "PP-Bizon":
        skins = OptionMenu(root, skin, "Antique", "Bamboo Print", "Blue Streak",  "Brass", "Candy Apple", "Carbon Fibe", "Chemical Green", "Cobalt Halftone",
        "Death Rattler", "Embargo", "Facility Sketch", "Forest Leaves", "Fuel Rod", "Harvester", "High Roller", "Irradiated Alert",
        "Judgement of Anubis", "Jungle Slipstream", "Modern Hunter", "Night Ops", "Night Riot", "Osiris", "Photic Zone", "Runic",
        "Rust Coat", "Sand Dashed", "Seabird", "Urban Dashed", "Water Sigil")
        skins.grid(row=2, column=2)

    elif item.get() == "P90":
        skins = OptionMenu(root, skin, "Ancient Earth", "Ash Wood", "Asiimov", "Astral Jörmungandr", "Baroque Red", "Blind Spot", "Chopper",
        "Cocoa Rampage", "Cold Blooded", "Death by Kitty", "Death Grip", "Desert Warfare", "Elite Build",
        "Emerald Dragon", "Facility Negative", "Fallout Warning", "Freight", "Glacier Mesh", "Grim", "Leather",
        "Module", "Nostalgia", "Off World", "Run and Hide", "Sand Spray", "Scorched", "Shallow Grave", "Shapewood",
        "Storm", "Sunset Lily", "Teardown", "Tiger Pit", "Traction", "Trigon", "Virus")
        skins.grid(row=2, column=2)

    elif item.get() == "UMP-45":
        skins = OptionMenu(root, skin, "Arctic Wolf", "Blaze", "Bone Pile", "Briefing", "Caramel", "Carbon Fiber", "Corporal", "Crime Scene", "Day Lily", "Delusion",
        "Exposure", "Facility Dark", "Fallout Warning", "Gold Bismuth", "Grand Prix", "Gunsmoke", "Houndstooth",
        "Indigo", "Labyrinth", "Metal Flowers", "Minotaur's Labyrinth", "Momentum", "Moonrise", "Mudder", "Plastique",
        "Primal Saber", "Riot", "Scaffold", "Scorched", "Urban DDPAT")
        skins.grid(row=2, column=2)


#HEAVY
    elif item.get() == "MAG-7":
        skins = OptionMenu(root, skin, "Bulldozer", "Carbon Fiber", "Chainmail", "Cinquedea", "Cobalt Core", "Core Breach", "Counter Terrace",
        "Firestarter", "Hard Water", "Hazard", "Heat", "Heaven Guard", "Irradiated Alert", "Justice", "Memento",
        "Metallic DDPAT", "Monster Call", "Petroglyph", "Popdog", "Praetorian", "Rust Coat", "Sand Dune",
        "Seabird", "Silver", "Sonar", "Storm", "SWAG-7")
        skins.grid(row=2, column=2)

    elif item.get() == "Nova":
        skins = OptionMenu(root, skin, "Antique", "Army Sheen", "Baroque Orange", "Blaze Orange", "Bloomstick", "Caged Steel", "Candy Apple",
        "Clear Polymer", "Exo", "Forest Leaves", "Ghost Camo", "Gila", "Graphite", "Green Apple", "Hyper Beast",
        "Koi", "Mandrel", "Modern Hunter", "Moon in Libra", "Plume", "Polar Mesh", "Predator", "Ranger", "Rising Skull",
        "Rust Coat", "Sand Dune", "Tempest", "Toy Soldier", "Walnut", "Wild Six", "Wood Fired")
        skins.grid(row=2, column=2)

    elif item.get() == "Sawed-off":
        skins = OptionMenu(root, skin, "Amber Fade", "Apocalypto", "Bamboo Shadow", "Black Sand", "Brake Light", "Clay Ambush", "Copper", "Devourer",
        "First Class", "Forest DDPAT", "Fubar", "Full Stop", "Highwayman", "Irradiated Alert", "Jungle Thicket", "Limelight", 
        "Morris", "Mosaico", "Orange DDPAT", "Origami", "Rust Coat", "Sage Spray", "Serenity", "Snake Camo", "The Kraken",
        "Wasteland Princess", "Yorick", "Zander")
        skins.grid(row=2, column=2)

    elif item.get() == "XM1014":
        skins = OptionMenu(root, skin, "Ancient Lore", "Banana Leaf", "Black Tie", "Blaze Orange", "Blue Spruce", "Blue Steel", "Bone Machine",
        "CaliCamo", "Charter", "Entombed", "Fallout Warning", "Frost Borre", "Grassland", "Heaven Guard", "Incinegator",
        "Jungle", "Oxide Blaze", "Quicksilver", "Red Leather", "Red Python", "Scumbria", "Seasons", "Slipstream",
        "Teclu Burner", "Tranquility", "Urban Perforated", "VariCamo Blue", "Ziggy")
        skins.grid(row=2, column=2)


#KNIVES
    elif item.get() == "Bayonet":
        skins = OptionMenu(root, skin, "Vanilla", "Autotronic", "Black Laminate", "Blue Steel", "Boreal Forest", "Bright Water", 
        "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", "Fade", "Forest DDPAT", "Freehand", "Gamma Doppler", "Lore",
        "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Butterfly Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", 
        "Fade", "Forest DDPAT", "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", 
        "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Bowie Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", 
        "Fade", "Forest DDPAT", "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", 
        "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Flip Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Autotronic", "Black Laminate", "Blue Steel", "Boreal Forest", "Bright Water", 
        "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", "Fade", "Forest DDPAT", "Freehand", "Gamma Doppler", "Lore",
        "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() =="Karambit":
        skins = OptionMenu(root, skin, "Vanilla", "Autotronic", "Black Laminate", "Blue Steel", "Boreal Forest", "Bright Water", 
        "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", "Fade", "Forest DDPAT", "Freehand", "Gamma Doppler", "Lore",
        "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Gut Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Autotronic", "Black Laminate", "Blue Steel", "Boreal Forest", "Bright Water", 
        "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", "Fade", "Forest DDPAT", "Freehand", "Gamma Doppler", "Lore",
        "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Falchion Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", 
        "Fade", "Forest DDPAT", "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", 
        "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Huntsman Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", "Fade",
        "Forest DDPAT", "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained",
        "Tiger Tooth", "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "M9 Bayonet":
        skins = OptionMenu(root, skin, "Vanilla", "Autotronic", "Black Laminate", "Blue Steel", "Boreal Forest", "Bright Water", 
        "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", "Fade", "Forest DDPAT", "Freehand", "Gamma Doppler", "Lore",
        "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Navaja Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", 
        "Fade", "Forest DDPAT", "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", 
        "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Shadow Daggers":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", 
        "Fade", "Forest DDPAT", "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", 
        "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Stiletto Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", 
        "Fade", "Forest DDPAT", "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", 
        "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Talon Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", 
        "Fade", "Forest DDPAT", "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", 
        "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Ursus Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", "Damascus Steel", "Doppler", 
        "Fade", "Forest DDPAT", "Marble Fade", "Night", "Rust Coat", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Tiger Tooth", 
        "Ultraviolet", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Classic Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", 
        "Fade", "Forest DDPAT", "Night Stripe", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Paracord Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", 
        "Fade", "Forest DDPAT", "Night Stripe", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Survival Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", 
        "Fade", "Forest DDPAT", "Night Stripe", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Skeleton Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", 
        "Fade", "Forest DDPAT", "Night Stripe", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Urban Masked")
        skins.grid(row=2, column=2)

    elif item.get() == "Nomad Knife":
        skins = OptionMenu(root, skin, "Vanilla", "Blue Steel", "Boreal Forest", "Case Hardened", "Crimson Web", 
        "Fade", "Forest DDPAT", "Night Stripe", "Safari Mesh", "Scorched", "Slaughter", "Stained", "Urban Masked")
        skins.grid(row=2, column=2)


#GLOVES
    elif item.get() == "Broken Fang Gloves":
        skins = OptionMenu(root, skin, "Jade", "Needle Point", "Unhinged", "Yellow-banded")
        skins.grid(row=2, column=2)

    elif item.get() == "Sport Gloves":
        skins = OptionMenu(root, skin, "Amphibious", "Arid", "Big Game", "Bronze Morph", "Hedge Maze", "Nocts", "Omega",
        "Pandora's Box", "Scarlet Shamagh", "Slingshot", "Superconductor", "Vice")
        skins.grid(row=2, column=2)

    elif item.get() == "Specialist Gloves":
        skins = OptionMenu(root, skin, "Buckshot", "Crimson Kimono", "Crimson Web", "Emerald Web", "Fade", "Field Agent",
        "Forest DDPAT", "Foundation", "Lt. Commander", " Marble Fade", "Mogul", "Tiger Strike")
        skins.grid(row=2, column=2)

    elif item.get() == "Moto Gloves":
        skins = OptionMenu(root, skin, "3rd Commando Company", "Blood Pressure", "Boom!", "Cool Mint", "Eclipse", "Finish Line",
        "Polygon", "POW!", "Smoke Out", "Spearmint", "Transport", "Turtle")
        skins.grid(row=2, column=2)

    elif item.get() == "Hand Wraps":
        skins = OptionMenu(root, skin, "Arboreal", "Badlands", "CAUTION!", "Cobalt Skulls", "Constrictor", "Desert Shamagh",
        "Duct Tape", "Giraffe", "Leather", "Overprint", "Slaughter", "Spruce DDPAT")
        skins.grid(row=2, column=2)
        
    elif item.get() == "Driver Gloves":
        skins = OptionMenu(root, skin, "Black Tie", "Convoy", "Crimson Weave", "Diamondback", "Imperial Plaid", "King Snake",
        "Lunar Weave", "Overtake", "Queen Jaguar", "Racing Green", "Rezan the Red", "Snow Leopard")
        skins.grid(row=2, column=2)

    elif item.get() == "Bloodhound Gloves":
        skins = OptionMenu(root, skin, "Bronzed", "Charred", "Guerrilla", "Snakebite")
        skins.grid(row=2, column=2)

    elif item.get() == "Hydra Gloves":
        skins = OptionMenu(root, skin, "Case Hardened", "Emerald", "Mangrove", "Rattler")
        skins.grid(row=2, column=2)

#MAIN SHOW FUNCTIONS
def showbuff():

    buffvalue = buff.get()
    multipliervalue = multiplier.get()

    buffqs = float(buffvalue) * float(multipliervalue)
    buffqs = round(buffqs, 2)
    after_tax = float(buffvalue) - (float(buffvalue) * 0.025)
    after_tax = round(after_tax, 2)
    bufftors =  float(after_tax) * float(multipliervalue)
    bufftors = round(bufftors, 2)
 
    showbuff = Label(root, text="                                                                  ") 
    showbuff.grid(row=10, column=1)
    showbuff = Label(root, text="Buff value is " + str(buffvalue)) 
    showbuff.grid(row=10, column=1)

    showbuffqs = Label(root, text="                                                                 ") 
    showbuffqs.grid(row=10, column=2)
    showbuffqs = Label(root, text="Buff to INR (" + str(multipliervalue) + ") is ₹ " + str(buffqs))
    showbuffqs.grid(row=10, column=2)

    empty11 = Label(root, text=" ")
    empty11.grid(row=11, column=0)

    empty12 = Label(root, text=" ")
    empty12.grid(row=12, column=0)

    showbuffaftertax = Label(root, text="                                                           ") 
    showbuffaftertax.grid(row=12, column=1)
    showbuffaftertax = Label(root, text="After tax " + str(after_tax)) 
    showbuffaftertax.grid(row=12, column=1)

    showbuffaftertax = Label(root, text="                                                            ")
    showbuffaftertax.grid(row=12, column=2)
    showbuffaftertax = Label(root, text="After tax to INR (" + str(multipliervalue) + ") is ₹ " + str(bufftors))
    showbuffaftertax.grid(row=12, column=2)

def showvalues():
    wear_value = wear.get()
    gun_name = item.get()
    skin_name = skin.get()
    stat_trak = stattrak.get()
    category_name = category.get()
    
    if category_name == "Knives" or category_name == "Gloves":

        if skin_name == "Vanilla":
            
            if stat_trak == "Non Stat-Trak":
                url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=24&market_hash_name=%E2%98%85 "+ gun_name

            else:
                url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=24&market_hash_name=%E2%98%85 StatTrak%E2%84%A2 "+ gun_name

        elif stat_trak == "Non Stat-Trak":
            url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=24&market_hash_name=%E2%98%85 "+ gun_name + " | " + skin_name + " (" + wear_value + ")"

        else:
            url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=24&market_hash_name=%E2%98%85 StatTrak%E2%84%A2 "+ gun_name + " | " + skin_name + " (" + wear_value + ")"

    else:
        if stat_trak == "Non Stat-Trak":
            url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=24&market_hash_name=" + gun_name + " | "+ skin_name +" (" + wear_value + ")"

        else:
            url = url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=24&market_hash_name=StatTrak%E2%84%A2 "+ gun_name + " | " + skin_name + " (" + wear_value + ")"

    if skin_name == "Vanilla":
        buffurl = "https://buff.163.com/market/?game=csgo#tab=selling&page_num=1&search=" + gun_name 
    
    else:

        buffurl = "https://buff.163.com/market/?game=csgo#tab=selling&page_num=1&search=" + gun_name + " " +  skin_name + " " + wear_value

    def openweb():
        webbrowser.open(buffurl)

    response = requests.get(url)

    info = response.json()

    price = re.split(r'[₹ .\s]\s*',info["lowest_price"])
    price = price[1].replace(',','')

    qs_price = int(int(price) * .65)

    result = Label(root, text="                                       ")
    result.grid(row=5,column=1)
    result = Label(root, text="Market Price is ₹ " + str(price))
    result.grid(row=5,column=1)

    result1 = Label(root, text="                                 ")
    result1.grid(row=5,column=2)
    result1 = Label(root, text="QS Price is ₹ " + str(qs_price))
    result1.grid(row=5,column=2)

    buff = Button(root, text = "Buff Link",command=openweb)
    buff.grid(row=5, column=3)

item.trace("w", show_skins)
category.trace("w", show_items)

drop2 = OptionMenu(root, wear, "Factory New", "Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scarred")
drop2.grid(row=3, column=0)

drop2 = OptionMenu(root, stattrak, "Non Stat-Trak", "Stat-Trak")
drop2.grid(row=3, column=1)

empty4 = Label(root, text=" ")
empty4.grid(row=4, column=0)

submit = Button(root, text="Submit!", pady=5, command=showvalues)
submit.grid(row=5, column=0)

empty7 = Label(root, text=" ")
empty7.grid(row=6, column=0)

empty8 = Label(root, text=" ")
empty8.grid(row=7, column=0)

enterbuff = Label(root, text="Enter Buff Value:")
enterbuff.grid(row=8, column=0)

buff = Entry(root)
buff.grid(row=8, column=1)

entermulti = Label(root, text="Multiplier:")
entermulti.grid(row=8, column=2)

multiplier = Entry(root)
multiplier.grid(row=8, column=3)

empty9 = Label(root, text=" ")
empty9.grid(row=9, column=0)

submitbuff = Button(root, text="Submit!", pady=5, command=showbuff)
submitbuff.grid(row=10, column=0)


root.mainloop()