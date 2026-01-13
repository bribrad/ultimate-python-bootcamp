def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Green Tea"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai_gen = get_chai_gen()

# for cup in chai_gen:
#     print(cup)

print(next(chai_gen))
print(next(chai_gen))
print(next(chai_gen))