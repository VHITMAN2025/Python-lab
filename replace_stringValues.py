# replace a value with another value

def replace_values(input_string):
    if input_string is None:
        return "String is empty"
    else:
        input_string = str(input_string).replace('1','2')
        return input_string
print(replace_values('Baahubali 1'))