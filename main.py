from pprint import pprint

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

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    recipe_dish = {}
    cook_book = open_recipes_file()
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients:
                total_quantity = int(ingredient['quantity']) * person_count
                recipe_dish[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                              'quantity': total_quantity}
    pprint(recipe_dish, sort_dicts=False)
    return recipe_dish


# pprint(open_recipes_file(), sort_dicts=False)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3)
