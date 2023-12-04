def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text) #Uncomment to see the text
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")
    num_letters = get_letter_count(text)
    # print(num_letters) #Uncomment to see the letters
    # by_letter = list(num_letters)
    #print(f"Letter {by_letter}")
    sorted_list = chars_to_sorted_list(num_letters)
    for item in sorted_list:
	    if item["char"].isalpha():
	        print(f"Letter {item['char']} appears {item['num']} times")
    print("---End Report---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
	return len(text.split())

def get_letter_count(text):
	chars = {}
	for char in text:
		letter_count = char.lower()
		if letter_count in chars:
			chars[letter_count] += 1
		else:
			chars[letter_count] = 1
	return chars

def chars_to_sorted_list(chars):
	letter_list = []
	for char in chars:
		letter_list.append({"char": char, "num": chars[char]})
	letter_list.sort(reverse=True, key=lambda x: x["num"])	
	return letter_list

main()