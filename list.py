    # write a python fuction that will take a  list s and the smallest value in the list

def  smallest_value(s):
    min_value  = s[0] 
    for number in s :
        if number < min_value :
            min_value = number 
    return min_value

small =smallest_value([45,2,56,4,87,34,622])
print(small)