from stats import get_word_count
from stats import get_char_counts
from stats import sort_char_counts
import sys

# returns content of file as str
def get_book_text(file_path):
  with open(file_path) as file:
    return file.read()

# gen report str
def gen_book_report(file_path):
  report_txt = "============ BOOKBOT ============\n"
  report_txt += f"Analyzing book found at {file_path}...\n"
  
  book_contents = get_book_text(file_path)

  word_count = get_word_count(book_contents)
  report_txt += "----------- Word Count ----------\n"
  report_txt += f"Found {word_count} total words\n"

  char_counts = sort_char_counts(get_char_counts(book_contents))
  report_txt += "--------- Character Count -------\n"
  
  for char_dict in char_counts:
    if char_dict["char"].isalpha():
      report_txt += f"{char_dict["char"]}: {char_dict["num"]}\n"

  report_txt += "============= END ==============="

  return report_txt

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  print(gen_book_report(sys.argv[1]))

main()