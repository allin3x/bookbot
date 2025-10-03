def sort_on(d):
    return d["num"]


def dict_to_sorted_list(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(cc:dict):
    dict(sorted(cc.items()))
    dict(sorted(cc.items(), key=lambda item: item[1]))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    print(cc)

def return_wordcount(text):
    words_list = text.split()
    word_count = len(words_list)
    print(f"Found {word_count} total words")
    return word_count

def count_characters(text):
    cc = {}

    for char in text:
        char = char.lower()
        if char in cc:
            cc[char] += 1
        else:
            cc[char] = 1
    return cc

# Method to count the letters and return a dict
def count_letters(text):
    # Crear un diccionario vacío
    dict = {}
    for character in text:
        letter = character.lower()
        if letter in dict:
            dict[letter] = dict[letter] + 1
        else:
            dict[letter] = 1
    return dict


# Method to count the words number
def get_num_words(text):
    words = text.split()
    return len(words)