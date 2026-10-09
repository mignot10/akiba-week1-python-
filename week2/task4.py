word = input("Enter the word: ")

word = word.lower()

reversed_word = word[::-1]
if word == reversed_word:
    print("Palindrom")
else: 
    print("Not palindrom")