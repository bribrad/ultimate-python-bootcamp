favorite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Green Tea",
    "Elaichi Chai",
    "Lemon Tea",
]

unique_chai = {chai for chai in favorite_chais}
print(unique_chai)

unique_chai = {chai for chai in favorite_chais if len(chai) > 9}
print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)