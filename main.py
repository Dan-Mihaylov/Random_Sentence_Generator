import random
from all_info import *


def generate_word(word_list):
    return random.choice(word_list)


print(f"Hello, this is your first random sentence.")
while True:
    rand_name = generate_word(names)
    rand_city = generate_word(cities)
    rand_verb = generate_word(verbs)
    rand_nouns = generate_word(nouns)
    rand_adverb = generate_word(adverbs)
    rand_location = generate_word(locations)
    print(f"{rand_name} from {rand_city} {rand_adverb} {rand_verb} {rand_nouns} {rand_location}")
    command = input("Pres Enter For New Sentence or type anything to stop.-->  \n")
    if command != "":
        break
