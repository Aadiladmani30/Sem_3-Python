tup = (1, 2, 3, 2, 4, 2, 5)
element = 2
count = tup.count(element)
print(f"Occurrences of {element}: {count}")

tup = (10, 20, 30, 40)
element = 30

if element in tup:
    print(f"{element} exists in the tuple")
else:
    print(f"{element} does not exist in the tuple")
    
tup = ('H', 'e', 'l', 'l', 'o')
string = ''.join(tup)
print("Tuple to string:", string)

tup = (5, 1, 9, 3, 7)
print("Maximum:", max(tup))
print("Minimum:", min(tup))

tup = ("Python", "is", "fun")
string = ' '.join(tup)
print("Tuple of strings to single string:", string)

tup = (9, 1, 5, 3, 7)
sorted_tup = tuple(sorted(tup))
print("Sorted tuple:", sorted_tup)

tup = (100, 200, 300, 400, 500)
print("First element:", tup[0])
print("Last element:", tup[-1])