"""Decrypt a civil war 'rail fence' type cipher.

This is for a 3-rail fence cipher for short messages.

Example plaintext:  'Buy more Maine potatoes'

Rail fence style:  B   O   A   P   T
                    U M R M I E O A O S
                     Y   E   N   T   E

Read zigzag:       \/\/\/\/\/\/\/\/\/\/

Ciphertext:  BOAPT UMRMI EOAOS YENTE

"""

# ===============================================================================
# USER INPUT:

# the string to be decrypted (paste between quotes):
ciphertext = """LSSEE EDTEE DTREU COSVR HRVRN RSUDR HSAEF HTEST ROTIA ENTHO EE"""


# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ===============================================================================

def main():
    """Run program to decrypt 3-rail rail fence cipher."""
    message = prep_ciphertext(ciphertext)
    row1, row2, row3 = split_rails(message)
    decrypt(row1, row2, row3)


def prep_ciphertext(ciphertext):
    """Remove whitespace."""
    message = "".join(ciphertext.split())
    print("\nciphertext = {}".format(ciphertext))
    return message


def split_rails(message):
    """Split message in three, always rounding UP for 1st row."""
    cycle = int((len(message) / 4))
    print(cycle)
    partial = (len(message) % 4)
    print(partial)
    if partial == 1:
        row_1_len = cycle + 1
        row_2_len = cycle * 2
    elif partial == (2 or 3):
        row_1_len = cycle + 1
        row_2_len = cycle * 2 + 1
    else:
        row_1_len = cycle
        row_2_len = cycle * 2
    print(row_1_len, row_2_len)
    row1 = (message[:row_1_len]).lower()
    row2 = (message[row_1_len:row_1_len + row_2_len]).lower()
    row3 = (message[row_1_len + row_2_len:]).lower()
    print (row1, row2, row3)
    return row1, row2, row3


def decrypt(row1, row2, row3):
    """Build list with every other letter in 3 strings & print."""
    plaintext = []
    for i in range(0,len(row3)):
        plaintext.append(row1[i])
        plaintext.append(row2[i*2])
        plaintext.append(row3[i])
        if (len(row2)%2) == 0 and (i != len(row3)):
            plaintext.append(row2[i*2+1])
    print("rail 1 = {}".format(row1))
    print("rail 2 = {}".format(row2))
    print("rail 3 = {}".format(row3))
    print("\nplaintext = {}".format("".join(plaintext)))


if __name__ == '__main__':
    main()
