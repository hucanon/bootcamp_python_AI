# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 11:54:58 by hcanon            #+#    #+#              #
#    Updated: 2019/11/07 15:31:58 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Recipe:
    TYPE = "Recipe"
    def __init__(self, name, cooking_time, cooking_lvl, ingredients, description, recipe_type):
        try :
            cooking_lvl = int(cooking_lvl)
            cooking_time = int(cooking_time)
            if name == "" or cooking_lvl > 5 or cooking_lvl < 1 or (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert") or cooking_time < 0 or len(ingredients) == 0 or isinstance(ingredients, list) == False:
                print("Error during the processing of the given arguments.")
                sys.exit(0)
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.recipe_type = recipe_type
            self.name = name
            self.description = description
        except ValueError:
            print("Error during the processing of the given arguments.")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += self.name + " :\nCooking level is : %i\nApproximatively %i minutes of preparation.\nIngredients required for %s are : " % (self.cooking_lvl, self.cooking_time, self.name) + str(self.ingredients) + "\nThis meal is a %s and this is its description : %s" % (self.recipe_type, self.description)
        return txt
