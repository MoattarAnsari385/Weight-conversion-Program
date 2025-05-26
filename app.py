# Python Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or L): ").strip().upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {weight:.2f} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {weight:.2f} {unit}")
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")

