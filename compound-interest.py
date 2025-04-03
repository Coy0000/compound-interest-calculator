principle=0
interest=0
time=0


while True:
  principle = float(input("Enter the principle amount:"))
  if principle < 0:
     print("Principle amount cannot be smaller than 0")
  else:
     break


while True:
    interest = float(input("Enter the interest rate:"))
    if interest < 0:
        print("interest rate cannot be smaller than 0")
    else: 
        break


while True:
   time = float(input("Enter the time (in years):"))
   if time < 0:
       print("Time cannot be smaller than 0")
   else: 
        break

compound_interest = principle * pow((1+interest/100),time)
print(f"The compound interest in {time} years, with {interest}% interest is {compound_interest}")
