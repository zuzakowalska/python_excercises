a = 'assa'
b = 'asda'

def palindrome(str):
    err = 0
    str_len = len(str)-1
    for i in range(0, str_len):
        if str[i] != str[str_len-i]:
            err += 1
    if err > 0:
        print(str + " is not a palindrome")
    else:
        print(str + " is a palindrome")
palindrome(a)
palindrome(b)