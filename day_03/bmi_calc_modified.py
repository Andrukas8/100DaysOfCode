weight = float(input("Your weight in kg: "))
height = float(input("Your height in  m: "))

bmi = round(weight / (height ** 2), 2)

print(f"Your bmi is {bmi}")

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")
