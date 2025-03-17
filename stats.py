# return number of words in str
def get_word_count(content):
  return len(content.split())

# return dict of all char counts
def get_char_counts(content):
  counts = {}

  for char in content:
    char = char.lower()
    if char in counts:
      counts[char] += 1
    else:
      counts[char] = 1

  return counts