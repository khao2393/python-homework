# Unit 2 | PyBank
# Kevin Hao

# Importing my libs
import csv
import pathlib

# Defining my empty list and dictionaries

file = pathlib.Path('C:/Users/14259/Desktop/Kevin/UW/Python Unit 2 HW/budget_data.csv')
changes = []
profits = []
dict = {}

# Opening my budget data csv file and reading it using my file path
with open(file, 'r') as f:
    # read the csv with csv reader and skip the first line
    budget_data = csv.reader(f)
    next(budget_data)
    # loop through the sheet and adding the data to my profits list and dictionary
    for month, money in budget_data:
        money = int(money)
        profits.append(money)
        dict[month] = money
        
# the total profit and the total months by using the profits list
total_profit = sum(profits)
total_months = len(profits)

# loop through the profits list and making a new list for every change in the profits
for i in range(len(profits)-1):
    # this subtracts the new data with the old data
    changes.append(profits[i+1] - profits[i]) 

# this calculates the avg change
avg_change = sum(changes)/len(changes) 

# defining my variables for the loop
increase = 0
decrease = 0
count = 0

# loop through the dictionary
for key in dict:
    # this keeps track of the new profit $
    number1 = dict[key]
    # this if statement is only for the first iteration of the loop. No numbers to compare.
    if count == 0:
        # this keeps track of the old profit $
        number2 = dict[key]
        count += 1
        # after the first iteration, it will only go through this loop
    elif count > 0:
        # calculate the difference between the new and old profit $
        difference = number1 - number2
        # if the difference is lower than the decrease, it will keep track of the month and the decrease amount
        if difference < decrease:
            decrease = difference
            decrease_month = key
            number2 = dict[key]
        # if the difference is bigger than the increase, it will keep track of the month and the increase amount
        elif difference > increase:
            increase = difference
            increase_month = key
            number2 = dict[key]
        # if the difference is not bigger or lower than the differences then it will just keep track of the old profit $
        else:
            number2 = dict[key]

# Output the results in the terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: {avg_change:0.2f}')
print(f'Greatest Increase in Profits: {increase_month} (${increase})')
print(f'Greatest Decrease in Profits: {decrease_month} (${decrease})')

# Output the results onto a text file 
with open('final_script.txt','w') as f:
    f.write('Financial Analysis\n')
    f.write('----------------------------\n')
    f.write(f'Total Months: {total_months}\n')
    f.write(f'Total: ${total_profit}\n')
    f.write(f'Average Change: {avg_change:0.2f}\n')
    f.write(f'Greatest Increase in Profits: {increase_month} (${increase})\n')
    f.write(f'Greatest Decrease in Profits: {decrease_month} (${decrease})\n')

        
        
        
        
