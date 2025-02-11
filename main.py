#main function to print out a book script
def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)

    #print header
    print(f"---Begin report of {book_path}---")

    #print book word count
    count = bookwordcount(file_contents)
    print(f"the book contains {count} words in the text")

    #print book char count
    char_dict = countChars(file_contents)

    #print out letters to console
    printTextChars(char_dict)
        

# read each word in the book and return a number
def bookwordcount(book_content):
    words = book_content.split()
    return len(words)

# read the contents of a file and return it as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

#return the character count of each char in the whole book
def countChars(text):
    char_dict = {}
    text = text.lower()

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    

    return char_dict

def printTextChars(dict):
    #sort dictionary by highest value 1st

    for char in dict:
        if char.isalpha():
            print(f"The '{char}' character was found {dict[char]} times")

    
    print("---End report---")

# A function that takes a dictionary and returns the value of the "num" key
# so .sort method knows how to sort




main()