def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(book_path):
    filecontent = get_book_text(book_path)
    filecontent = filecontent.split()
    num_words = len(filecontent)
    print(f"Found {num_words} total words")

def sort_char(char_list):
    char_result = []
    for char in char_list:
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = char_list[char]
        char_result.append(char_dict)
    return char_result

def sort_on(items):
    return items["num"]

def get_num_char(book_path):
    filecontent = get_book_text(book_path)
    filecontent = list(filecontent)
    result = {}
    for f in filecontent:
        if f.lower() not in result:
            result[f.lower()] = 1
        else:
            result[f.lower()] += 1

    result = sort_char(result)
    result.sort(reverse=True, key=sort_on)

    for x in result:
        print(f"{x["char"]}: {x["num"]}")