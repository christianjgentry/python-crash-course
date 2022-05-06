#get loan details

dollars_owed = float(input("How much money do you owe in dollars?\n")) #50,000
apr = float(input("What is the APR? \n")) #3%)
payment = float(input("What will your monthly payment be in dollars?\n")) #1,000
months = int(input("How many months do you want to see results for? \n")) #24

#divide apr by 100 and then by 12 to make it a monthly percent
monthrate = apr/100/12

for i in range(months):
    #add interest
    interest_paid = dollars_owed * monthrate
    dollars_owed = dollars_owed + interest_paid

    if (dollars_owed - payment < 0):
        print(f"The last payment is {dollars_owed}.")
        print(f"You paid off the loan in {i+1} months.")
        break

    #make payment
    dollars_owed = dollars_owed - payment

    #print the results after this month
    print(f"Paid {payment}, of which, {interest_paid} was interest.")
    print(f"Now I owe {dollars_owed}.")

