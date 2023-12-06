# בס״ד

fruits = ['Apple', 'Pear', 'Orange']


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print(f'Code has an error: {error_message}. Looks like the index {index} is wrong.')
    else:
        print(fruit + 'pie')


make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes += 0
print(f'Total number of likes: {total_likes}')
