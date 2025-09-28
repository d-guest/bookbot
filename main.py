import sys
from stats import get_word_count, get_character_count, sort_characters_list, characters_to_list

def get_book_text(filepath):
    with open(f"{filepath}", "r") as file:
        content = file.read()
    return content


def main(relative_path):
    book_text = get_book_text(relative_path)
    word_count = get_word_count(book_text)
    characters = get_character_count(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + relative_path + "...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("------- Character Count ---------")
    char_list = characters_to_list(characters)
    sorted_characters = sort_characters_list(char_list)
    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
            

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])

