pizzas = ['pepperoni','buffalo chicken','cheese']
for pizza in pizzas:
    print(f"{pizza.title()} pizza is my favorite pizza")
print("I really love pizza!")

animals = ['seaturtle','seagull','sealion']
for animal in animals:
    print(f"A {animal.title()} would make a great pet")
print("Any of these animals would make a great pet!")

numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','18','19','20']
for number in numbers:
    print(f"{number.title()}")

def display_message():
    """Display a simple message."""
    print("This chapter we're learning aboout functions")

display_message()

def favorite_book():
    """Display my favorite book."""
    print("One of my favorite books is Diary of a Wimpy Kid")

favorite_book()

def make_shirt(shirt_size, shirt_text):
    """Display shirt"""
    print(f"/nThe shirt size is {shirt_size} and the shirt says {shirt_text}")

make_shirt('large', 'I love Python!')
make_shirt('medium', 'I love Python!')
make_shirt('large', 'I hate Python!')

def describe_city(city,country):
    """Name a city and the country"""
    print(f"/n{city} is in {country}")

describe_city('Las Vegas', 'US')
describe_city('New York City', 'US')
describe_city('Georgetown', 'Guyana')

def city_country(city,country):
    """Name a city and the country"""
    print(f"/n{city},{country}")

city_country('DC', ' US')
city_country('Quebec', ' Canada')
city_country('London', ' United Kingdom')