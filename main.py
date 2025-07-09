# File: main.py
from stats import get_num_words, get_dictionary_of_letters, generate_report
import sys

def get_book_text(path_to_file):
    """
    Reads the contents of a book file and returns it as a string.
    
    :param path_to_file: The path to the book file.
    :return: The contents of the book file as a string.
    """
    with open(path_to_file, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    file_contents = get_book_text(path_to_file)
    print(f"{get_num_words(file_contents)} words found in the document")
    print(get_dictionary_of_letters(file_contents))
    print(generate_report(file_contents))
main()