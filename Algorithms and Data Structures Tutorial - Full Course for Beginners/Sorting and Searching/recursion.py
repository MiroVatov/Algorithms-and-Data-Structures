from datetime import datetime

# NON-RECURSIVE SOLUTION

# def sum_numbers(nums):
#     total = 0
#
#     for number in nums:
#         total += number
#     return total

# RECURSIVE SOLUTION


def sum_numbers(nums):
    if not nums:
        return 0

    print(f'Calling sum_numbers{nums[1:]}')
    remaining_sum = sum_numbers(nums[1:])
    print(f'Call to sum_numbers {nums}, {nums[0]} + {remaining_sum}')
    return nums[0] + remaining_sum


numbers = [1, 5, 6, 3]
print(f'Final Result: {sum_numbers(numbers)}')
