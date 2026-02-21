# def greet():
#     name = input("What's your name? ").capitalize()
#     location = input("Where do you live? ").capitalize()
#     time = input("What time is it? ").lower()
#
#     print(f"Good {time}, {name} from {location}!")
#
#
# greet()


def greet_with_parameter(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")


greet_with_parameter(input("What's your name? "), input("What's your location? "))

# positional argument
greet_with_parameter("Caverney", "Pemalang")

# keyword argument
greet_with_parameter(location="Pemalang", name="Caverney")
