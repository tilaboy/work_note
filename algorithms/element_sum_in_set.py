from sorting import quick_search, merge_sort

def find_elements_2_sum(value, array):
    merge_sort(array, 0, len(array))
    print(array)
    for index, element in enumerate(array[:-1]):
        #print(index, element)
        # note the value should have negative
        if element > value:
            #print("{} too large, stop the loop".format(element))
            break
        else:
            matched_index = quick_search(array, index + 1, len(array) - 1, value - element)
            if matched_index is not None:
                print("found: [{}]=>{}, [{}]=>{}".format(index, element, matched_index, value-element))


arr = [5, 41, 2, 58, 11, 16, 32, 13, 4, 39, 29, 7, 15, 27, 53, 48, 34, 35, 24, 20, 26, 54, 55, 42, 23, 6, 59, 21, 1, 3]

find_elements_2_sum(40, arr)
