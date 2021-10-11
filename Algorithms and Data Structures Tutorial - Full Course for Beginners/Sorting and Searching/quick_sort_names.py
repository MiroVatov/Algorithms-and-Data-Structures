from quick_sort import quicksort
from load import load_strings

#
unsorted_names = load_strings('names/unsorted.txt')
sorted_names = quicksort(unsorted_names)

file = open('names/sorted.txt', 'w')

for n in sorted_names:
    file.write(n + '\n')
    print(n)
