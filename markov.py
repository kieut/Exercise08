#!/usr/bin/env python

import sys
from sys import argv

script, corpus = argv

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    open_file = open(corpus)

    all_text = open_file.read().lower()

    words = all_text.split()

    stripped_list = []
    

    for word in words:
        word = word.strip(",.?!-")
        stripped_list.append(word)

    markov_chains = {}

    for i in range(len(stripped_list) - 2):
        x = i + 1
        y = i + 2
        tuple_key = stripped_list[i], stripped_list[x]
        value = [stripped_list[y]]

        # word_counts_dict[word] = word_counts_dict.get(word, 0) + 1
        # set default value to empty list in order to add new value
        markov_chains[tuple_key] = markov_chains.get(tuple_key, []) + value

    return markov_chains


# make_chains(corpus)


def make_text(input_dictionary):
    import random
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # tell program to choose a random key and a random value from the key
    # and return two words
    # then use 2nd word as key, and run again
    # keep doing that till it runs out
    # chain_dictionary, populate a list of every key

    key_list = input_dictionary.keys()
    random_key = random.randrange(len(key_list))
    random_tuple = key_list[random_key]

    
    random_string = random_tuple[0] + " " + random_tuple[1]

    value_list = input_dictionary[random_tuple] #looks up key in dict, returns value

    random_value = random.randrange(len(value_list))

    third_word = value_list[random_value]

    random_string = random_string + " " + third_word

    split_string = random_string.split() # creates a list, each item is a word from the string

    new_tuple = (split_string[-2], split_string[-1])

    new_random_string = ""

     #start loop here#


    next_value_list = input_dictionary[new_tuple]

    new_random_value = random.randrange(len(next_value_list))

    next_word = next_value_list[new_random_value]

    new_random_string = new_random_string + " " + next_word

    #next: split new_random_string up
    new_split_string = new_random_string.split()

    next_tuple = (new_split_string[-2], new_split_string[-1])

    #end loop here#

    concatenated_string = random_string + new_random_string
    print next_tuple
    print random_string
    print new_random_string

    print concatenated_string

    # new_tuple = (random_tuple[1], third_word)

    # print new_tuple
    





    # return "Here's some random text."

def main():
    # args = sys.argv
    # import random
    chain_dictionary = make_chains(corpus)

    random_text = make_text(chain_dictionary)

    # Change this to read input_text from a file
    # input_text = "Some text"

    # chain_dict = make_chains(input_text)
    # random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()