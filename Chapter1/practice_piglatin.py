"""This program takes an input word and converts it to pig latin."""
import sys

VOWELS = 'aeiouy'

while True:
    original_word = input("Enter a word to convert to pig latin: ")

    if original_word[0] in VOWELS:
        piglatin_word = original_word + 'way'
    else:
        piglatin_word = original_word[1:] + original_word[0] + 'ay'
    print()
    print("{}".format(piglatin_word), file=sys.stderr)

    try_again = input("\n\nTry again? (Press Enter or else n to stop\n ")
    if try_again.lower == "n":
        sys.exit()
