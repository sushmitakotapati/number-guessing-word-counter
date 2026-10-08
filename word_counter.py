from collections import Counter

filename = input("Enter the file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.lower().split()
    word_count = Counter(words)

    print("Total words:", len(words))
    print("\nWord Frequency:")

    for word, count in word_count.items():
        print(word, ":", count)

except FileNotFoundError:
    print("File not found.")