def sort_by_last(tup):
    return sorted(tup,key = lambda x: x[-1])
tup = [(5,4),(1,7),(9,3),(10,0)]
print(sort_by_last(tup))