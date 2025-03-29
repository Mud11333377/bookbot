def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    char_count = {}

    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        
        else:
            char_count[char] = 1
    
    return char_count

def sort_char_counts(char_count):
    sorted_list = []

    for char , count in char_count.items():
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})
        
        def get_count(item):
            return item["count"]

    sorted_list.sort(key=get_count, reverse=True)
    return sorted_list
