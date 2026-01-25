def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, no more chai")

stall = chai_stall()
print(next(stall))
stall.close()
# print(stall.send("Masala Chai"))


def token_dispenser(start: int = 1):
    try:
        while True:
            yield start
            start += 1
            # start = yield
    except:
        print("Dispenser closed.")
        
token = token_dispenser()
for _ in range(5):
    print(next(token))