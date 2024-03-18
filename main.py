def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_book_word_count(text)
    letters = get_letter_count(text)
    print(f"Beginning report...")
    print()
    print_report(words, letters)
    print()
    print("End of report")

def print_report(words, letters):
    print(f"{words} words found in the document")
    char_list = list(letters.items())
    char_list.sort(reverse=True, key=sort_on)
    for char in char_list:
        if char[0].isalpha():
            print(f"The '{char[0]}' was found {char[1]} times")
        else:
            print("heheheeh")

def sort_on(item):
    return item[1]

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_word_count(text):
    return len(text.split())

def get_letter_count(text):
    letters_dict = {}
    for str in text:
        letters_split = str.lower()
        if str.isalpha():
            if letters_split in letters_dict:
                letters_dict[letters_split] += 1
            else:
                letters_dict[letters_split] = 1
        else:
            continue
    return letters_dict

main()