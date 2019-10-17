# This code is linked with 'Challenge_16.py'.


def max_finder(a_list):

    max_in_list = a_list[0]
    for index in range(1, len(a_list)):

        if a_list[index] > max_in_list:
            max_in_list = a_list[index]

    return max_in_list
