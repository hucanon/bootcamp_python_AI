# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 11:30:50 by hcanon            #+#    #+#              #
#    Updated: 2019/11/07 11:53:00 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

ran = random.randint(1, 99)
key = ""
attempt = 0

while key != "exit":
    key = input("What's your guess between 1 and 99 ?\n")
    try:
        key = int(key)
        attempt += 1
        if key > ran:
            print("Too high !")
        if key < ran:
            print("Too low !")
        if key == ran:
            if attempt == 1:
                print("Correct ! Wow you found it from the very first try !")
            else:
                print("Congrats, you've got it !\nYou found it in %i attempts !" % attempt)
            if ran == 42:
                print("PS : Did you know that the Pink Floyd performed on stage with Adams for his 42th birthday ?")
            key = "exit"
    except ValueError:
        if key == "exit":
          print("Goodbye !")
        else:
          print("That's not a number.")
