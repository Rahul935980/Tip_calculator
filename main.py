#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line

print('Welcome to tip calculator')
a = float(input('Enter the bill amount:'))
b = int(input('how much percent tip do you want to give:'))
tip = b/100*a 
total_bill = a + tip
people = int(input("How many people do you want to split the bill:"))
split_amount = total_bill / people
final_amount = "{:.2f}".format(split_amount)
print(f'Each persom has to pay rupees {final_amount}')