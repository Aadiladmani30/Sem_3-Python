i = 1
while i <= 100:
    if i % 2 != 0:
        print(i)
    i += 1

n = int(input("Enter n: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum =", total)

def count_digits(num):
    return len(str(num))

number = int(input("Enter a number: "))
print("Total digits =", count_digits(number))

num = input("Enter a number: ")

first_digit = num[0]
last_digit = num[-1]

print("First digit =", first_digit)
print("Last digit =", last_digit)

num = input("Enter a number: ")

# If number has only one digit
if len(num) == 1:
    print("Swapped number =", num)
else:
    swapped = num[-1] + num[1:-1] + num[0]
    print("Swapped number =", swapped)

num = input("Enter a number: ")

product = 1
for digit in num:
    product *= int(digit)

print("Product of digits =", product)

num = input("Enter a number: ")

reverse_num = num[::-1]

print("Reversed number =", reverse_num)

