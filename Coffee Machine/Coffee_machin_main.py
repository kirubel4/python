from Resource import MENU,resources,logo

count_money = 0

def calculating():
    """Calculate the use of resource"""

    if ask == "espresso":
        for i in resources:
            resources[i]=resources[i]-MENU["espresso"]["ingredient"][i]
    elif ask == "latte":
        for i in resources:
            resources[i] = resources[i]-MENU["latte"]["ingredient"][i]
    elif ask == "cappuccino":
        for i in resources:
            resources[i]= resources[i]-MENU["cappuccino"]["ingredient"][i]


def check():
    """Check if there is enough resource to work."""

    for keys, values in resources.items():
        if values < MENU[ask]["ingredient"][keys]:
            print("There is no enough "+keys)
            again()
        elif values < MENU[ask]["ingredient"][keys]:
            print("There is no enough "+keys)
            again()
        elif values < MENU[ask]["ingredient"][keys]:
            print("There is no enough "+keys)
            again()
    global count_money
    count_money = count_money + MENU[ask]["cost"]


def report():
    """Tell the amount of resource."""

    print(f"water: {resources['Water']}ml")
    print(f"coffee: {resources['cCoffee']}g")
    print(f"milk: {resources['Milk']}ml")
    print(f"${count_money}")


def insert_coin():
    """Ask the user to insert coin."""
    global Penny,Dime,Nickel,Quarter
    print("please insert coin!")
    Penny = float(input("How many Penny? "))
    Dime = float(input("How many Dime? "))
    Nickel = float(input("How many Nickel? "))
    Quarter = float(input("How many Quarter? "))


def  sum_coin():
    """"Add the coin that the customer inserts."""

    global Penny,Dime,Nickel,Quarter
    Penny = 0.01*Penny
    Dime = 0.10*Dime
    Nickel = 0.05 * Nickel
    Quarter = 0.25 *Quarter
    sum = Penny +Dime +Nickel+  Quarter
    return float(sum)


def changes():
    """Tell the amount of coin inserts and calculate change if there is."""

    temp = sum_coin()
    print("Your deposit money was $"+str(temp))
    change = temp - MENU[ask]["cost"]
    change_result = round(change, 2)
    if temp > MENU[ask]["cost"]:
        print("Here is $"+str(change_result)+" in change.")
        print("Here is your",ask+logo)
    else:
        print("Sorry the coin is not enough!")
        again()

def analysis():
    """This holds the other methods by order"""

    check()
    calculating()
    insert_coin()
    changes()
    again()


def again():
    """Ask the customer and provide service."""

    global ask
    ask = input("What would you like? (espresso / latte / cappuccino): ").lower()
    if ask == "report":
        report()
        again()
    elif ask == "off":
        print("Thank you for using the coffee machine.")
    elif ask == "espresso":
        analysis()
    elif ask == "cappuccino":
        analysis()
    elif ask == "latte":
        analysis()
    else:
        again()


def ask_customer():
    """Ask the customer whether to use the coffee machine or not."""
    order = input("Would you like to use the coffee machine? type 'yes' to use or 'no' to skip. ").lower()
    if order == "yes":
        again()
    elif order == "no":
        print("Thank you for using")

ask_customer()
