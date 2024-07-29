def remove_duplicates(lst):
    the_list = []
    result_list = []
    for item in lst:
        if item not in the_list:
            the_list.append(item)
            result_list.append(item)
    return result_list
original_list = ['a','b','c','d','a','c']
unique_list = remove_duplicates(original_list)
print(unique_list)
