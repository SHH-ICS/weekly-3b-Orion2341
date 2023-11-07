import math
pizzaSizeCost = 0
pizzaToppingsCost = {
    1: 1,
    2: 1.75,
    3: 2.5,
    4: 3.35
}
taxRate = 0.13
Large = 6
ExtraLarge = 10
print("Welcome to Juicy Pizzas!")
print("Choose your size! 'Large', or 'ExtraLarge'!")
pizzaSize = input()
if pizzaSize == "Large":
    pizzaSizeCost = Large
elif pizzaSize == "ExtraLarge":
    pizzaSizeCost = ExtraLarge
else:
    print("Invalid size of pizza")
    print("Try again!")
    exit()
print("Great! now it's time to choose your toppings")
numberOfToppings = int(input("How many toppings would you like to choose between 1-4?"))
if numberOfToppings in pizzaToppingsCost:
    toppingsCost = pizzaToppingsCost[numberOfToppings]
else:
    print("Invalid number of toppings")
    print("Try again!")
    exit()
subTotal = pizzaSizeCost + toppingsCost
tax = subTotal * taxRate
totalCost = subTotal + tax
print("Your subTotal is $",subTotal)
print("Your tax is $",tax)
print("Your totalCost is$",totalCost)