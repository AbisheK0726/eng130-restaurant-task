# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

#create a dictionary of menu items

menu = {1: "steak", 2: "pizza", 3: "salad", 4: "chicken", 5: "pasta", 6: "tofu", 7: "burger", 8: "sandwich", 9: "soup", 10: "ice cream"}

print ("\nWelcome to the restaurant! Here is our menu: ")
for key, value in menu.items():
    print (key, "-" , value)

#ask user up to 3 orders
order = {}

while True:
        
    order_number = int(input("What would you like to order? "))
    order[order_number] = menu[order_number]
    
    if len(order) == 3:
        print ("Your order is: ")
        for key, value in order.items():
            print (key, "-" , value)
        break
    
    order_again = input("Would you like to order anything else? (yes/no) ")
    if order_again == "yes":
        continue
    elif order_again == "no":
        print("=====================================")
        print ("Your order is: ")
        for key, value in order.items():
            print (key, "-" , value)
            print("=====================================")
        break
    else:
        print ("Please enter yes or no")
        continue
        
