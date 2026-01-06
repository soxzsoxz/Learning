def calculate_bmi(w,h):
    bmi = w/h**2
    return bmi
    
weight = input("Enter your weights(kg) : ")
height_cm = input("Enter your heights(cm) : ")

weight = float(weight)
height_m = float(height_cm)/100

bmi = calculate_bmi(weight,height_m)
print(f"{bmi:.2f}")


    