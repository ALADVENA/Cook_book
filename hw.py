# Задание № 1

with open('recipes.txt') as f:
    cook_book = {}
    for i in f:
        cook_name = i.strip()
        ingredient_count = int(f.readline())
        ingredients = []
        for cook in range(ingredient_count):
            cook = f.readline()
            ingredient_name, quantity, measure = cook.strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        f.readline()
        cook_book[cook_name] = ingredients
        
print(f'cook_book = {cook_book}')

# Задание № 2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list= dict()
    for dish in dishes: 
        if dish in cook_book:
            for ingredients in cook_book[dish]: 
                add_list = dict()
                if ingredients['ingredient_name'] not in shop_list:
                    add_list['measure'] = ingredients['measure']
                    add_list['quantity'] = ingredients['quantity'] * person_count
                    shop_list[ingredients['ingredient_name']] = add_list
                else:
                    shop_list[ingredients['ingredient_name']]['quantity'] = shop_list[ingredients['ingredient_name']]['quantity'] + \
                                                                     ingredients['quantity'] * person_count

        else:
            print(f'\n"В меню нет - идите голодными."\n')
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))