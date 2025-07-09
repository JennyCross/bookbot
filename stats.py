# stats.py
def get_num_words(text):
    """
    Counts the number of words in a given text.
    
    :param text: The text to count words in.
    :return: The number of words in the text.
    """
    return len(text.split())

def get_dictionary_of_letters(text):
    """
    Creates a dictionary of letters and their frequencies in the given text.
    
    :param text: The text to analyze.
    :return: A dictionary with letters as keys and their frequencies as values.
    """
    letter_dict = {}
    for char in text:
        char = char.lower()  # Normalize to lowercase
        letter_dict[char] = letter_dict.get(char, 0) + 1
    return letter_dict

def generate_report(text):
    """
    Generates a report of the text statistics.
    
    :param text: The text to analyze.
    :return: A string report of the text statistics.
    """
    num_words = get_num_words(text)
    letter_dict = get_dictionary_of_letters(text)
    
    report = "============ BOOKBOT ============\n"
    report += "Analyzing book found at books/frankenstein.txt...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {num_words} total words\n"
    report += "--------- Character Count -------\n"
    for letter, frequency in sorted(letter_dict.items(), key=lambda item: item[1], reverse=True):
        if letter.isalpha():
            report += f"{letter}: {frequency}\n"

    return report