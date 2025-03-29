from stats import *

def main():
    filepath = "books/frankenstein.txt"
    
    try:
        text = get_book_text(filepath)
        num_words = get_number_of_words(text)
        character_count = get_character_count(text)
        report = sort_char_counts(character_count)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in report:
            print(f"{item['char']}: {item['count']}")
        print("============= END ===============")



    except FileNotFoundError:
        print(f"File not found at at '{filepath}'. Please check the path.")
    except Exception as e:
        print(e)
    
main()