from stats import word_count, character_count, sorted_dict_list, print_report

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    print(file_contents)




def main():

    #get_book_text("books/frankenstein.txt")
    word_count("books/frankenstein.txt")
    character_count("books/frankenstein.txt")
    sorted_dict_list("books/frankenstein.txt")
    print_report(sorted_dict_list("books/frankenstein.txt"), "books/frankenstein.txt")

main()