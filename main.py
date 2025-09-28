from stats import count_words, count_characters, sorted_dicts
import sys

def get_books_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def main():
    files = sys.argv
    if len(files) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book = files[1]
    text = get_books_text(files[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for d in sorted_dicts(count_characters(text)):
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

main()

