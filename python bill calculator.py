#
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10%, 12%, 0r 15%?" )
calc_percentage = (int(percentage)/100) + 1
number_of_people = input("How many people to split the bill?" )
Total_bill_per_person = (float(total_bill)* float(calc_percentage))/int(number_of_people)
bill_per_person = "{:.2f}".format(Total_bill_per_person)
print(f"Each person should pay: ${bill_per_person}")