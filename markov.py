"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    contents = contents.replace("\n", " ")

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # Create list of words from our string
    tokens = text_string.split(" ")

    for i in range(len(tokens) - 2):
        # Create bigram as tuple
        bigram = (tokens[i], tokens[i + 1])
        # Get the word that follows the bigram
        next_word = tokens[i + 2]
        # If bigram already exists in dict, append next word
        # to the list of next words in the value
        if bigram in chains:
            chains[bigram].append(next_word)
        # If bigram doesn't exist in dict, create new key, value pair where
        # bigram is key and value is an empty list
        else:
            chains[bigram] = []
            # Now that we have the list, append next word to it
            chains[bigram].append(next_word)
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
