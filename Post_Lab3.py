string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

string = input("Enter a string: ")

if string == string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

string = input("Enter a string: ")

if string.isdigit():
    print("String contains only digits")
else:
    print("String does not contain only digits")

sentence = input("Enter a sentence: ")

words = sentence.split()
longest_word = max(words, key=len)

print("Longest word:", longest_word)

sentence = input("Enter a sentence: ")

words = sentence.split()
last_word = words[-1]

print("Length of last word:", len(last_word))
