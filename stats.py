def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    count = {}

    for char in text.lower():
        if char in count:
            count[char] += 1
        
        else:
            count[char] = 1
    
    return count


