import random


ARRAY_SIZE = random.randint(5,50)
unsorted = []

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

    print(num_passes)

print("Worst case:", len(unsorted) - 1)
sort()
print(unsorted)
