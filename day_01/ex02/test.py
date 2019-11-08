# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 17:18:05 by hcanon            #+#    #+#              #
#    Updated: 2019/11/08 17:01:39 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

v1 = Vector([1.0, 2.0, 3.0])
v2 = Vector((10, 15))
v3 = Vector(3)
print(v1)
print(v2)
print(v3)

print("\nadd :")
print(v1 + v3)
print(v2 + v3)
print(v1 + v2 + v3)

print("\nsub :")
print(v1 - v3)
print(v2 - v3)
print(v1 - (v2 + v3))

print("\nmul :")
print(v1 * v3)
print(v2 * v3)
print(v1 * v2 * v3)
print(v1 * 5)
print(5 * v3)

print("\ntruediv :\n")
print(v1 / v3)
print(v2 / v3)
print(v1 / v2)
print(v3 / 5)
print(5 / v1)
