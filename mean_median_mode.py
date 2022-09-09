#how to calculate the mean of list of numbers

numbers = [12,16,20,20,12,30,25,23,24,20,50,54]
numbers.sort()
print(numbers)

#how to calculate my mean
mean = sum(numbers) / len(numbers)
print(mean)

#to calculate the median
if len(numbers) % 2 == 0:
    m1=  numbers[len(numbers)//2] 
    m2 = numbers[len(numbers) //2 - 1] / 2
    median = m1 + m2
else:
    median = numbers[len(numbers)//2]

print(median)

#to calculate the mode
occurrences =  {}
for i in numbers:
    occurrences.setdefault(i,0)
    occurrences[i]+=1
frequent = max(occurrences.values())
for i,j in occurrences.items():
    if j == frequent:
        mode = i

print(mode)