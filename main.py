def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count(file_contents)

    print(word_count(file_contents))
    print(letter_count(file_contents))

def word_count(book):
    words = book.split()
    return(len(words))

def letter_count(book):
    lowwered_book = book.lower()
    total_words = {}

    for l in lowwered_book:
        if l in total_words:
            total_words[l] += 1
        else:
            total_words[l] = 1
    return(total_words)



main()

