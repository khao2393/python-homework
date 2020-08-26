# Unit 2 | PyRamen

import csv
import pathlib

menu = []
sales = []
menu_file = pathlib.Path('C:/Users/14259/Desktop/Kevin/UW/Python Unit 2 HW/menu_data.csv')
sales_file = pathlib.Path('C:/Users/14259/Desktop/Kevin/UW/Python Unit 2 HW/sales_data.csv')


with open(menu_file, 'r') as m:
    menu_data = csv.reader(m)
    next(menu_data)
    for row in menu_data:
        menu.append(row)

with open(sales_file, 'r') as s:
    sales_data = csv.reader(s)
    next(sales_data)
    for row in sales_data:
        sales.append(row)

report = {}

for a,b,c,quantity,sales_item in sales:
    quantity = int(quantity)
    if sales_item not in report:
        report[sales_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0,
"04-profit": 0,}
        report[sales_item]['01-count'] += quantity
    elif sales_item in report:
        report[sales_item]['01-count'] += quantity
    for menu_item,d,e,price,cost in menu:
        price = float(price)
        cost = float(cost)
        if menu_item == sales_item:
            profit = price - cost
            report[sales_item]['02-revenue'] += price * quantity
            report[sales_item]['03-cogs'] += cost * quantity
            report[sales_item]['04-profit'] += profit * quantity
        #else:
           #print(f'{menu_item} does not equal {sales_item}! NO MATCH!')



    
        

    


        
    


    
    
    
        
        
        
        
    

