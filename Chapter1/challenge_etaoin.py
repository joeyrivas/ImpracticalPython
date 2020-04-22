"""Create chart showing the letter frequency in a given sentence"""
import sys
import pprint
from collections import defaultdict

sentence = 'This is the song that never ends, yes it goes on and on my \
friend, some people started singing it.'
spanish = 'Esta es la cancion que nunca termina, si sigue y sigue en mi amigo \
algunas personas comenzaron a cantarlo.'

ALPHABET = 'abcedfghijklmnopqrstuvwxyz'

# defaultdict module lets you build dictionary keys on the fly
mapped = defaultdict(list)

for char in spanish:
    char = char.lower()
    if char in ALPHABET:
        mapped[char].append(char)

for char in ALPHABET:
    mapped[char]

# pprint lets you print stacked output
print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')
print("{}\n".format(spanish), file=sys.stderr)
pprint.pprint(mapped, width=110)
