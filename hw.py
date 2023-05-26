
with open('recipes.txt') as f:
    cook_book = {}
    for i in f:
        cook_name = i.strip()
        ingredient_count = int(f.readline())
        ingredient = []
        for cook in range(ingredient_count):
            cook = f.readline()
            ingredient_name, quantity, measure = cook.strip().split(' | ')
            ingredient.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        f.readline()
        cook_book[cook_name] = ingredient
        
print(f'cook_book = {cook_book}')

