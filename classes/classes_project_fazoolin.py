class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{name} menu available from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time=self.end_time)

    def calculate_bill(self, purchased_items):
        total = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                total += self.items[purchased_item]
            else:
                continue
        return total

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return 'The address for this store is {address}. Come on by!'.format(address = self.address)

    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
            else:
                continue
        return available_menu

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas = Menu("Take a’ Arepa", arepas_menu, 1000, 2000)

brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("Brunch", brunch_items, 1100, 1600)

# print(brunch)
# print(brunch.calculate_bill(['pancakes', 'coffee', 'home fries']))

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("Early Bird", early_bird_items, 1500, 1800)

# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("Dinner", dinner_items, 1700, 2300)

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("Kids", kids_items, 1100, 2100)

menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)
# print(flagship_store)
# print(new_installment)
# print(flagship_store.available_menus(1200))

basta = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])
# print(basta.name)
takea = Business('Take a’ Arepa', [arepas_place])

