# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 17:16:28 by hcanon            #+#    #+#              #
#    Updated: 2019/11/04 17:20:46 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

phrase = "the right format"
strlen = len(phrase)
final_str = ""

for i in range(41 - strlen):
    final_str += "-"
final_str += phrase
print(final_str)
