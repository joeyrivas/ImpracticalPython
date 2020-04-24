"""Find palindromes (letter palingrams) in a dictionary file."""
import load_dictionary
import time

word_list = load_dictionary.load('2of4brif.txt')
pali_list = []
#word_list = ('rotor', 'motor', 'radar', 'reader', 'onto')

def ispalindrome(word):
    if len(word) in (0,1):
        result = True
    elif word[:1] != word[len(word)-1:]:
        result = False
    else:
        word = word[1:-1]
        result = ispalindrome(word)
    return result

start_time = time.time()
for word in word_list:
    if ispalindrome(word) == True:
        pali_list.append(word)
end_time = time.time()

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
print("\nRuntime for this program was {} seconds.".format(end_time - start_time))
