expenses = [10.50, 8, 6.98, 15, 3]

# FOR LOOP METHOD

sum = 0

for expense in expenses:
    sum += expense

# you can concatenate using commas, and specify separators
print("You spent $", sum, sep = '') 


#SUM FUNCTION METHOD
# a cool feature of Python is the sum function which reduces the need for a for loop!

total = round(sum(expenses), 2) #To round a decimal you use, round(number, decimal places)

print("You spent $", total, sep='')



#ADDING INPUT TO THE MIX
total = 0
expenses = []

# get input from the user for number of expenses
num_expenses = int(input("Enter # of expenses:"))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent $", total, sep='')
