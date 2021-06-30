class Truck(object):
    """A truck for sale by Jeffco Car Dealership."""

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this truck as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the truck."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 10000 - (.10 * self.miles)


def func(user_input):
    output = ""
    for char in user_input:
        output = char + output
    return output

print(func("INDIA"))


week_days = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print(week_days.count('mon'))

objects = {'python', 'coding', 'tips', 'for', 'beginners'}

print(objects)
print(len(objects))

if 'tips' in objects:
    print("These are the best Python coding tips.")
if 'Java tips' not in objects:
    print("These are the best Python coding tips not Java tips.")


names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)
