dictionary = {}
def add_values(name,regd):
    dictionary['name'] = name
    dictionary['regd'] = regd
    return dictionary
name = input("enter your name: ")
regd = int(input("enter your regd number: "))
print(add_values(name,regd))