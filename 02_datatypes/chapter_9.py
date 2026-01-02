essential_spices = {"ginger", "cardamom", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# all_spices = essential_spices.union(optional_spices)

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# common_spices = essential_spices.intersection(optional_spices)
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

print(f"Is ginger in essential spices?: {'ginger' in essential_spices}")

frozen_set = frozenset(["ginger", "cardamom", "cinnamon"])
print(f"Frozen set: {frozen_set}")