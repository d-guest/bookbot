from stats import get_word_count, get_character_count

def get_book_text(filepath):
    with open(f'{filepath}', 'r') as file:
        content = file.read()
    return content


def main(relative_path):
    book_text = get_book_text(relative_path)
    word_count = get_word_count(book_text)
    characters = get_character_count(book_text)
    print(f'Found {word_count} total words')
    print(characters)
    
main('books/frankenstein.txt')
