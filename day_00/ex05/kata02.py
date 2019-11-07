t = (3,30,2019,9,25)

def true_value(nb):
    new_str = str(nb // 10) + str(nb % 10)
    return (new_str)

final_str = true_value(t[3]) + "/" + true_value(t[4]) + "/" + str(t[2])
final_str += " " + true_value(t[0]) + ":" + true_value(t[1])
print(final_str)
