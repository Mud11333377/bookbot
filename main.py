from stats import *
import sys

def main():
    
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

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



    
main()