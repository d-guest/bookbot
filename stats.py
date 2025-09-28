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

def characters_to_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetic characters
            char_list.append({"char": char, "num": count})
        else:
            continue
    return char_list

def sort_characters_list(char_list):
    return sorted(char_list, key=lambda x: x['num'], reverse=True)