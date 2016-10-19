# a program that calculates the minimum fixed monthly payment needed in
# order pay off a credit card balance within 12 months. By a fixed
# monthly payment, we mean a single number which does not change each month,
# but instead is a constant amount that will be paid each month (in multiples
# of 10).

balance = 3926
annualInterestRate = 0.2
monthly_payment = 10

def yearOfPayments(previousBalance, monthlyPayment, APR):
    """ returns the remaining balance after making 12 monthly payments
        of monthlyPayment towards previousBalance with annual percentage
        rate APR """
    monthly_interest_rate = APR / 12.0

    for i in range(12):
        #print('balance on month {} = {}'.format(i+1, round(previousBalance, 2)))
        monthly_unpaid_balance = previousBalance - monthlyPayment
        #print('unpaid balance on month {} = {}'.format(i+1, round(monthly_unpaid_balance, 2)))
        previousBalance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    
    #print("Remaining balance: {}".format(round(previousBalance, 2)))
    return previousBalance
    
while yearOfPayments(balance, monthly_payment, annualInterestRate) >= 0:
    monthly_payment += 10

print("Lowest Payment: {}".format(monthly_payment))