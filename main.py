import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words, get_num_char
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
get_num_words(sys.argv[1])
print("--------- Character Count -------")
get_num_char(sys.argv[1])
print("============= END ===============")