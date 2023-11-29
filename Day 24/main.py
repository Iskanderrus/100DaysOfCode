with open('my_data.txt', 'r+') as f:
    contents = f.readlines()
    for row in contents:
        print(row)