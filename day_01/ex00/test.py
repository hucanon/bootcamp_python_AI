# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 12:09:19 by hcanon            #+#    #+#              #
#    Updated: 2019/11/07 15:45:23 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

indian_rice = Recipe("Indian rice", 45, 2, ["rice", "curry", "cumin", "paprika"], "rice with some Indian spices.", "lunch")
to_print = str(indian_rice)
print(to_print)
book = Book("The Cookbook")
book.add_recipe(indian_rice)
book.get_recipe_by_name(indian_rice.name)
book.get_recipes_by_types("lunch")
