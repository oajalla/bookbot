from stats import count_letters, sort_character_count, count_words
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    book_text = get_book_text(sys.argv[1])
    total_words = count_words(book_text)
    total_letters = count_letters(book_text)
    sorted_chars = sort_character_count(total_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()
     