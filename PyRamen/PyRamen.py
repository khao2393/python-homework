{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Unit 2 | PyRamen\n",
    "\n",
    "import csv\n",
    "\n",
    "menu = []\n",
    "sales = []\n",
    "\n",
    "with open('C:\\\\Users\\\\14259\\\\Desktop\\\\Kevin\\\\UW\\\\Python Unit 2 HW\\\\menu_data.csv') as m:\n",
    "    menu_data = csv.reader(m)\n",
    "    next(menu_data)\n",
    "    for row in menu_data:\n",
    "        menu.append(row)\n",
    "\n",
    "with open('C:\\\\Users\\\\14259\\\\Desktop\\\\Kevin\\\\UW\\\\Python Unit 2 HW\\\\sales_data.csv') as s:\n",
    "    sales_data = csv.reader(s)\n",
    "    next(sales_data)\n",
    "    for row in sales_data:\n",
    "        sales.append(row)\n",
    "\n",
    "report = {}\n",
    "\n",
    "for a,b,c,quantity,sales_item in sales:\n",
    "    quantity = int(quantity)\n",
    "    if sales_item not in report:\n",
    "        report[sales_item] = {\"01-count\": 0, \"02-revenue\": 0, \"03-cogs\": 0,\n",
    "\"04-profit\": 0,}\n",
    "        report[sales_item]['01-count'] += quantity\n",
    "    elif sales_item in report:\n",
    "        report[sales_item]['01-count'] += quantity\n",
    "    for menu_item,d,e,price,cost in menu:\n",
    "        price = float(price)\n",
    "        cost = float(cost)\n",
    "        if menu_item == sales_item:\n",
    "            profit = price - cost\n",
    "            report[sales_item]['02-revenue'] += price * quantity\n",
    "            report[sales_item]['03-cogs'] += cost * quantity\n",
    "            report[sales_item]['04-profit'] += profit * quantity\n",
    "        #else:\n",
    "           #print(f'{menu_item} does not equal {sales_item}! NO MATCH!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
