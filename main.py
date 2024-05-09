# A function that opens and reads a file
def get_book_text(path):
    with open(path) as f:
        return f.read()

# A function that takes a string and return the wordcount   
def count_words(text):
    words = text.split()
    return len(words)

# A function that takes a string and returns all char occurences as dictionary
def count_characters(text):
    dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        count = dict.get(char, 0)
        count += 1
        dict[char] = count

    chars = []
    
         
    return dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    characters = count_characters(text)
    
main()
