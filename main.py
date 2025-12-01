from stats import get_book_word_count, get_book_char_count


BOOK_LIST = {
    "Frankenstein": "books/frankenstein.txt"
}

def get_book_text(filepath):
    try:
        with open(filepath, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    return ""

def main():
    frankenstein_text = get_book_text(BOOK_LIST["Frankenstein"])
    frankenstein_text_word_count = get_book_word_count(frankenstein_text)
    frankenstein_text_char_count = get_book_char_count(frankenstein_text)
    print(frankenstein_text_word_count)
    print(frankenstein_text_char_count)


main()