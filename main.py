# A function that opens and reads a file
def get_book_text(path):
    with open(path) as f:
        return f.read()

# A function that takes a string and return the wordcount   
def count_words(text):
    words = text.split()
    return len(words)

# A function that takes a string and returns all char occurences as list of dictionaries
def count_characters(text):
    dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        count = dict.get(char, 0)
        count += 1
        dict[char] = count

    chars = []
    for char in dict:
        entry = {}
        if char.isalpha():
            entry["char"] = char
            entry["count"] = dict[char]
            chars.append(entry)

    chars.sort(reverse=True, key=sort_on)
         
    return chars

# Sort function
def sort_on(dict):
    return dict["count"]

# A Function that takes a path to a book and prints its wordcount and character count information
def print_book_info(book_path):
    text = get_book_text(book_path)
    word_count = count_words(text)
    characters = count_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    
    for entry in characters:
        print(f"The '{entry["char"]}' character was found {entry["count"]} times")

    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    print_book_info(book_path)
    


main()
