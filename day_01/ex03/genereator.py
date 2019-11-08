# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    genereator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 17:37:04 by hcanon            #+#    #+#              #
#    Updated: 2019/11/08 18:10:37 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def generator(text, sep = " ", option = None):
    words = []
    while text[i]:
        while text[i] == sep:
            i += 1
        if not text[i]:
            return words
        curr_word = ""
        while text[i] != sep:
            curr_word += text[i]
            i += 1
        if option == "unique":
            for i in words:
                if i == curr_word:
                    curr_word = ""
        if curr_word != "":
            words.append(curr_word)
    return words
