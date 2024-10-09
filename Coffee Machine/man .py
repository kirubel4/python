from Resource import MENU,resources,logo
Penny_coin = 0.01
Dime_coin = 0.10
Nickel_coin = 0.05
Quarter_coin = 0.25
count_money = 0

def calculating():
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
    for keys, values in resources.items():
        if values < MENU[ask]["ingredient"][keys]:
            print("there is no enough "+keys)
            again()
        elif values < MENU[ask]["ingredient"][keys]:
            print("there is no enough "+keys)
            again()
        elif values < MENU[ask]["ingredient"][keys]:
            print("there is no enough "+keys)
            again()
    global count_money
    count_money = count_money + MENU[ask]["cost"]


def report():
    print("water: "+str(resources["water"])+"ml")
    print("coffee: "+str(resources["coffee"])+"g")
    print("milk: "+str(resources["milk"])+"ml")
    print("$"+str(count_money))


def insert_coin():
    global Penny,Dime,Nickel,Quarter
    print("please insert coin!")
    Penny = float(input("How many Penny? "))
    Dime = float(input("How many Dime? "))
    Nickel = float(input("How many Nickel? "))
    Quarter = float(input("How many Quarter? "))


def  sum_coin():
    global Penny,Dime,Nickel,Quarter
    global Penny_coin,Dime_coin,Nickel_coin,Quarter_coin
    Penny = Penny_coin*Penny
    Dime = Dime_coin*Dime
    Nickel = Nickel_coin * Nickel
    Quarter = Quarter_coin *Quarter
    sum = Penny +Dime +Nickel+  Quarter
    return float(sum)


def changes():
    temp = sum_coin()
    print("Your deposit mony $"+str(temp))
    change = temp - MENU[ask]["cost"]
    change_result = round(change, 2)
    if temp > MENU[ask]["cost"]:
        print("Here is $"+str(change_result)+" in change.")
        print("Here is your",ask+logo)
    else:
        print("Sorry the coin is not enough!")
        again()

def analysis():
    check()
    calculating()
    insert_coin()
    changes()
    again()


def again():
    global ask
    ask = input("what would you like? (espresso / latte / cappuccino / no): ").lower()
    if ask == "report":
        report()
        again()
    elif ask== "no":
        print("Thank you for using the coffee machine.")
    elif ask == "espresso":
        analysis()
    elif ask == "cappuccino":
        analysis()
    elif ask == "latte":
        analysis()


def ask_customer():
    order = input("Would you like to use the coffee machine? type 'yes' to use or 'no' to skip. ").lower()
    if order == "yes":
        again()
    elif order == "no":
        print("Thank you for using")

ask_customer()
