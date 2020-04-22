"""Create chart showing the letter frequency in a given sentence"""
import sys
import pprint
from collections import defaultdict

sentence = "This is the song that never ends, yes it goes on and on my \
            friend, some people started singing it."

ALPHABET = 'abcedfghijklmnopqrstuvwxyz'

# defaultdict module lets you build dictionary keys on the fly
mapped = defaultdict(list)
for char in sentence:
    char = char.lower()
    if char in ALPHABET:
        mapped[char].append(char)

# pprint lets you print stacked output
print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')
print("{}\n".format(sentence), file=sys.stderr)
pprint.pprint(mapped, width=110)
