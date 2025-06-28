def get_num_words(text):
    words = text.split()
    return len(words)


def char_count(text):
    chars = {}

    for char in text:
        char_lower = char.lower()

        if char_lower in chars:
            chars[char_lower] += 1
        else:
            chars[char_lower] = 1

    return chars


def sort_on(items):
    return items["num"]


def sort_dic(dic):
    sorted_list = []
    for i in dic:
        char_dicc = {"name": i, "num": dic[i]}
        sorted_list.append(char_dicc)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
