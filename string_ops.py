# String functions
def str_funs(s1,s2):
    res = (s1 + s2)
    para = '''Hello HITMAN
How are you'''
    special_string =' Vijay,Raj '
    print(para)
    print(s1.isalpha())
    print(s2.isdigit())
    print(res.isalnum())
    print(s1.isdigit())
    print((s1+" ")*3)
    print(s1 != s2)
    print(s1.format('%s'))
    print(s1[0:3])
    print(s1[-3:])
    print(special_string.strip())
    print(special_string.rstrip())
    print(special_string.lstrip())
    sub1 , sub2 = special_string.split(",")
    print(sub1)
    print(sub2)
    special_string2 = special_string.replace(' ','K')
    print(special_string2)
    print(special_string.capitalize())
    print(special_string.count('a'))
    print(special_string.find('y'))
    print(special_string.rfind('j'))
    print(special_string.index('i'))
    print(special_string.rindex('V'))
    print(s1.endswith('N'))
    print(s2.startswith('1'))
def isPal(string):
    string = str(string)
    if(string == string[::-1]):
        return True
    else:
        return False
# count number of upper case letters in a string
def count_lower(string):
    count = 0
    for iter in string:
        if iter.isupper():
            count += 1
    return count

# 
str_funs('HITMAN','123')
print(isPal('mom'))
print(count_lower('AeroPlane'))
