# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 17:01:19 by hcanon            #+#    #+#              #
#    Updated: 2019/11/07 18:29:27 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    def __init__(self, arg):
        self.values = []
        if type(arg) == int:
            for i in range(arg):
                self.values.append(float(i))
        elif type(arg) == tuple:
            for i in arg:
                self.values.append(float(i))
        elif type(arg) == list:
            for i in arg:
                self.values.append(float(i))
    def __add__(self, v2):
        pass
