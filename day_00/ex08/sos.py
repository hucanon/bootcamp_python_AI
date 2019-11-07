# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 20:34:21 by hcanon            #+#    #+#              #
#    Updated: 2019/11/07 11:30:32 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 
                    'D':'-..', 'E':'.', 'F':'..-.', 
                    'G':'--.', 'H':'....', 'I':'..', 
                    'J':'.---', 'K':'-.-', 'L':'.-..', 
                    'M':'--', 'N':'-.', 'O':'---', 
                    'P':'.--.', 'Q':'--.-', 'R':'.-.', 
                    'S':'...', 'T':'-', 'U':'..-', 
                    'V':'...-', 'W':'.--', 'X':'-..-', 
                    'Y':'-.--', 'Z':'--..', '1':'.----', 
                    '2':'..---', '3':'...--', '4':'....-', 
                    '5':'.....', '6':'-....', '7':'--...', 
                    '8':'---..', '9':'----.', '0':'-----'}
final_str = ""
argc = len(sys.argv)
if argc > 2:
    print("ERROR")
    sys.exit(0)
if argc == 2:
    for i in sys.argv[1]:
        try :
            final_str += morse[i]
        except KeyError:
            print("ERROR")
            sys.exit(0)
    print(final_str)