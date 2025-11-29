# Input principal, rate, and time
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100
# Print the interest
print("Simple Interest:", simple_interest)