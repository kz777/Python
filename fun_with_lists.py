n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Create a function called flatten
def flatten(lists):
    results = []
    for numbers in lists:
        for num in numbers:
            results.append(num)
    return results
        



print flatten(n)