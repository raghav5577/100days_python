print("Welcome to the tip calculator!")
bill=float(input("What si the total bill? "))
tip=int(input("What percentage of tip would you like to give? 10, 12, 15 ? "))
persons=int(input("How many people to split the bill?  "))
total=(tip/100 * bill +bill)/5
final_amount=round(total,2)
print("The bill amount to be given by each person is",final_amount)