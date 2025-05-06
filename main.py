def get_book_text(file):
    with open(file) as f:
        file_contents=f.read()
    return file_contents
def main():
    text=get_book_text("books/frankenstein.txt")
    words=text.split()
    nWords=len(words)
    print(f"{nWords} words found in the document")
main()