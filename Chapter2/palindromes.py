"""Find palindromes (letter palingrams) in a dictionary file."""
import load_dictionary
import time

word_list = load_dictionary.load('2of4brif.txt')
pali_list = []

start_time = time.time()
for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)
end_time = time.time()
print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
print("\nRuntime for this program was {} seconds.".format(end_time - start_time))