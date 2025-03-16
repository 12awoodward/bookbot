# returns content of file as str
def get_book_text(file_path):
  with open(file_path) as file:
    return file.read()

# return number of words in str
def get_word_count(content):
  return len(content.split())

def main():
  book_contents = get_book_text("books/frankenstein.txt")
  word_count = get_word_count(book_contents)
  print(f"{word_count} words found in the document")

main()