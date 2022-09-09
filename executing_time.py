#a program to alculate the execution time of a programs

from time import time
start_time = time()

# a program to create acronyms
word = "ARTIFICIAL INTELLIGENCE"
text = word.split()
a = " "
for i in text:
    a = a + str(i[6]).lower()

print(a)

end_time = time()

execution_time = end_time - start_time
print("Execution time is", execution_time)