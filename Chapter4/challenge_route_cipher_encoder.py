"""Create a program that takes the message as input and automatically
substitutes the code words, fills the bottom row with dummy words, and
transposes the words using the key [-1, 3, -2, 6, 5, -4]

Use a 6x7 matrix and if there are not enough words to fill out the matrix add
filler words

Required input = message to encode
"""
import sys
import random

#===============================================================================
# USER INPUT:

# the string to be encrypted (paste between quotes):
plaintext = """We will run the batteries at Vicksburg the night of April 16 and 
proceed to Grand Gulf where we will reduce the forts. Be prepared to cross the 
river on April 25 or 29. Admiral Porter.
"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#===============================================================================

# Code word dictionary
CODE_WORDS = {'BATTERIES': 'HOUNDS', 'VICKSBURG': 'ODOR', 'APRIL': 'CLAYTON',
              '16': 'SWEET', 'GRAND': 'TREE', 'GULF': 'OWL', 'FORTS': 'BAILEY',
              'RIVER': 'HICKORY', '25': 'MULTIPLY', '29': 'ADD',
              'ADMIRAL': 'HERMES', 'PORTER': 'LANGFORD'}
FILLER_WORDS = ('THE', 'REST', 'IS', 'JUST', 'NONSENSE', 'FILLING', 'ALL',
                'BLANKS')
KEY = """ -1 3 -2 6 5 -4 """
COLS = 6
ROWS = 7


def main():
    cipherlist = list(plaintext.upper().split())
    coded_cipherlist = add_code_words(cipherlist)
    matrix = create_matrix(coded_cipherlist)
    print(*matrix, sep='\n')
    key_int = key_to_int(KEY)
    encrypted_message = encrypt(key_int, matrix)
    print("\nEncryption key - {}".format(KEY))
    print("\nEncrypted message - {}".format(encrypted_message))


def add_code_words(cipherlist):
    """Take list of words and convert specific words that found in the
    CODE_WORDS dictionary"""
    index = 0
    for word in cipherlist:
        for key in CODE_WORDS:
            if word == key:
                cipherlist[index] = CODE_WORDS[key]
        index += 1
    return cipherlist


def create_matrix(cipherlist):
    """Create a 6x7 matrix of the cipher list by making a list of lists
    If there are not enough words to fill the matrix add random words from
    FILLER_WORDS list."""
    while len(cipherlist) < 42:
        cipherlist.append(random.choice(FILLER_WORDS))
    matrix = []
    while cipherlist:
        matrix.append(cipherlist[:6])
        cipherlist = cipherlist[6:]
    return matrix


def key_to_int(key):
    """Turn key into list of integers & check validity."""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
            or 0 in key_int:
        print("\nError - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int


def encrypt(key_int, matrix):
    """Use key to encrypt matrix and return coded message."""
    crypttext = ''
    stop = ROWS
    for k in key_int:
        if k < 0:  # read bottom-to-top of column
            crypttext += ' '.join(
                [matrix[r - 1][abs(k) - 1] for r in range(stop, 1, -1)])
        elif k > 0:  # read top-to-bottom of column
            crypttext += ' '.join(
                [matrix[r][abs(k) - 1] for r in range(0, stop)])
        crypttext += ''.join(' ')
    return crypttext


if __name__ == '__main__':
    main()
