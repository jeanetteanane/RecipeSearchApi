import requests

def recipe_search(ingredient,meal_of_the_day,cuisine):
    app_id = ''
    app_key = ''
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}&mealType={}&cuisineType={}'.format(ingredient,app_id,app_key,meal_of_the_day,cuisine))
    data = result.json()
    return data['hits']

type_of_meal = ["breakfast", "brunch", "lunch/dinner", "snack"]

cuisine_type = ["american", "asian", "british", "chinese","french", "italian", "japanese"]

def run():
    meal_of_the_day = input('Which meal type do you want? \n {}:'.format(type_of_meal))
    while meal_of_the_day not in type_of_meal:
        meal_of_the_day = input("Unknown meal of day. Please choose from one of listed meal types: \n {}".format(type_of_meal))

    cuisine = input('Which cuisine are you seeking after? \n {}:'.format(cuisine_type))
    while cuisine not in cuisine_type:
        cuisine = input("Unknown cuisine. Please choose from one of the listed cuisines: \n {}".format(cuisine_type))

    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient,meal_of_the_day,cuisine)
    while ingredient == "":
        print("Unknown ingredient. Please add an ingredient again: ")

    meal_search = print('You would like to have a {} {} meal with {} included in the recipe.'.format(cuisine,meal_of_the_day,ingredient))

    print("-" * 150)

    with open("recipebook.txt", "w") as recipe_file:
        for result in results:
            recipe = result['recipe']
            print(round(int(recipe['calories'])))
            print(recipe['label'])
            print(recipe['cuisineType'])
            print(recipe['mealType'])
            print(recipe['url'])
            print("-" * 100)

            lines = ['You can make this recipe: ', recipe['label'], str(recipe['cuisineType']), str(recipe['mealType']), 'Calories:',str(round(int(recipe['calories']))),recipe['url'], 'Ingredients: ',','.join(recipe['ingredientLines']), "-------------------------------------------------------------------------------------------------------------" + '\n']
            recipe_file.write('\n'.join(lines))
run()

# codecs

