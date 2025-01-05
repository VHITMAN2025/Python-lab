# remove duplicates in a list
def remove_duplicate(list):
    seen_items = []
    unique_list = []
    for item in list:
        if item in seen_items:
            continue
        else:
            seen_items.append(item)
            unique_list.append(item)
    return unique_list
list = [4,1,2,3,1,4]
print(remove_duplicate(list))