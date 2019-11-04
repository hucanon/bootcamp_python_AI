# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 18:09:47 by hcanon            #+#    #+#              #
#    Updated: 2019/11/04 19:55:47 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

sandwich = {"name" : "sandwich", "ingredients" : ["ham", "bread", "cheese", "tomatoes"], "meal" : "lunch", "prep_time" : 10}
cake = {"name" : "cake", "ingredients" : ["flour", "sugar", "bread"], "meal" : "dessert", "prep_time" : 60}
salad = {"name" : "salad", "ingredients" : ["spinach", "arugula", "avocado", "tomatoes"], "meal" : "lunch", "prep_time" : 15}
cookbook = {0 : sandwich, 1 : cake, 2 : salad}
key = 0
i = 0
ingredients = []

def find_index(name):
    """find the index of a recipe in the cookbook"""
    for key in cookbook:
        if cookbook[key]["name"] == name:
            return key
    return -1

def print_recipe(name):
    """print the recipe from a chosen meal in the cookbook"""
    index = find_index(name)
    print("\nRecipe for " + name + " :")
    print("Ingredients list: " + str(cookbook[index]["ingredients"]))
    print("To be eaten for " + cookbook[index]["meal"])
    print("Takes " + str(cookbook[index]["prep_time"]) + " minutes of cooking")

def add_recipe(name, ingredients, meal, prep_time):
    """add a recipe in the cookbook"""
    dict_len = len(cookbook)
    new_dict = {}
    new_dict["name"] = name
    new_dict["ingredients"] = ingredients
    new_dict["meal"] = meal
    new_dict["prep_time"] = prep_time
    cookbook[dict_len] = new_dict
    print("The recipe of " + name + " has been successfully added to the cookbook.")

def del_recipe(name):
    """delete a chosen recipe from the cookbook"""
    index = find_index(name)
    del cookbook[index]
    print("The recipe of " + name + " has been successfully deleted.")

def print_cookbook():
    """print the entire cookbook !"""
    for key in cookbook:
        print_recipe(cookbook[key]["name"])

while key != 5:
    key = int(input("\nPlease select an option by typing the corresponding number\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n"))
    if key == 1:
        print("Adding a new recipe to the cookbook, great !")
        name = input("Name of the recipe : ")
        while (str(key) != "end"):
            key = input("ingredients needed for the recipe (type \"end\" when you are finished with the ingredients): ")
            if key != "end":
                ingredients.append(key)
        meal = input("when shall we eat the meal ? ")
        prep_time = input("Average time required to prepare the meal : ")
        add_recipe(name, ingredients, meal, prep_time)
    elif key == 2:
        name = input("Which recipe do you want to delete from the book ? ")
        del_recipe(name)
    elif key == 3:
        name = input("Which recipe do you want to do today ? ")
        print_recipe(name)
    elif key == 4:
        print("Here are all the recipes you possess :")
        print_cookbook()
    elif key == 5:
        print("Cookbook closed.")
    else:
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
