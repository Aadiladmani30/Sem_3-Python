# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * math.pi * self.radius


# # Example usage
# c1 = Circle(5)

# print("Radius:", c1.radius)
# print("Area:", c1.area())
# print("Perimeter:", c1.perimeter())

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("-" * 30)

    def apply_discount(self, discount_percent):
        discount_amount = self.price * (discount_percent / 100)
        self.price -= discount_amount


# (a) Create two objects for different books
book1 = Book("Python Programming", "John Smith", 500)
book2 = Book("Data Structures", "Jane Doe", 650)

print("📘 Book 1 Details:")
book1.display_details()

print("📗 Book 2 Details:")
book2.display_details()

# (b) Apply 10% discount to book2
book2.apply_discount(10)

print("📉 Book 2 Details After 10% Discount:")
book2.display_details()
