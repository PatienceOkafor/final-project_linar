import numpy as np

numbers = [23, 76, 45, 20, 70, 65, 15, 54]

min_value =numbers[0]
idx_value = 0

for i in range(len(numbers)):
    if numbers[i] < min_value:
        min_value = numbers[i]
        idx_min = i

print( numbers,min_value, idx_min)  
print("index min:", np.argmin(np.asarray(numbers)))
print("value min:", numbers[np.argmin(np.asarray(numbers))])
