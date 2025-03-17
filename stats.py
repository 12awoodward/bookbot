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

# return array of sorted dicts of chars and counts
def sort_char_counts(counts_dict):
  counts_array = []

  for key in counts_dict:
    counts_array.append({
      "char": key,
      "num": counts_dict[key]
    })

  counts_array.sort(reverse=True, key=sort_by_num)
  return counts_array

def sort_by_num(dict):
  return dict["num"]