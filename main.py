from stats import count_words, count_chars, get_sorted_char_counts
import sys

def get_book_text(filepath):
    # Takes a text (.txt) file from filepath and outputs the content as a string
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = args[1]
        
    book_text = get_book_text(filepath)

    num_words = count_words(book_text)
    char_counts = count_chars(book_text)
    sorted_counts = get_sorted_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key,value in sorted_counts.items():
        print(f"{key}: {value}")
    print("============= END ===============")

if __name__=='__main__':
    main()
