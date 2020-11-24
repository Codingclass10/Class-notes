name = input("Hello! It is me the computer. What is your name? : ")
print("hello",name)
weight=float(input("Enter your weight(kg): "))
height=float(input("Enter your height(m): "))
BMI= weight/height**2
if BMI >25:
	print("Your BMI is:", BMI)
	print(name,", you are overweight. Need to start working out.")
elif BMI>18.5:
	print("Your BMI is:", BMI)
	print(name,", you are healthy.Great maintaining.")
else:
	print("Your BMI is:", BMI)
	print(name,", you are underweight. You really need to consider your diet.")