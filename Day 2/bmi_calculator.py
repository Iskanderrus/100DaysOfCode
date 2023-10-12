# Write a simple BMI calculator utilizing the formula:
# bmi = kg / m**
# round the result to the whole number

height = input('What is your height in m?\n')
weight = input('What is your weight in kg?\n')
print(f"Your BMI is {int(float(weight.replace(',', '.')) / float(height.replace(',', '.'))**2)}")