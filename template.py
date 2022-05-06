import pickle

story = {
    1: {
        'Text': [
            "Hello! Hit Enter to Start",
            "This is a template showing you an example of the syntax you must use to create your own game.",
        ],
        'Options': [
            ("Okay!", 2),
            ("Could you repeat that?", 1)
        ]
    },
    2: {
        'Text': [
            "What you're reading now is 'Text'. We'll use this to output stories to the user..",
            "Then afterwards, the user will be able to choose a choice from 'Options' by typing in the allocated number",
            "The option will bring us to a corresponding page. Pages are labelled by numbers, as seen in the template."
        ],
        'Options': [
            ("So these are my options, okay..", 3),
            ("Wait what, I'm confused!?", 2)
        ]
    },
    3: {
        'Text': [
            "So these are the two fundamentals you use to create your games!"
        ],
        'Options': [
            ("Okay", 4)
        ]
    },
    4: {
        'Text': [
            "You should have an idea how this works now. Copy and paste this template and create your own story.",
        ],
        'Options': [
            ("Sure!", 5)
        ]
    },
    5: {
        'Text': [
            "Have fun creating your stories!",
            "Be sure to give this project a star on Github if you enjoyed it!"
        ],
        'Options': [

        ]
    }
}

with open('current_game.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
    print("")
    print("[Game Loaded] Run 'engine.py' to begin playing!")
