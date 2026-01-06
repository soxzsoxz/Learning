weight = input("Enter your weights(kg) : ")
height_cm = input("Enter your heights(cm) : ")

weight = float(weight)
height_m = float(height_cm)/100

bmi = weight/height_m**2

print(f"Your BMI are {bmi:.2f}")

if bmi < 18.5 :
    print(f"Result : Underweight")
elif bmi >= 18.5 and bmi <= 24.9 :
    print(f"Result : Normal")
elif 25 <= bmi <= 30  :
    print(f"Result : Overweight")
elif bmi > 30 :
    print(f"Result : Fat")
