from stats import get_word_count
from stats import get_char_counts
from stats import sort_char_counts

# returns content of file as str
def get_book_text(file_path):
  with open(file_path) as file:
    return file.read()

def main():
  book_contents = get_book_text("books/frankenstein.txt")

  word_count = get_word_count(book_contents)
  print(f"{word_count} words found in the document")

  char_counts = sort_char_counts(get_char_counts(book_contents))
  print(char_counts)

main()