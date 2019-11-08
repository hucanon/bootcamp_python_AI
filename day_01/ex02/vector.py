# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcanon <hugo@frogames.com>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/07 17:01:19 by hcanon            #+#    #+#              #
#    Updated: 2019/11/08 17:33:55 by hcanon           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    def __init__(self, arg):
        self.values = []
        if type(arg) == int:
            for i in range(arg):
                self.values.append(float(i))
        elif type(arg) == tuple:
            r = []
            i = arg[0]
            while i < arg[1]:
                r.append(i)
                i += 1
            for i in r:
                self.values.append(float(i))
        elif type(arg) == list:
            for i in arg:
                self.values.append(float(i))

    def __add__(self, others):
        new_values = []
        i = 0
        case = 0
        try:
            v1_len = len(self.values)
            v2_len = len(others.values)
        except AttributeError:
            print("All of the objects must be of type 'Vector' for additions")
            return 0
        if v1_len >= v2_len:
            case = 1
        if case == 1:
            while i < v2_len:
                new_values.append(self.values[i] + others.values[i])
                i += 1
            while i < v1_len:
                new_values.append(self.values[i])
                i += 1
        else:
            while i < v1_len:
                new_values.append(self.values[i] + others.values[i])
                i += 1
            while i < v2_len:
                new_values.append(others.values[i])
                i += 1
        return Vector(new_values)

    def __radd__(self, others):
        return self.__add__(others)

    def __sub__(self, others):
        return self.__add__(others.__mul__(-1))

    def __rsub__(self, others):
        return self.__sub__(others)

    def __mul__(self, others):
        new_values = []
        i = 0
        case = 0
        if type(others) == int:
            for i in self.values:
                new_values.append(i * others)
        else:
            try:
                v1_len = len(self.values)
                v2_len = len(others.values)
            except AttributeError:
                print("All of the objects must be of type 'Vector' or 'int' for multiplications")
                return 0
            if v1_len >= v2_len:
                case = 1
            if case == 1:
                while i < v2_len:
                    new_values.append(self.values[i] * others.values[i])
                    i += 1
                while i < v1_len:
                    new_values.append(0)
                    i += 1
            else:
                while i < v1_len:
                    new_values.append(self.values[i] * others.values[i])
                    i += 1
                while i < v2_len:
                    new_values.append(0)
                    i += 1
        return Vector(new_values)

    def __rmul__(self, others):
        return self.__mul__(others)

    def __truediv__(self, others):
        try:
            new_values = []
            i = 0
            case = 0
            if type(others) == int:
                for i in self.values:
                    new_values.append(i / others)
            else:
                try:
                    v1_len = len(self.values)
                    v2_len = len(others.values)
                except AttributeError:
                    print("All of the objects must be of type 'Vector' or 'int' for divisions")
                    return 0
                if v1_len >= v2_len:
                    case = 1
                if case == 1:
                    while i < v2_len:
                        new_values.append(self.values[i] / others.values[i])
                        i += 1
                    while i < v1_len:
                        new_values.append(0)
                        i += 1
                else:
                    while i < v1_len:
                        new_values.append(self.values[i] / others.values[i])
                        i += 1
                    while i < v2_len:
                        new_values.append(0)
                        i += 1
            return Vector(new_values)
        except ZeroDivisionError:
            print("You cannot divide any values by 0")
            return 0

    def __rtruediv__(self, others):
        try:
            new_values = []
            i = 0
            case = 0
            if type(others) == int:
                for i in self.values:
                    new_values.append(others / i)
            else:
                try:
                    v1_len = len(self.values)
                    v2_len = len(others.values)
                except AttributeError:
                    print("All of the objects must be of type 'Vector' or 'int' for divisions")
                    return 0
                if v1_len >= v2_len:
                    case = 1
                if case == 1:
                    while i < v2_len:
                        new_values.append(others.values[i] / self.values[i])
                        i += 1
                    while i < v1_len:
                        new_values.append(0)
                        i += 1
                else:
                    while i < v1_len:
                        new_values.append(others.values[i] / self.values[i])
                        i += 1
                    while i < v2_len:
                        new_values.append(0)
                        i += 1
            return Vector(new_values)
        except ZeroDivisionError:
            print("You cannot divide any values by 0")
            return 0

    def __str__(self):
        ret = "(Vector [" 
        flag = 0
        for i in self.values:
            if flag == 0:
                ret += str(i)
                flag = 1
            else:
                ret += ", " + str(i)
        ret += "])"
        return ret

    def __repr__(self):
        return self.values
