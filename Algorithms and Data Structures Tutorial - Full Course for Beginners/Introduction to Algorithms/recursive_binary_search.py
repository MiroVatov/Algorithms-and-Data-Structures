def recursive_binary_search(lst, target):

    # RECURSIVE SOLUTION
    # uses Logarithmic time -> O(log n) -> time complexity
    # THIS ALGORITHM USES LOGARITHMIC SPACE COMPLEXITY ->
    # every time the functions calls itself with a new list (size divided by 2), more space is needed

    if len(lst) == 0:
        # function base case or stopping condition,
        # where the function ends without finding the target we are searching for
        return False
    else:
        midpoint = len(lst) // 2

        if lst[midpoint] == target:
            # function base case, where the functions ends with result
            return True
        else:
            if lst[midpoint] < target:
                return recursive_binary_search(lst[midpoint + 1:], target)
            else:
                return recursive_binary_search(lst[:midpoint], target)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def verify(result):
    print(f"Target found : {result}")


result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 10)
verify(result)
