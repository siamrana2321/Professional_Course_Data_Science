################ 11. Calculate compound interest ################
P = float(input("Enter principal amount: "))
T = float(input("Enter time period (in years): "))
R = float(input("Enter rate of interest (per annum): "))

compound_interest = P * (1 + R/100) ** T - P

print("Compound interest:", compound_interest)