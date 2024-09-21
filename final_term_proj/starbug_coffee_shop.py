def readMenu(fn="CoffeeMenu01.txt"):
    with open(fn) as fd:
        return fd.read()


class CupOfCoffee:
    def __init__(self, coffee_type, drinking_type, price):
        self.coffee_type = coffee_type
        self.drinking_type = drinking_type
        self.price = price
        self.add_on = []

    def set_add_on(self, one_add_on, one_add_on_price):
        self.add_on.append(one_add_on)
        self.price += one_add_on_price

    def get_addon(self):
        return self.add_on

    def get_coffee_type(self):
        return self.coffee_type

    def __repr__(self):
        if len(self.add_on) > 1:
            k = ", ".join(self.add_on[:-1])
            return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {k} and {self.add_on[-1]}, {self.price} baht."
        elif len(self.add_on) == 1:
            return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {self.add_on[0]}, {self.price} baht."
        return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with no add on, {self.price} baht."


class CustomerBill:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_ordered_coffee(self, aCupOfCoffeeObject):
        self.orders.append(aCupOfCoffeeObject)

    def receipt(self):
        name = f"Kun {self.name}'s Receipt"
        rep = ""
        rep += "++++++++++++++++++++++++++++++++\n"
        rep += "      CPE38 **StarBUG Cafe    \n"
        rep += f"{name:^32}\n"
        rep += "++++++++++++++++++++++++++++++++\n"
        rep += "Description                Price\n"
        total_price = sum([order.price for order in self.orders])
        for order in self.orders:
            coffee = f"{order.drinking_type} {order.coffee_type}"
            rep += f"{coffee:<26} {order.price:>5}\n"
            for addon in order.get_addon():
                rep += f" + {addon}\n"
            rep += "\n"
        rep += f"{'Total':<26} {total_price:>5,}\n"
        rep += "++++++++++++++++++++++++++++++++\n"
        rep += " Thank you, please come back :) \n"
        rep += "++++++++++++++++++++++++++++++++\n"

        return rep


coffee_menu_filename = "CoffeeMenu01.txt"
addon_menu_filename = "CoffeeMenuAddOn01.txt"
# coffee_menu_filename = input("Enter Coffee Menu available today (filename): ")
coffee_menu_CSV = readMenu(coffee_menu_filename)
# addon_menu_filename = input("Enter AddOn Menu available today (filename): ")
add_on_menu_CSV = readMenu(addon_menu_filename)


def runStarBUGcafe_main():
    coffee_menu = [
        [y.strip() for y in x.split(",") if y.strip()]
        for x in coffee_menu_CSV.splitlines()
        if x
    ]
    addon_menu = [
        [y.strip() for y in x.split(",") if y.strip()]
        for x in add_on_menu_CSV.splitlines()
        if x
    ]
    coffee_menu = [x for x in coffee_menu if len(x)]
    addon_menu = [x for x in addon_menu if len(x)]

    drinking = {"h": "Hot", "c": "Cold", "f": "Frappe"}
    sold = []
    while 1:
        render_menu(coffee_menu, addon_menu)
        customer_name = input("Enter customer's name: ")
        customer = CustomerBill(customer_name)
        if customer_name == "Good Day":
            closed(sold)
            break
        cups = input("How many cups of coffee to order? ")
        while not cups.isnumeric() or cups == "0":
            print(" ERROR: Invalid input!")
            cups = input("How many cups of coffee to order? ")
        for i in range(int(cups)):
            while 1:
                coffee_type = input(f"Cup #{i+1}, please select type of coffee: ")
                if (
                    not coffee_type.isnumeric()
                    or int(coffee_type) > len(coffee_menu)
                    or int(coffee_type) <= 0
                ):
                    print(" ERROR: Invalid input!")
                    continue
                coffee = coffee_menu[int(coffee_type) - 1]
                drinking_types = [x for x in enumerate(coffee[1:]) if x[1] != "0"]
                k = "hcf"
                if len(drinking_types) == 1:
                    price = int(drinking_types[0][1])
                    types = drinking[k[drinking_types[0][0]]]
                    cup = CupOfCoffee(coffee[0], types, price)
                    select_addon(cup, i, addon_menu)
                    customer.add_ordered_coffee(cup)
                    sold.append((coffee_type, cup))
                    print(cup)
                    break
                else:
                    option = ",".join(["HCF"[i] for i, x in drinking_types])
                    drink_type = "h"
                    while 1:
                        drink_type = input(
                            f"Cup #{i+1}, please select drinking type ({option}): "
                        )
                        if drink_type.lower() not in "".join(
                            ["hcf"[i] for i, x in drinking_types]
                        ):
                            print(" ERROR: Invalid input!")
                            continue
                        break
                    index = k.index(drink_type.lower())
                    price = int(drinking_types[index][1])
                    types = drinking[k[drinking_types[index][0]]]
                    cup = CupOfCoffee(coffee[0], types, price)
                    select_addon(cup, i, addon_menu)
                    customer.add_ordered_coffee(cup)
                    sold.append((coffee_type, cup))
                    print(cup)
                    break
        print(customer.receipt())


def render_menu(coffee_menu, addon_menu):
    print("Welcome to CPE38 **StarBUG Cafe!")
    print("+++++++++++++ MENU +++++++++++++")
    print("Coffee         Hot  Cold  Frappe")
    for i, menu in enumerate(coffee_menu):
        print(f"{i+1}.{menu[0]:<12} {menu[1]:>3} {menu[2]:>5} {menu[3]:>5}")
    print("++++++++++++ ADD-ON ++++++++++++")
    for i, menu in enumerate(addon_menu):
        print(f"{i+1}.{menu[0]:<19} {menu[1]:>2}")
    print("++++++++++++++++++++++++++++++++")
    print()


def select_addon(cup, i, addon_menu):
    exit = False
    addon_list = []
    for j in range(len(addon_menu)):
        while 1:
            addon = input(f"Cup #{i+1}, please select add on (enter for exit): ")
            if addon == "":
                exit = True
                break
            if (
                not addon.isnumeric()
                or int(addon) > len(addon_menu)
                or int(addon) <= 0
                or addon in addon_list
            ):
                print(" ERROR: Invalid input!")
                continue
            addon_list.append(addon)
            addon = addon_menu[int(addon) - 1]
            addon_type = addon[0]
            addon_price = int(addon[1])
            cup.set_add_on(addon_type, addon_price)
            break
        if exit:
            break


def closed(sold):
    sold_amount = sum([x.price for i, x in sold])
    coffee_types = {}
    coffee_list = []
    for i, x in sold:
        if not x.get_coffee_type() in coffee_types:
            coffee_types[x.get_coffee_type()] = 1
            coffee_list.append((i, x.get_coffee_type()))
        else:
            coffee_types[x.get_coffee_type()] += 1
    print("++++++++++++++++++++++++++++++++")
    print("      CPE38 **StarBUG Cafe    ")
    print("  Report for Coffee sold today")
    print("++++++++++++++++++++++++++++++++")
    coffee_list.sort(key=lambda x: x[0])
    for i, coffee in coffee_list:
        cups = coffee_types[coffee]
        if cups > 1:
            suffix = "cups"
        else:
            suffix = "cup"
        print(f" {coffee:<22} {cups:>2} {suffix}")
    print()
    print(f"{'Total sold amount':<21} {sold_amount:>5,} baht")
    print("++++++++++++++++++++++++++++++++")
    print("       What's a good day!     ")
    print("++++++++++++++++++++++++++++++++")
    print()


runStarBUGcafe_main()
