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
    print(f"{nWords} words found in the document")
    print(nChar)
main()