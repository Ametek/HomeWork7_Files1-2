def open_recipes_file():
    cook_book = {}
    with open('./files/recipes.txt', 'r', encoding='utf-8') as file:
        while True:
            dish = []
            dish_name = file.readline().rstrip('\n')
            quantity_ingredients = int(file.readline().rstrip('\n'))
            for ingredient in range(quantity_ingredients):
                attributes = file.readline().split(' | ')
                dish.append({'ingredient_name' : attributes[0],
                             'quantity' : attributes[1],
                             'measure' : attributes[2].rstrip('\n')})
            cook_book[dish_name] = dish
            null_string = file.readline()
            if null_string == "":
                break
    return (cook_book)

from pprint import pprint
pprint(open_recipes_file(), sort_dicts=False)
