from EX1 import *


def test_fun(fun_name, input):
    print('input = ',input)
    print('output = ',fun_name(input))
    print()   

print("Arrays and Strings")
print("reverse a string in place")
test_fun(reverse_string,'abcdefg')

print('find the maximum and minimum elements in an array')
test_fun(fin_max_min,[123,34,2,45,6,2,54,7,0,21,5])

print('remove duplicates from a sorted array')
test_fun(remove_duplicates,[1,1,2,2,3,3,7,8,8,9,9])