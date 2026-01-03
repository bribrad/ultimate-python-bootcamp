inventory = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavor in inventory:
    print(flavor)
    if flavor == "Out of Stock":
        continue
    elif flavor == "Discontinued":
        break 
   