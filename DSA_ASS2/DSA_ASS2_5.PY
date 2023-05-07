def sort_dict_strings(lst):
    # Define the order in which to compare the strings
    order = 'abcdefghijklmnopqrstuvwxyz'

    # Define a custom key function that returns the index of each character in the order string
    key_func = lambda s: [order.index(c) for c in s]

    # Sort the list using the custom key function
    return sorted(lst, key=key_func)
