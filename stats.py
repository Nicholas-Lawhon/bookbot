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

def sort_on(dict):
    return dict["num"]

def create_sorted_dict(dict):
    dict_list = []

    for i in dict:
        new_dict = {}

        new_dict["name"] = i
        new_dict["num"] = dict[i]
        dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def console_display(book_path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("----------- Character Count ----------")

    for i in char_count:
        if not i["name"].isalpha():
            continue
        else:
            print(f"{i["name"]}: {i["num"]}")