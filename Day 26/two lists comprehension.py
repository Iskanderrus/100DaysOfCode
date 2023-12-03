# בס״ד

def grab_the_numbers(a_txt_file) -> list:
    """
    function to take a txt file with the numbers and convert it into the list of integers
    :param a_txt_file: any txt file containing numbers in one column - a number per string
    :return: list of integers
    """
    with open(a_txt_file) as f:
        return [int(x.strip()) for x in f.readlines()]


# getting two lists
list1 = grab_the_numbers(a_txt_file='file1.txt')
list2 = grab_the_numbers(a_txt_file='file2.txt')

# searching for overlapping
overlapping = [x for x in list1 if x in list2]
print(overlapping)

# option 2
print([x for x in grab_the_numbers(a_txt_file='file1.txt') if x in grab_the_numbers(a_txt_file='file2.txt')])
