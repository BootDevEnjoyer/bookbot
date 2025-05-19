def count_words(book_text):
    words = book_text.split()
    nr_words = len(words)
    return nr_words

def count_chars(book_text):
    book_text = book_text.lower()
    char_counts = {}

    char_list = list(book_text)
    for char in char_list:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] = char_counts.get(char) + 1
    
    return char_counts

def get_sorted_char_counts(char_counts):
    sorted_dict = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
    for char in char_counts:
        if not char.isalpha():
            del sorted_dict[char]
    
    return sorted_dict

