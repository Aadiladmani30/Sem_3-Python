# import pandas as pd

# # Two Series
# s1 = pd.Series([10, 20, 30, 40, 50])
# s2 = pd.Series([1, 2, 3, 4, 5])

# print("Addition:\n", s1 + s2)
# print("Subtraction:\n", s1 - s2)
# print("Multiplication:\n", s1 * s2)
# print("Division:\n", s1 / s2)

# import pandas as pd

# # Dictionary
# data = {'a': 100, 'b': 200, 'c': 300, 'd': 400}

# # Convert to Series
# s = pd.Series(data)
# print(s)

# import pandas as pd
# import numpy as np

# # From List
# s_list = pd.Series([10, 20, 30, 40])
# print("Series from list:\n", s_list)

# # From Numpy Array
# arr = np.array([1, 2, 3, 4, 5])
# s_array = pd.Series(arr)
# print("\nSeries from NumPy array:\n", s_array)

# # From Dictionary
# d = {'x': 100, 'y': 200, 'z': 300}
# s_dict = pd.Series(d)
# print("\nSeries from dict:\n", s_dict)

import pandas as pd

s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

# Stack Vertically
vertical = pd.concat([s1, s2], axis=0)
print("Stacked Vertically:\n", vertical)

# Stack Horizontally
horizontal = pd.concat([s1, s2], axis=1)
print("\nStacked Horizontally:\n", horizontal)

