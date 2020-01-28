class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def __init__(self, price_of_item=0):
        self.price_of_item = price_of_item
        print("The cost of your vehicle is {price}".format(price=price_of_item))

    def get_rate(self):
        return self.price_of_item * 0.001


honda_insurance = VehicleInsurance(100)
print("The Insurance Rate for your car is", honda_insurance.get_rate())


class HomeInsurance(InsurancePolicy):
    def __init__(self, price_of_item):
        self.price_of_item = price_of_item

    def get_rate(self):
        return self.price_of_item * 0.00005


sandstone_insurance = HomeInsurance(500000)
print("The insurance rate for your home is", sandstone_insurance.get_rate())