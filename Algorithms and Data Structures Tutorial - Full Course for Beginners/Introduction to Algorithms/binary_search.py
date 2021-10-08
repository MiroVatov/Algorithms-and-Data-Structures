from linear_search import linear_search, verify


def binary_search(lst, target):
    # ITERATIVE SOLUTION
    # THIS ALGORITHM USES CONSTANT SPACE COMPLEXITY -> THE LIST SIZE DOES NOT CHANGE
    # Works if the list is sorted
    # At he end the midpoint variable should be equal to the searched target (if the target is in the list)

    first = 0  # constant time operation
    last = len(lst) - 1  # constant time operation

    while first <= last:
        midpoint = (first + last) // 2  # constant time operation

        if lst[midpoint] == target:  # compare is constant time operation
            return midpoint
        elif lst[midpoint] < target:  # compare is constant time operation
            first = midpoint + 1  # constant time operation
        else:
            last = midpoint - 1  # constant time operation

    return None


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 10)
index = linear_search(numbers, 10)
verify(index)
print(result)
