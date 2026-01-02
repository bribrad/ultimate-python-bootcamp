masala_spices = ("cardamom", "cloves", "cinnamon")

# unpacking a tuple
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ginger ratio: {ginger_ratio}, Cardamom ratio: {cardamom_ratio}")

# variable swapping. no need of a temp variable
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ginger ratio: {ginger_ratio}, Cardamom ratio: {cardamom_ratio}")

# membership

print(f"Is ginger in masala spices?: {'ginger' in masala_spices} ")