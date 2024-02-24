"""The BookBot project of Boot.dev"""


def main():
    """Main entry"""
    book_path = "./books/frankenstein.txt"
    book_text = read_book(book_path)
    word_count = get_word_count(book_text)

    print(f"The words count for the book at {book_path} is: {word_count}")


def get_word_count(input_str: str) -> int:
    """Gets the number of words of an input string"""
    words = input_str.split()
    return len(words)


def read_book(book_path: str) -> str:
    """Read the book at a given path."""
    with open(book_path, encoding="utf-8") as f:
        return f.read()


main()
