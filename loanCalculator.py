# Get loan details
amount_owed = float(input('How much do you owe (in dollars)?\n'))
apr = float(input("What is the annual percentage rate of the loan?\n"))
payment = float(input("How much will you pay off each month (in dollars)?\n"))
months = int(input("How long is the desired term (in months)?\n"))

monthly_rate = apr/100/12

for i in range(months):
    # Calculate interest
    interest_paid = amount_owed * monthly_rate

    # Add in interest
    amount_owed = amount_owed + interest_paid

    if(amount_owed - payment < 0):
        print('The last payment is: $', amount_owed)
        print('You paid off the loan in', i+1, 'months!')
        break
    
    # Make Payment
    amount_owed = amount_owed - payment

    print('Paid $', payment, ' of which $', interest_paid, ' was interest.', sep='', end=' ')
    print('Now I owe $', amount_owed, sep='')