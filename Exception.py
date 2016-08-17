try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannotdivide by zero!")
print("Finished.")

#1. ValueError will occur when the nemerator or the denominator are invalid values.
#2. ZeroDivision will occur when the denomintors value is 0.
#3. Put an error checking loop in.