# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 12:09:19 by hcanon            #+#    #+#              #
#    Updated: 2019/11/07 12:48:48 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# from book import Book
from recipe import Recipe

indian_rice = Recipe("Indian rice", 2, 45, ["rice", "curry", "cumin", "paprika"], "rice with some Indian spices.", "lunch")
to_print = str(indian_rice)
print(to_print)
