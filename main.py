import numpy as np

arr = np.linspace(0, 9, 10)
modified_arr = np.where(arr % 2 != 0, -1, arr)
reshaped_arr = arr.reshape(2, 5)
even_sum = sum(x for x in arr if x % 2 == 0)

print("Original Array:", arr)
print("Modified Array:", modified_arr)
print("Reshaped Array:\n", reshaped_arr)
print("Sum of Even Numbers:", even_sum)
