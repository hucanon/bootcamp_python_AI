# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 12:09:10 by hcanon            #+#    #+#              #
#    Updated: 2019/11/07 15:45:02 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from datetime import datetime
import sys

class Book:
    def __init__(self, name, last_update = 0, creation_date = 0, recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}):
        """initialize the book which contains recipes"""
        if name == "":
            print("The book must have a name.")
        else:
            self.name = name
            self.recipes_list = recipes_list
            last_update = datetime.now()
            creation_date = datetime.now()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        recipe = ""
        for curr in self.recipes_list:
            for i in self.recipes_list[curr]:
                if i.name == name:
                    recipe = i
        if recipe == "":
            print("This recipe doesn't seem to be in your book...")
        else:
            print(str(recipe))
            return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
            print("Recipe type unknown...")
        else:
            for i in self.recipes_list[recipe_type]:
                print(str(i))

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) == int or type(recipe) == str or type(recipe) == dict or type(recipe) == list:
            print("This is not a recipe.")
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            last_update = datetime.now()
