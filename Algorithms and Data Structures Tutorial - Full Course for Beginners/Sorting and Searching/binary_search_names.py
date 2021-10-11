# TODO -> Time Complexity: O(log n)

from load import load_strings

sorted_names_list = load_strings('names/sorted.txt')

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
                "Bria Kelly",
                "AAATHITHYAYA S",
                "Z KHAN"]


def binary_search(collection, target):
    first = 0
    last = len(collection) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


for name in search_names:
    index = binary_search(sorted_names_list, name)
    print(index)


