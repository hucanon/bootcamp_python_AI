# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 15:47:45 by hcanon            #+#    #+#              #
#    Updated: 2019/11/07 16:13:20 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = is_alive

class Lannister(GotCharacter):
    """The Lions of the seven kingdoms"""
    def __init__(self, first_name = None, is_alive = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar"

    def die(self):
        self.is_alive = False

    def print_house_words(self):
        print(self.house_words)
