# pure function. no interaction with global scope
def pure_chai(cups):
    return cups * 10

total_chai = 0

# impure function. interacts with global scope
# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups
    return total_chai


def pour_chai(n):
    if n == 0:
        return "All cups poured!"
    print(f"Pouring chai {n}")
    return pour_chai(n-1)

pour_chai(5)

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))

print(strong_chai)