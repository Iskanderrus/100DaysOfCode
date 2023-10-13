print('Welcome to the Love Calculator!')
name1 = input('What is your name?\n').lower()
name2 = input('What is your partner\'s name?\n').lower()

word1 = 'true'
word2 = 'love'

num1 = 0
num2 = 0

for x in word1:
    num1 += (name1 + name2).count(x)

for x in word2:
    num2 += (name1 + name2).count(x)

score = int(str(num1) + str(num2))


if score < 10 or score > 90:
    print(f'Your love score is {score}, you go together like coke and mentos.')
elif 50 >= score >= 40:
    print(f'Your love score is {score}, you are alright together.')
else:
    print(f'Your love score is {score}.')