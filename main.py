from stats import get_nWords
from stats import get_nChar

def get_book_text(file):
    with open(file) as f:
        file_contents=f.read()
    return file_contents
def main():
    text=get_book_text("books/frankenstein.txt")
    nWords=get_nWords(text)
    nChar=get_nChar(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {nWords} total words")
    print("--------- Character Count -------")
    for i in nChar:
        if i["char"].isalpha() is True:
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
main()