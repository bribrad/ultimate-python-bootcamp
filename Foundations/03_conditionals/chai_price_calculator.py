cup_size = input("Enter your cup size (small, medium, large): ").lower()

price = 0
if cup_size == "small":
    price = 10
elif cup_size == "medium":
    price = 15
elif cup_size == "large":
    price = 20
else:
    print("Unknown cup size.")
    exit()

print(f"Price is ${price}.")