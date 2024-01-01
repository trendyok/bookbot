def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_letters = count_letters_dict(text)
    sorted_letters = letters_dict_to_list(count_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_letters:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def letters_dict_to_list(count_letters):
    sorted_list = []
    for l in count_letters:
        sorted_list.append({"char": l, "num": count_letters[l]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_letters_dict(text):
    letters = {}
    for letter in text:
        lower = letter.lower()
        if lower in letters:
            letters[lower] += 1
        else:
            letters[lower] = 1
    return letters


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()