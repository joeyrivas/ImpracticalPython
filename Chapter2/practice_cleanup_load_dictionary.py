"""Load a text file as a list.

Arguments:
-text file name (and directory path, if needed)

Exceptions:
-IOError if filename not found.

Returns:
-A list of all words in a text file in lower case.

Requires-import sys

"""
import sys
clean_txt = []

def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            for x in loaded_txt:
                if len(x) > 1:
                    clean_txt.append(x)
            return clean_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)
