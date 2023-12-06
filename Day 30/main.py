# בס״ד

fruits = ['Apple', 'Pear', 'Orange']


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print(f'Code has an error: {error_message}. Looks like the index is wrong.')
    else:
        print(fruit + 'pie')


make_pie(4)
