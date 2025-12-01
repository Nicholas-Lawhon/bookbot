from stats import get_book_word_count, get_book_char_count, create_sorted_dict, console_display
from pathlib import Path
import sys


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
    if not len(sys.argv) > 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    book_text_word_count = get_book_word_count(book_text)
    book_text_char_count = get_book_char_count(book_text)
    book_text_sorted_dict = create_sorted_dict(book_text_char_count)
    console_display(sys.argv[1], book_text_word_count, book_text_sorted_dict)
    

main()