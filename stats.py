def get_book_word_count(book_string):
    book_split = book_string.split()
    
    return f"Found {len(book_split)} total words"

def get_book_char_count(book_string):
    char_dict = {}

    for i in book_string.lower():
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    return char_dict