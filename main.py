import sys
from stats import return_wordcount
from stats import count_characters
from stats import print_report
from stats import get_num_words, count_letters, dict_to_sorted_list, sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    #file_contents = get_book_text("books/frankenstein.txt")
    #print("Word Count: ", return_wordcount(file_contents))
    #cc = count_characters(file_contents)
    #print_report(cc)
    # Set a variable for the book path
    #book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    # Create a method that read the file and store it on a variable
    text = get_book_text(book_path)
    # Using the method get_num_words that count how many words does the file has, we store it on a variable
    num_words = get_num_words(text)
    # Using the method count_letters that count the number of letters and return a dict
    character_count = count_letters(text)
    # Variable that store the dict that we convert into a list
    listi = dict_to_sorted_list(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    #print(f"---Begin report of {book_path}")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in listi:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
main()