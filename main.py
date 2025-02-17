from collections import Counter

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

def count_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.split()  
    return len(words)  

def count_character_frequencies(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()  

    
    filtered_text = ''.join([char for char in text if char.isalpha()])

    char_counts = Counter(filtered_text)  
    return char_counts


filename = "books/frankenstein.txt"
word_count = count_words(filename)
print(f"Word count: {word_count}")

char_frequencies = count_character_frequencies(filename)

print(f"{word_count} words found in the document")
for letter, count in char_frequencies.most_common():
    print(f"The '{letter}' character was found {count} times")

print("--- End report ---")

main()