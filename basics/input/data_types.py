name = input("What is your name human? ")
age = int(input("What is your age human? "))
height = float(input("What is your height in meters human? "))
weight = int(input("What is your weight in kilograms human? "))
height_squared = height * height
bmi = weight / height_squared
print(name,"you are",age,"years old and your bmi is {:0.2f}".format(bmi))