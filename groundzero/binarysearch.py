import random


ARRAY_SIZE = random.randint(5,50)
unsorted = []
sorted = []

for i in range(ARRAY_SIZE):
    unsorted.append(random.randint(1,150)) 

def sort():
    n = len(unsorted)
    swap_count = 0
    num_passes = 0

    for j in range(n-1):
        for i in range(n - 1 - j):
            if unsorted[i] < unsorted[i + 1]:
                unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                swap_count += 1
        if swap_count == 0:
            break
        swap_count = 0
        num_passes += 1

def search():
    
    x = int(input("Input the number you want to search for: "))
    flag = False
    lower = 0
    upper = len(unsorted)-1
    midpoint = (upper + lower)//2

    while lower <= upper:

        midpoint = (upper + lower)//2

        if unsorted[midpoint] == x:
            print("Your number is located at i =", midpoint)
            break
        elif x > unsorted[midpoint]:
            upper = midpoint - 1
        elif x < unsorted[midpoint]:
            lower = midpoint + 1
    
    if x != unsorted[midpoint]:
        print("Number not found.")
    
  
sort()
print(unsorted)
search()


