numbers = [2, 3, 4, 5]

product = 1
for num in numbers:
    product *= num

print("Product =", product)

numbers = [10, 25, 4, 89, 56]

largest = max(numbers)

print("Largest number =", largest)

my_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(my_list))

print("List without duplicates:", unique_list)

my_list = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for item in my_list:
    frequency[item] = frequency.get(item, 0) + 1

print("Frequency of elements:", frequency)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = list(set(list1) & set(list2))

print("Common items:", common)

nums = [1, 2, 3, 4]

single_integer = int("".join(map(str, nums)))

print("Single integer:", single_integer)
