#main function to print out a book script
def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)



    count = bookwordcount(file_contents)
    print(f"the book contains {count} words.")
        

# read each word in the book and return a number
def bookwordcount(book_content):
    print("counting the word count for the book...")
    words = book_content.split()
    return len(words)

# read the contents of a file and return it as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()



main()