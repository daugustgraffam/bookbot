def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text) # Uncomment to see the text
    num_words = get_word_count(text)
    print(f"Number of words: {num_words}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
	return len(text.split())

main()