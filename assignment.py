import math
pizzaCost = 0
subTotal = 0
tax = 0
totalCost = 0
Large = 6
ExtraLarge = 10
print("Welcome to Juicy Pizzas!")
print("Choose your size! 'Large', or 'Extra Large'!")
pizzaSize = input()
if pizzaSize == "Large":
    pizzaCost = Large
elif pizzaSize == "ExtraLarge":
    pizzaCost = ExtraLarge
print("Great! now it's time to choose your toppings")
print("How many toppings would you like between 1 and 4?")
