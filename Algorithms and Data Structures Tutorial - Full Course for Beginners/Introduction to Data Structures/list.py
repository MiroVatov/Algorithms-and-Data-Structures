new_list = [1, 2, 3]

print(new_list[0])

print(new_list[5])

if 1 in new_list:  # IN operator uses linear search in the list -> like for loop, with comparison operation
    print(True)

# INSERT method

new_list.insert(0, 5)
"""    
  inserting value on specific index in a list uses linear runtime -> 
  goes through each element in a list and all elements moves with one position after the chosen index
  INSERT method also uses the append method memory size allocation when method is used: 0, 4 ,8 ,16, 25, 35, 46 ...
  INSERT after the resize, all element needs to be shifted by one. This is more time consuming.
"""

# APPEND method

new_list.append(9)
"""
  appending value in a list -> uses constant time to perform, 
  because is inserting the element at the end of the array.
  append method calls LIST RESIZE operation before append the element, in order to allocate the proper memory size for the data.
  List resize operation grows the memory and the list respectively each time the list needs to be resized -
  (number of elements in the list gets to the limit of the actual list size) with 0, 4, 8, 16, 25, 35, 46 size....memory allocation
"""

# EXTEND method

numbers = []

numbers.extend([4, 5, 6])
"""
EXTEND makes series of append operations until there are elements to extend
Time complexity O(k) -> K: is the number of elements we want to add in the existing list
"""

# DELETE method

"""
.remove(element)
.pop(index)

when performed -> all the elements in a list, shifts to the right (the list size is shrinking, the opposite of the insert method)
"""