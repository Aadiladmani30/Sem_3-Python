import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting the line
plt.plot(x, y)

# Labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Graph")

# Display the plot
plt.show()

import matplotlib.pyplot as plt

# Data for the lines
x = [1, 2, 3, 4, 5]

y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [5, 4, 3, 2, 1]

# Plot lines
plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.plot(x, y3, label="Line 3")

# Add labels, title and legend
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Lines on Same Plot")
plt.legend()

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Sample data
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create bar chart
plt.bar(languages, popularity)

# Labels and title
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")

# Display chart
plt.show()
