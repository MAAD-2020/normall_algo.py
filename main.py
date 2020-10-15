import sys
import os.path
from algoriphm_application import step_of_alg, alg_ap
address_word = ""
address_alg = ""
address_out = ""
if __name__ == "__main__":
    if len(sys.argv) == 4:
        address_word = sys.argv[1]
        address_alg = sys.argv[2]
        address_out = sys.argv[3]
        print(type(address_word), address_alg, address_out)
    else:
        print("EROR OF INPUT, TRY AGAIN")
file_in_word = open("address_word")
file_in_alg = open("address_alg")
file_out = open("address_out", "w")
strings_of_alg = file_in_alg.read().rstrip().split("\n")
word_of_alg = file_in_word.read().rstrip().split("\n")
strings_of_alg = [x.split() for x in strings_of_alg]
print(alg_ap(word_of_alg, strings_of_alg))