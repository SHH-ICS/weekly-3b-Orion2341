<!DOCTYPE html>
<html>
    <body>
    <?php
        $pizzaSizeCost = 0
        $pizzaToppingsCost = [
            1 => 1,
            2 => 1.75,
            3 => 2.5,
            4 => 3.35
        ];
        $taxRate = 0.13;
        $Large = 6;
        $ExtraLarge = 10;
        echo("Welcome to Juicy Pizzas!")
        $pizzaSize = $_POST['Choose your size, "Large", or "ExtraLarge"'];
        if ($pizzaSize == "Large") {
            $pizzaSizeCost = $Large;
        } elseif ($pizzaSize == "ExtraLarge") {
            $pizzaSizeCost = $ExtraLarge;
        } else {
            echo("Invalid size of pizza")
            echo("Try again")
            exit();
        }
        echo("Great! now it's time to choose your toppings")
        $numberOfToppings = $_POST['How many toppings would you like to choose between 1-4?'];
        if (array_key_exists($numberOfToppings, $pizzaToppingsCost)) {
            $toppingsCost = $pizzaToppingsCost[$numberOfToppings];
        } else {
            echo("Invalid number of toppings")
            echo("Try again")
            exit();
        }
        $subTotal = $pizzaSizeCost + $pizzaToppingsCost;
        $tax = $subTotal * $taxRate;
        $totalCost = $subTotal + $taxRate;
        echo("Your subTotal is $", $subTotal);
        echo("Your tax is $", $tax);
        echo("Your totalCost is $", $totalCost);
    ?>
    </body>
</html>