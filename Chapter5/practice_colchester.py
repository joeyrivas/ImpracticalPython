"""Detect a message within a null cipher using a variable pattern of n
where n is the nth letter in the nth word of the message."""
import sys


def load_text(file):
    """Load a text file as a string."""
    with open(file) as f:
        return f.read().strip()


# load & process message:
filename = input("\nEnter full filename for message to decode: ")
try:
    loaded_message = load_text(filename)
except IOError as e:
    print("{}. Terminating program.".format(e), file=sys.stderr)
    sys.exit(1)

# check loaded message & # of lines
print("\nORIGINAL MESSAGE = {}".format(loaded_message), "\n")

# convert message to list and get length
message = loaded_message.split()
end = len(message)

# get user input on interval to check
increment = int(input("Input max word & letter position to "
                      "check (e.g., every 1 of 1, 2 of 2, etc.): "))
print()

# find letters at designated intervals
for i in range(1, increment + 1):
    print("\nUsing increment letter {} of word {}".format(i, i))
    print()
    count = i - 1
    location = i - 1
    for index, word in enumerate(message):
        if index == count:
            if location < len(word):
                print("letter = {}".format(word[location]))
                count += i
            else:
                print("Interval doesn't work", file=sys.stderr)
