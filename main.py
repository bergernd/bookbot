def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    book_dictionary = letter_count(text)
    #print()
    #print(letter_count(text))
    sorted_dic = sort_dict(book_dictionary)
    print(f"--- Book Analysis of {book_path} ---")
    print(f"{word_count(text)} words found in the book")
    print("")
    for x in sorted_dic:
        print(f"The '{x['letter']}' character was found {x['num']} times")
    print('--- End of Analysis ---')



def word_count(book) -> int:
    words = book.split()
    return(len(words))

def letter_count(book) -> dict:
    lowwered_book = book.lower()
    total_words = {}

    for l in lowwered_book:
        if l in total_words:
            total_words[l] += 1
        else:
            total_words[l] = 1
    return(total_words)

def get_book(location):
     with open("books/frankenstein.txt") as f:
       return(f.read())

def sort_dict(book_dict) -> list:
    dict_list = []
    for x, y in book_dict.items():
        if x.isalpha():
            dict_list.append({'letter':x, 'num':y})

    #new_list = dict_list.sort(reverse=True)
    dict_list.sort(reverse=True, key = sort_on)

    return(dict_list)

def sort_on(dict):
    return dict['num']

main()

