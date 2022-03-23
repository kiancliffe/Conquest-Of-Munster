import pickle

story = {
    1: {
        'Text': [
            "Hello there!",
            "This is a template showing you an example of the syntax you must use to create your own games!",
        ],
        'Options': [
            ("Understood", 2),
            ("Ugh...", 1)
        ]
    },
    2: {
        'Text': [
            "This is text. We'll use this to output to user our story",
            "Then afterwards, the user will be able to choose from an option"
            "The option will bring us to a following page. Pages are labelled by numbers."
        ],
        'Options': [
            ("So these are my options, okay..", 3),
            ("Wait what, I'm confused!?", 2)
        ]
    },
    3: {
        'Text': [
            "So we know about text and options, and we also have an idea of the syntax...",
            "Once you view this file within the Stories folder, that is."
            "Ignore this part for now." #TODO Chapter explaination
        ],
        'Options': [
            ("Okay", 4)
        ]
    },
    4: {
        'Text': [
            "So now you have an idea of how this works. Copy and paste this template and create your story.",
            "Also, make sure your story is within the Stories folder in the AdventureGame main directory!"
        ],
        'Options': [
            ("Understood!", 5)
        ]
    },
    5: {
        'Text': [
            "Have fun creating your stories!!",
            "Be sure to give this project a star on Github if you enjoyed it!"
        ]
    }
}
# Name the ch. file as the same name as this py. file
with open('../template.ch', 'wb') as chapter:
    pickle.dump(story, chapter)
