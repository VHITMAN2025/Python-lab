# merge two lists and sort it
def merge_sort_list(list1,list2):
    if list1 is None and list2 is None:
        print("List(s) is None")
    else:
        resultant_list = list1 + list2
        return sorted(resultant_list)
l1 = [1,4,3]
l2 = [9,10,1]
print(merge_sort_list(l1,l2))