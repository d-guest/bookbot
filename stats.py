def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = dict()
    words = text.split()
    for word in words:
        for char in word.lower():
            characters[char] = characters.get(char, 0) + 1
    return characters
