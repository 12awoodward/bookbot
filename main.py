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
  end = "============= END ==============="
  report_txt = "============ BOOKBOT ============\n"
  report_txt += f"Analyzing book found at {file_path}...\n"
  
  try:
    book_contents = get_book_text(file_path)
  except FileNotFoundError:
    report_txt += "\nCould not find book\n"
    report_txt += end
    return report_txt
  
  if len(book_contents) == 0:
    report_txt += "\nBook is empty\n"
    report_txt += end
    return report_txt

  word_count = get_word_count(book_contents)
  report_txt += "----------- Word Count ----------\n"
  report_txt += f"Found {word_count} total words\n"

  char_counts = sort_char_counts(get_char_counts(book_contents))
  report_txt += "--------- Character Count -------\n"
  
  for char_dict in char_counts:
    if char_dict["char"].isalpha():
      report_txt += f"{char_dict["char"]}: {char_dict["num"]}\n"

  report_txt += end

  return report_txt

def main():
  arg = sys.argv.pop()

  if arg == "main.py":
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  while arg != "main.py":
    print(gen_book_report(arg))
    arg = sys.argv.pop()

main()