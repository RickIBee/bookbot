import sys
from stats import get_num_words
from stats import character_count
from stats import characters_final

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = character_count(text)
    sorted_list = characters_final(character_dict)
    print_report(book_path, num_words, sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()


