def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    filepath = "books/frankenstein.txt"
    
    try:
        text = get_book_text(filepath)
        print(text)
    
    except FileNotFoundError:
        print(f"File not found at at '{filepath}'. Please check the path.")
    except Exception as e:
        print(e)

main()