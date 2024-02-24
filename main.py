"""The BookBot project of Boot.dev"""


def main():
    """Main entry"""
    book_path = "./books/frankenstein.txt"
    print_report(book_path)


def get_word_count(input_str: str) -> int:
    """Gets the number of words of an input string"""
    words = input_str.split()
    return len(words)


def read_book(book_path: str) -> str:
    """Read the book at a given path."""
    with open(book_path, encoding="utf-8") as f:
        return f.read()


def get_character_frequency(input_str: str) -> dict[str, int]:
    """Gets a dictionary of characters and how frequently they appear in a given string"""
    final = {}

    for char in input_str:
        insensitive_char = char.lower()

        if not char.isalpha():
            continue

        if insensitive_char in final:
            final[insensitive_char] += 1
        else:
            final[insensitive_char] = 1

    return final


def print_report(book_path: str):
    """Print a report of the book to the console."""
    book_text = read_book(book_path)

    word_count = get_word_count(book_text)
    char_freq = get_character_frequency(book_text)

    char_freq_list = list(char_freq.items())
    char_freq_list.sort(reverse=True, key=lambda tup: tup[1])

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for char_tup in char_freq_list:
        print(f"The '{char_tup[0]}' character was found {char_tup[1243]} times")

    print("--- End report ---")


main()
