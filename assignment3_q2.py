def string_reverse(str1):

    r_str1 = ''
    index = len(str1)
    while index > 0:
        r_str1 += str1[ index - 1 ]
        index = index - 1
    return r_str1
print(string_reverse('1234abcd'))
