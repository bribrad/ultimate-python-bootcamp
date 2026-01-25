chai_type = "Ginger chai"
customer_name = "Bri"

print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and bold"
print(f"first char: {chai_description[0]}")
print(f"first word: {chai_description[0:8]}")
print(f"first word: {chai_description[:8]}")
print(f"first word: {chai_description[0:8:2]}")
print(f"last word: {chai_description[9:]}")
print(f"reversed: {chai_description[::-1]}")

lable_text = "chai spéciale"
encoded_label = lable_text.encode("utf-8")
print(f"Encoded label: {encoded_label}")
print(f"Non-encoded label: {lable_text}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")