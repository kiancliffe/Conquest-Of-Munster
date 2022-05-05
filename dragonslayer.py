import pickle

story = {
    1: {
        'Text': [
            "Cullen was a brave Celtic warrior.",
            "One day, his chief asked him to slay an evil dragon that threatened their village.",
            "'Go through the mountain pass, Cullen', his chief said. 'You will find the dragon on the other side.'"
        ],
        'Options': [
            ("Okay!", 2)
        ]
    },
    2: {
        'Text': [
            "Cullen took his favourite sword and shield, and walked to the pass.",
            "There he found a cold cave, a windy cave, and a narrow trail."
        ],
        'Options': [
            ("Enter the cold cave", 17),
            ("Enter the windy cave", 8),
            ("Walk up the trail", 12)
        ]
    },
    3: {
        'Text': [
            "Cullen stepped onto a rocky hill.",
            "He could see the dragon sleeping below.",
            "He also saw a tavern off a road nearby."
        ],
        'Options': [
            ("Climb down", 16),
            ("Visit tavern", 14)
        ]
    },
    4: {
        'Text': [
            "Following the stench, Cullen found a filthy viking!",
            "The viking roared, and charged at Cullen with his spiked club."
        ],
        'Options': [
            ("Raise shield", 9),
            ("Swing sword", 13)
        ]
    },
    5: {
        'Text': [
            "Treading through the bog..",
            "Cullen discovered a banshee blocking his way."
        ],
        'Options': [
            ("Attack Banshee", 15),
            ("Give gold", 10)
        ]
    },
    6: {
        'Text': [
            "The sword lodged itself in the tough, scaly neck of the beast.",
            "It wailed and thrashed, but Cullen held on..",
            "and eventually he gained the upper hand..",
            "and managed to decapitate the beast, killing it instantly!",
            "Cullen returned home victorious..",
            "and his village was never bothered by the dragon again.",
            "THE END"
        ],
        'Options': [

        ]
    },
    7: {
        'Text': [
            "Leaving the bog behind him..",
            "Cullen could see the dragon's lair nearby..",
            "as well as a small, welcoming tavern."
        ],
        'Options': [
            ("Go to the lair", 16),
            ("Go to Tavern", 14)
        ]
    },
    8: {
        'Text': [
            "A strong gust of wind blew Cullen's torch out..",
            "and knocked him into a pit where he split his head and died..",
            "THE END"
        ],
        'Options': [

        ]
    },
    9: {
        'Text': [
            "The viking laughed as his club splintered Cullen's shield..",
            "and smashed into his face..",
            "Cullen died instantly.."
            "and the viking had a new trophy for his hut..",
            "THE END"
        ],
        'Options': [

        ]
    },
    10: {
        'Text': [
            "Cullen remembered a story his Gran told him..",
            "and tossed two gold coins down for the banshee.",
            "She faded away, allowing him to pass."
        ],
        'Options': [
            ("Continue", 7)
        ]
    },
    11: {
        'Text': [
            "Cullen crept towards the belly of the beast,",
            "but no sooner had he taken his eyes off the head of the beast..",
            "that it snapped him up and ate him whole..",
            "sword and all.",
            "THE END"
        ],
        'Options': [

        ]
    },
    12: {
        'Text': [
            "Climbing up, Cullen found a camp.",
            "He met a wise man who shared bread, and showed two paths to the dragon's lair.",
            "One went through the hills..",
            "and the other through a bog."
        ],
        'Options': [
            ("Take the hills", 3),
            ("Take the bog", 5)
        ]
    },
    13: {
        'Text': [
            "Before the viking could strike,",
            "Cullen swing his mighty sword!",
            "The viking's head and club fell uselessly to the ground."
        ],
        'Options': [
            ("Continue", 3)
        ]
    },
    14: {
        'Text': [
            "Cullen stopped at the tavern to rest before fighting the dragon.",
            "A rival clan ran the tavern, however..",
            "and poisoned his ale so they could steal his gold..",
            "THE END"
        ],
        'Options': [

        ]
    },
    15: {
        'Text': [
            "Cullen swing his sword as hard as he could,",
            "but the Banshee hardly seemed to notice.",
            "She turned around, staring at Cullen..",
            "and screamed a wail at him so violent..",
            "that his ears and eyes began to bleed..",
            "and he dropped to the ground suddenly..",
            "dying soon after..",
            "THE END"
        ],
        'Options': [

        ]
    },
    16: {
        'Text': [
            "Cullen found the lair where the dragon slept,",
            "tendrils of smoke wafting from its nostrils.",
            "The air made Cullen's eyes sting,",
            "and he nearly slipped on the bones of men, picked clean.",
            "The beast lay on its side..",
            "and the throat and belly both waiting targets."
        ],
        'Options': [
            ("Strike the neck", 6),
            ("Strike the belly", 11)
        ]
    },
    17: {
        'Text': [
            "Cullen stepped into the frozen cave..",
            "but his large fur clothing kept him warm.",
            "A smelly tunnel laid ahead of him,",
            "and wind howled from another to his left.",
            "A ladder was nearby as well."
        ],
        'Options': [
            ("Take the smelly tunnel", 4),
            ("Take the windy tunnel", 8),
            ("Climb the ladder", 12)
        ]
    }
}

with open('current_game.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
    print("")
    print("[Game Loaded] Run 'engine.py' to begin playing!")
