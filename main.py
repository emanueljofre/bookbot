from stats import get_num_words, char_count, sort_dic
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def print_report(dicc, path, total_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for char in dicc:

        if char["name"].isalpha():
            letter = char["name"]
            count = char["num"]
            print(f"{letter}: {count}")

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)
    else:
        path = sys.argv[1]
        book = get_book_text(path)
        num_words = get_num_words(book)
        print(f"{num_words} words found in the document")
        diccionary = char_count(book)
        sorted_chars = sort_dic(diccionary)
        print_report(sorted_chars, path, num_words)


main()
