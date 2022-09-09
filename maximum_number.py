import numpy as np

numbers = [23, 76, 45, 20, 70, 65, 15, 54]

max_value =numbers[0]
idx_value = 0

for i in range(len(numbers)):
    if numbers[i] > max_value:
        max_value = numbers[i]
        idx_max = i

print( numbers,max_value, idx_max)  
print("index max:", np.argmax(np.asarray(numbers)))
print("value max:", numbers[np.argmax(np.asarray(numbers))])
