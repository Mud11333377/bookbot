from stats import *

def main():
    filepath = "books/frankenstein.txt"
    
    try:
        text = get_book_text(filepath)
        print(text)

        num_words = get_number_of_words(text)
        
        print(f"{num_words} words found in the document")

        character_count = get_character_count(text)

        print(character_count)



    except FileNotFoundError:
        print(f"File not found at at '{filepath}'. Please check the path.")
    except Exception as e:
        print(e)
    

main()