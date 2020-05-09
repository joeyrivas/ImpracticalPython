"""Encrypt a civil war 'rail fence' type cipher.
This is for a "3-rail" fence cipher for short messages.

Example text to encrypt:  'Buy more Maine potatoes'

Rail fence style:  B   O   A   P   T
                    U M R M I E O A O S
                     Y   E   N   T   E

Read zigzag:       \/\/\/\/\/\/\/\/\/\/

Encrypted:  BOAPT UMRMI EOAOS YENTE
"""

#===============================================================================
# USER INPUT:

# the string to be encrypted (paste between quotes):
plaintext = """Let us cross over the river and rest under the shade of the 
trees"""


# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#===============================================================================

def main():
    """Run program to encrypt message using 3-rail rail fence cipher."""
    message = prep_plaintext(plaintext)
    print(len(message))
    rails = build_rails(message)
    encrypt(rails)


def prep_plaintext(plaintext):
    """Remove spaces & leading/trailing whitespace."""
    message = "".join(plaintext.split())
    message = message.upper()  # convention for ciphertext is uppercase
    print("\nplaintext - {}".format(plaintext))
    return message


def build_rails(message):
    """Build 3 strings using the Cycle formula to determine the letters row."""
    cycle = 4
    top = message[0::cycle]
    if (len(message) % cycle) == 2:
        mid = message[1::2] + message[-1]
    else:
        mid = message[1::2]
    bottom = message[2::cycle]
    rails = top + mid + bottom
    print(top, mid, bottom)
    print(len(rails))
    print(len(message))
    return rails


def encrypt(rails):
    """Split letters in cipher text into chunks of 5 & join to make a string."""
    ciphertext = ' '.join([rails[i:i + 5] for i in range(0, len(rails), 5)])
    print("ciphertext = {}".format(ciphertext))
    print(len(ciphertext))


if __name__ == '__main__':
    main()
