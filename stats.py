
def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters_list = {}
    characters = text.lower()
    for character in characters:
        if character in characters_list:
            characters_list[character] += 1
        else:
            characters_list[character] = 1
    return characters_list

def sort_on(char):
     return char["num"]

    
def characters_final(character_dict):
    sorted_list = []
    for character in character_dict:
        sorted_list.append({"char": character, "num": character_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

