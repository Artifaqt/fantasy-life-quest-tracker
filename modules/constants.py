"""
Constants and configuration for Fantasy Life Quest Tracker
"""

# Life professions with emoji icons
LIVES = [
    ("Paladin", "⚔️"),
    ("Mercenary", "🗡️"),
    ("Hunter", "🏹"),
    ("Wizard", "🔮"),
    ("Carpenter", "🔨"),
    ("Blacksmith", "⚒️"),
    ("Tailor", "🪡"),
    ("Cook", "🍳"),
    ("Miner", "⛏️"),
    ("Woodcutter", "🪓"),
    ("Angler", "🎣"),
    ("Alchemist", "⚗️")
]

# Rank progression order for Life quests
RANK_ORDER = [
    "Novice",
    "Fledgling",
    "Apprentice",
    "Adept",
    "Expert",
    "Master",
    "Hero",
    "Legend",
    "Demi-Creator",
    "Creator"
]

# Status colors for quest rows
STATUS_COLORS = {
    0: "#ff6b6b",  # Unobtained - Red
    1: "#ffd43b",  # Obtained - Yellow
    2: "#51cf66",  # Completed - Green
    3: "#339af0"   # Turned In - Blue
}

# Status names
STATUS_NAMES = [
    "Unobtained",
    "Obtained",
    "Completed",
    "Turned In"
]
