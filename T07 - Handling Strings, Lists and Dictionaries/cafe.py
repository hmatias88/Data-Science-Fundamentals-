# Practical Task 2

#Setting up the menu list
menu=["Cappucino","Latte","Sandwich","Calzone"]

#Setting up the stock dictionary
stock={"Cappucino":10,"Latte":10,"Sandwich":10,"Calzone":10}

#Setting up the price dictionary
price={"Cappucino":3.5,"Latte":3.8,"Sandwich":4.5,"Calzone":5}

#Looping through each item of the menu and working out the corresponding stock quantity and unit value to work out the total value.
for item in menu:
    item_value=stock[item] * price[item]
    print(f"The total stock value of {item} is: ${item_value}")