import pickle
import random
import sys
import time


# This allows text to be read slowly line by line as if someone is speaking the words, as opposed to having all the text put in front of the user at once.
# This really helps to generate a more immersive experience that the user has someone talking to them
# *Iterates over each letter and force outputsitinto the terminal*
def speak_words(text):
    typing_speed = 80  # wpm
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print('')


# Prints a line at a time.
# *Iterates over lines slowly and then requires the enter key to be pressed before
# moving onto the next line*
def continue_text(lines: list):
    for line in lines:
        speak_words(line)
        # Make the user press enter to see the next line
        get_user_input([""])


# Takes input from the user. If not within our list of valid inputs then print error
# and loop, else return the valid user input
def get_user_input(valid_input: list):
    while True:
        user_entered = input()
        if user_entered not in valid_input:
            print("Invalid input. Please use one \
                   of the following inputs:\n")
            print(valid_input)
            user_entered = None
        else:
            return user_entered


# Iterates over options and text, printing numbers for each one.
def get_response(options: list):
    for index, option in enumerate(options):
        print(str(index) + ". " + option[0])

    valid_inputs = [str(num) for num in range(len(options))]

    option_index = int(get_user_input(valid_inputs))

    return options[option_index][1]


# When first loaded, it makes the current_page 1.
# If page is empty, ends story.
def form_story(story: dict):
    current_page = 1

    while current_page is not None:
        page = story.get(current_page, None)

        if page is None:
            current_page = None
            break

        continue_text(page['Text'])

        if len(page['Options']) == 0:
            current_page = None
            break

        current_page = get_response(page['Options'])


def run(chapter):
    if __name__ == '__main__':
        story = {}
        with open(chapter + '.ch', 'rb') as chapter:
            story = pickle.load(chapter)

        form_story(story)
