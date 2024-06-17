h = float(input("Enter your height in m :  "))
w = float(input("Enter your weight in kg :"))

a = w/(h*h)

if a<18.5:
    print("The person falls in UNDERWEIGHT category")
elif a<=24.9:
    print(" The person falls in NORMAL WEIGHT category ")
elif a<=29.9:
    print (" The person falls in OVERWEIGHT category ") 
else:
    print("The person falls in OBESE category")           