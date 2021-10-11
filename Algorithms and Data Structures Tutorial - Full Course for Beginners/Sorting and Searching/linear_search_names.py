# As usual, this code at the top isn 't relevant to the search algorithm.
# It's just like the code that loaded a list of numbers
# from a file in the previous stage, but this code calls a the above
# function, load_strings, to load a list of strings in.


# TODO TIME COMPLEXITY: Slow Search Algorithm -> O(n)


from datetime import datetime
from load import load_strings

names = load_strings('names/unsorted.txt')

# Here's a separate hard-coded list containing the 100 names we're
# going to search for. We'll loop through each name in the list, and
# pass it to our search function to get the index within the full
# list where it appears.

search_names = ["Edward Highland",
"Andrew Hojnowski",
"Dustin Holaday",
"Jared Hutchins",
"Brian Kelly",
"Michael Ketrow",
"Yoon Kim",
"MOOKIAH T",
"ALAGUVELU K",
"LOUIS SAM",
"ASIR PACKIARAJ",
"Cynthia Sullivan",
"SHAJITH K.K",
"SANJAY GUPTA",
"SARAVANA V",
"NAND V",
"ANAN GHOSH",
"ANA GHOSH",
"SANJA GUPTA",
"Michae Ketrow",
"Yoo Kim",
"Jare Hutchins",
"Bria Kelly"]


# Now let's implement the search function. Compared to the sorting
# algorithms, this is going to be short. The index_of_item function
# takes the Python list you want to search through, and a single
# target value you want to search for.

def index_of_item(collection, target):
    # Now we need to loop over each item in the list. The range
    # function gives us a range of numbers from its first argument up
    # to, but not including, its second argument. So if our list had a
    # length of five, this would loop over the indexes 0 through 4.
    for i in range(0, len(collection)):
        # We test whether the list item at the current index matches our
        # target.
        if target == collection[i]:
            # If it does, then we return the index of the current
            # item. This will exit the index_of_item function without
            # looping over the remaining items in the list.
            return i
    # If we reach the end of the loop without finding the target value,
    # that means it wasn't in the list. So instead of returning an
    # index, we return the special Python value "None", which indicates
    # the absence of a value.  Other languages have similar values like
    # "nil" or "null", but if yours doesn't, you might have to return a
    # value that would otherwise be impossible, like an index of "-1".
    return None


# Now let's call our new search function. We start by looping over
# the list of 100 values we're looking for. We're using the values
# themselves this time, not their indexes within the list, so there's
# no need to mess with Python's "range" function.

start_time = datetime.now()

for n in search_names:
    # Here's the actual call to the index_of_item function. We pass it
    # the full list of names that we loaded from the file, plus the
    # name we want to search for within that list. Then we store the
    # index it returns in a variable.
    index = index_of_item(names, n)
    # Lastly, we print the index we got back.
    print(index)

end_time = datetime.now()
print(f"Algorithn duration: {end_time - start_time}")