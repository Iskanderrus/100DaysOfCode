# Write a simple BMI calculator utilizing the formula:
# bmi = kg / m**
# round the result to the whole number

height = input('What is your height in m?\n')
weight = input('What is your weight in kg?\n')
bmi = int(float(weight.replace(',', '.')) / float(height.replace(',', '.'))**2)

if bmi < 18.5:
    print(f'Your BMI is {bmi}.\nYou have underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}.\nYou have normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}.\nYou have overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}.\nYou are obese.')
else:
    print(f'Your BMI is {bmi}.\nYou are clinically obese.')