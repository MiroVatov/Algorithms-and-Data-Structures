from load import load_numbers


def merge_sort(lst):
    """
    1. sorts list in ascending order
    2. returns new sorted list

    Steps -> Divide and Conquer
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sorts the sublists created in previous step
    Combine: Merge the sorted lists created in the previous step

    Overall runtime : O(n log n) time.
    Takes linear space.
    """

    # Stopping condition -> Bottom case
    if len(lst) <= 1:
        return lst

    left_half, right_half = split(lst)

    # Recursion is invoked on the divided 2 parts
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(lst):
    """
    Divide the unsorted list at midpoint into sublists
    Returns 2 sublists -> left and right

    Takes O(log n) time -> Split operation divides the list in 2 halves.
    """
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    return left, right


def merge(left, right):
    """
    Merges 2 lists(arrays), sorting them in process.
    makes comparison between the left parts and right parts of the lists and changes their positions if needed.
    Returns new merged list.

    Runs in overall O(n) time -> n: is depending on the number of the splits that have to be done

    """
    l = []  # the new merged list
    i = 0  # tracks the indexes ot the current values in the left list
    j = 0  # tracks the indexes ot the current values in the right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(lst):
    n = len(lst)

    # This is the bottom case or stopping condition for the recursion
    if n == 0 or n == 1:
        return True  # naive sorting, when a list is empty or with 1 element, there is nothing to sort

    return lst[0] < lst[1] and verify_sorted(lst[1:])
    # each time we are calling the verify_sorted function with smaller list


# unsorted_list = [1, 5, 3, 9, 2]
unsorted_list = load_numbers('numbers/8.txt')
sorted_list = merge_sort(unsorted_list)
print(sorted_list)
print(verify_sorted(sorted_list))
# print(verify_sorted([2, 3, 4, 6, 5]))
