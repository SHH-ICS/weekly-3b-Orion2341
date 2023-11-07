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
print("How many toppings would you like to choose?")
print("one, two, three, or four")
numberOfToppings = input()
if numberOfToppings == "one":
    pizzaToppingsCost + one
elif numberOfToppings == "two":
    pizzaToppingsCost + two
elif numberOfToppings == "three":
    pizzaToppingsCost + three
elif numberOfToppings == "four":
    pizzaToppingsCost + four
else:
    print("Invalid number of toppings")
    print("Try again!")
    exit()
subTotal = pizzaSizeCost + pizzaToppingsCost
tax = subTotal * taxRate
totalCost = subTotal + taxRate
print(subTotal)
print(tax)
print(totalCost)