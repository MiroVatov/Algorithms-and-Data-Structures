# Time complexity -> O(1)

def stupid_function(array):
    total = 0  # -> O(1)
    return total  # -> O(1)

    # Every time the function returns the same result


# --------------------------------------
# Function Time complexity is calculated from the all operations time complexities.


# Time comp. -> O(n)

def find_sum(array):
    total = 0  # O(1)
    for number in array:
        total += number  # -> O(1) - Adding single number to total, but it is repeated N - times,
        # depending on the size of the given array
    return total  # -> O(1)


# Time comp. -> T = O(1) + n*O(1) + O(1) = O(n)  -> Linear time

# 2-D array time complexity -> O(n2) -> Quadratic time complexity

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
]


def find_sum_2d(matrix):  # Quadratic time complexity
    total = 0  # -> O(1) - constant ime comp. - doesnt depend on the size of the input
    for row in matrix:  # O(n2)
        for number in row:
            total += number  # O(1) - doesnt depend on the size of the input
    return total  # O(1)  - doesnt depend on the size of the input

# T = O(1) + n2 * O(1) + O(1) -> if the matrix is square - equal amount of rows and cols

