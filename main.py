import sys

from stats import get_word_count, get_char_counts, sort_char_counts
from report import Report


# returns content of file as str
def get_book_text(file_path: str):
    with open(file_path) as file:
        return file.read()


# gen report str
def gen_book_report(file_path: str):
    rpt = Report(39)
    rpt.add_line(f"Analyzing book found at {file_path}...")

    try:
        book_contents = get_book_text(file_path)
    except FileNotFoundError:
        rpt.add_line("Could not find book", True)
        return rpt.get_text()

    if len(book_contents) == 0:
        rpt.add_line("Book is empty", True)
        return rpt.get_text()

    word_count = get_word_count(book_contents)
    rpt.add_line_fill("Word Count")
    rpt.add_line(f"Found {word_count} total words")

    char_counts = sort_char_counts(get_char_counts(book_contents))
    rpt.add_line_fill("Character Count")

    for char_dict in char_counts:
        if char_dict["char"].isalpha():
            rpt.add_line(f" '{char_dict["char"]}': {char_dict["num"]}")

    return rpt.get_text()


def main():
    arg = sys.argv.pop()

    if arg == "main.py":
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    while arg != "main.py":
        print(gen_book_report(arg))
        arg = sys.argv.pop()


main()
