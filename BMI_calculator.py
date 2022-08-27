user_weight = float( input("Please enter your current weight in kg: ") )
user_height = float( input("Please enter your current height in m: ") )
bmi = user_weight/(user_height**2)
bmi_to_one_dp = round(bmi, 1)
print("Your current BMI is " + str( bmi_to_one_dp ) )
# To the print the outcome
if bmi_to_one_dp < 18.5:
  print("You are underweight")
elif bmi_to_one_dp < 25:
  print("You have normal weight")
elif bmi_to_one_dp < 30:
  print("You are overweight")
elif bmi_to_one_dp < 35:
  print("You are Obese")
else:
  print("You are clinically Obese")
