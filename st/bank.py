#get savings from user
savings = float(input("Enter your savings: "))
#set interest rate at 2 percent
interest_rate = 0.02
#calculate the amount of money in the account after one year
account_value = savings * (1 + interest_rate)
#calculate the amount of money in the account after two years
account_value2 = savings * (1 + interest_rate) * (1 + interest_rate)
#calculate the amount of money in the account after three years
account_value3 = savings * (1 + interest_rate) * (1 + interest_rate) * (1 + interest_rate)
#print out the result
print("After one year, your account value will be " + str(account_value))
print("After two years, your account value will be " + str(account_value2))
print("After three years, your account value will be " + str(account_value3))
