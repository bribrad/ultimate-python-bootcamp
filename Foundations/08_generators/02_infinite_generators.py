def inifinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = inifinite_chai()

user_2 = inifinite_chai()

for _ in range(30):
    print(next(refill))

for _ in range(3):
    print(next(user_2))