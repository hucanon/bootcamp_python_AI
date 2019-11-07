# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 17:21:04 by hcanon            #+#    #+#              #
#    Updated: 2019/11/04 18:03:46 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
t = ( 0, 4, 132.42222, 10000, 12345.67)

def true_value(nb):
    new_str = str((nb // 10) % 10) + str(nb % 10)
    return (new_str)

def digits_count(n):
    if n > 0:
       digits = int(math.log10(n))+1
    elif n == 0:
       digits = 1
    else:
        digits = int(math.log10(-n))+2
    return (digits)

final_str = "day_" + true_value(t[0]) + ", ex_" + true_value(t[1]) + " : "
final_str += format(t[2], ".2f") + ", "
final_str += format(t[3], ".2e") + ", "
final_str += format(t[4], ".2e")

print(final_str)
