#Arrays and Strings
def reverse_string(input):
    return input[::-1]

def fin_max_min(input):
    #set min and max element to first index in array
    max = input[0]
    min = input[0]
    #loop over array to find the min and max
    for i in input:
        if i > max:
            max = i
        if i < min:
            min = i
    return max,min

def remove_duplicates(input):
    new_list = [input[0]]
    for i in input[1:]:
        if new_list[-1] != i:
            new_list.append(i)
    return new_list

