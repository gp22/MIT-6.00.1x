# a program that uses bisection search to find the smallest monthly
# payment to the cent, such that we can pay off the debt within a year.

balance = 320000
annualInterestRate = 0.2
monthly_interest_rate = annualInterestRate / 12.0
#monthly_payment = 10
lower = balance / 12
upper = balance * ((1 + monthly_interest_rate)**12) / 12
epsilon = 0.01
answer = (upper + lower)/2
numGuesses = 0
#print('lower = {}'.format(lower))
#print('upper = {}'.format(upper))

def yearOfPayments(previousBalance, monthlyPayment, APR):
    """ returns the remaining balance after making 12 monthly payments
        of monthlyPayment towards previousBalance with annual percentage
        rate APR """

    for i in range(12):
        #print('balance on month {} = {}'.format(i+1, round(previousBalance, 2)))
        monthly_unpaid_balance = previousBalance - monthlyPayment
        #print('unpaid balance on month {} = {}'.format(i+1, round(monthly_unpaid_balance, 2)))
        previousBalance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    
    #print("Remaining balance: {}".format(round(previousBalance, 2)))
    return previousBalance

while yearOfPayments(balance, answer, annualInterestRate) >= epsilon or \
      yearOfPayments(balance, answer, annualInterestRate) < 0:
    numGuesses += 1
    if yearOfPayments(balance, answer, annualInterestRate) >= epsilon:
        lower = answer
    else:
        upper = answer
    answer = (upper + lower)/2
    
print('Lowest Payment: {}'.format(round(answer,2)))
print('Found in {} guesses'.format(numGuesses))
print('Balance after one year of making this payment: {}'.format(\
       round(yearOfPayments(balance, answer, annualInterestRate),2)))