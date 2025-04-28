def word_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    split_contents = file_contents.split()

    #print(f"{len(split_contents)} words found in the document")
    return len(split_contents)


def character_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    lowercase_contents = file_contents.lower()
    splitword_contents = list(lowercase_contents)
    
    character_count = {}

    for char in splitword_contents:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    #print(character_count)
    return character_count

# 1. new function takes dictionary characters and their counts and returns a sorted list of dictionaries
def sorted_dict_list(file_path):
    # char_count = {}
    char_count = character_count(file_path)

    sorted_list = []

    for char in char_count:
        sorted_list.append({"char": char, "num": char_count[char]})

    final_sorted = sorted(sorted_list, key=lambda x: x['num'], reverse=True)

    
    #print(final_sorted)
    return(final_sorted)


def sort_on(dict):
    return dict['num']


def print_report(sorted_dict, file_path):
    count = word_count(file_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    for k in sorted_dict:
        if k['char'].isalpha():
            print(f"{k['char']}: {k['num']}")

    print("============= END ===============")