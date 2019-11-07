# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 19:57:40 by hcanon            #+#    #+#              #
#    Updated: 2019/11/04 20:30:17 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re
import string

if len(sys.argv) != 3:
    print("ERROR")
else:
    try:
        int(sys.argv[1])
        print("ERROR")
        sys.exit(0)
    except ValueError:
        long_words = []
        current = ""
        all_words = sys.argv[1].replace(';',' ').replace(',',' ').split()
        try:
            n = int(sys.argv[2])
        except ValueError:
            print("ERROR")
            sys.exit(0)

        for current in all_words:
            if len(current) >= int(n):
                long_words.append(current)
        print(long_words)
