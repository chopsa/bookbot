from stats import word_count, character_count, sorted_dict_list, print_report
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    print(file_contents)




def main():

    try:
        #get_book_text("books/frankenstein.txt")
        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

        path_to_book = sys.argv[1]
    except FileNotFoundError as e:
        print(e)

    word_count(path_to_book)
    character_count(path_to_book)
    sorted_dict_list(path_to_book)
    print_report(sorted_dict_list(path_to_book), path_to_book)
    

main()