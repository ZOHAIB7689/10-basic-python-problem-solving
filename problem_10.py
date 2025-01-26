# Recommend a type of pet food based on the species of the pet (e.g. cat - fish, dog - chicken, rabbit - carrot)
def recommend_pet_food(species):
    recommendations = {
        'cat': 'fish',
        'dog': 'chicken',
        'rabbit': 'carrot'
    }
    return recommendations.get(species, 'unknown')

# Example usage
species = input("Is your pet a cat, dog, or rabbit? ").lower()
print(f"The recommended food for a {species} is {recommend_pet_food(species)}.")