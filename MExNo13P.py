
# Count lines, words, and characters
with open("C:\\Users\\Aadiladmani\\OneDrive\\Desktop\\ict.txt", "r") as file:
    text = file.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)

#Read lines into a list
with open("C:\\Users\\Aadiladmani\\OneDrive\\Desktop\\ict.txt", "r") as file:
    lines_list = file.readlines()

# Remove newline characters
lines_list = [line.strip() for line in lines_list]

print("Lines in list:", lines_list)

# Read CSV file
import csv

with open("data-1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Merge two files
with open("C:\\Users\\Aadiladmani\\OneDrive\\Desktop\\ict.txt", "r") as f1, open("C:\\Users\\Aadiladmani\\OneDrive\\Desktop\\ict2.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("merged.txt", "w") as merged:
    merged.write(data1 + "\n" + data2)

print("Files merged into merged.txt successfully!")
