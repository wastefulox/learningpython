class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        if self.owner.is_museum == True:
            return "{artist}. \"{title}\". {year}, {medium}, {owner_name}, {owner_location}.".format(artist = self.artist, title = self.title, year = self.year, medium = self.medium, owner_name = self.owner.name, owner_location = self.owner.location)
        else:
            return "{artist}. \"{title}\". {year}, {medium}, {owner_name}, Private Collection.".format(artist = self.artist, title = self.title, year = self.year, medium = self.medium, owner_name = self.owner.name)

class Marketplace:
    def __init__(self, listings):
        self.listings = listings

    def __repr__(self):
        return "Welcome to the marketplace."

    def add_listing(self, new_listing):
        counter = 0
        for listing in self.listings:
            if listing == new_listing:
                counter += 1
                continue
            else:
                counter += 0
                continue
        if counter == 0:
            self.listings.append(new_listing)
        else:
            pass

    def remove_listing(self, existing_listing):
        for listing in self.listings:
            if listing == existing_listing:
                self.listings.remove(existing_listing)
                return str(existing_listing), "removed."
            else:
                continue

    def show_listing(self):
        x = []
        for listing in self.listings:
            x.append(str(listing))
        return "\n".join(x)

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self.name)
            veneer.add_listing(new_listing)
        else:
            return "seller not authorized to sell this art."

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artwork:
                    art_listing = listing
                    artwork.owner  = self
                    veneer.remove_listing(art_listing)
                    break
                else:
                    continue
        else:
            return "you do not have permission to buy your own art."



class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{art}: {price}".format(art=self.art, price=self.price)

veneer = Marketplace([])
edytta = Client('Edytta Halpirt', 'New York', False)
moma = Client('The MOMA', 'New York', True)
kyra = Client('Kyra Sturdevant', 'South Carolina', False)
girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)
giraffe_with_glasses = Art('Vogel, Donna', 'Giraffe with Glasses', 'watercolor on canvas', 2019, kyra)

# selling artwork
edytta.sell_artwork(girl_with_mandolin,6000000)
print(veneer.show_listing())
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
print(veneer.show_listing())

# prints the painting info
# print(girl_with_mandolin)
# print(giraffe_with_glasses)

# mats_gallary = Marketplace([girl_with_mandolin])
# print(mats_gallary.show_listing(), "\n")
# mats_gallary.add_listing(giraffe_with_glasses)
# print(mats_gallary.show_listing(), "\n")
# mats_gallary.remove_listing(girl_with_mandolin)
# print(mats_gallary.show_listing(), "\n")