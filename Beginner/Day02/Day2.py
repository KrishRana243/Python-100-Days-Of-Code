#Tip Calculator
print("Welcome to The Tip Calculator")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people would split the bill? "))
total_tip = (tip/100)*total
total_bill = (total+total_tip)/people
print("Each person should pay:",round(total_bill,2))
