def get_sets(x, i):
    if i == 0:
        return [[x[0]], []]

    new_sets = get_sets(x, i-1)
    return new_sets + add_element(x[i], new_sets)

def add_element(ele, sets):
    sets = [each_set + [ele] for each_set in sets]
    return sets

x= [5, 10, 6, 9]

sets = get_sets(x, len(x) - 1)
print(sets)
