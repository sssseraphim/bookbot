from stats import count_words

def get_books_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def main():
    text = get_books_text("books/frankenstein.txt")
    print(f"Found {count_words(text)} total words")

main()

