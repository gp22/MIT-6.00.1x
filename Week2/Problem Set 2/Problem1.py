# Write a program to calculate the credit card balance after one year if
# a person only pays the minimum monthly payment required by the credit
# card company each month.

balance = 484
annualInterestRate = .2
monthlyPaymentRate = .04
previous_balance = balance
monthly_interest_rate = annualInterestRate / 12.0

for i in range(12):
    minimum_monthly_payment = monthlyPaymentRate * previous_balance
    monthly_unpaid_balance = previous_balance - minimum_monthly_payment
    previous_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    
print("Remaining balance: {}".format(round(previous_balance, 2)))