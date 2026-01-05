# chai = "Ginger chai"

# def prepare_chai(order):
#     print(f"Preparing {order}")
    

# prepare_chai(chai)

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low")
make_chai(tea="Green", milk="No", sugar="Medium")

def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_chai("Cinnamon", "Cardamom", sweetener="Honey", foam="Yes")

# default traps
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# chai_order()
# chai_order()


def chai_order(order=None):
    if order is None:
        order = []
    order.append("Masala")
    print(order)

chai_order()
chai_order()
