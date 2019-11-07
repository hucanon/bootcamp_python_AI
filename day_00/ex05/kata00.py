
flag = 1
length = len(t)
i = 0

if length > 1:
    final_str = "The %i numbers are: " % (length)
if length == 1:
    final_str = "The number is: "
if length < 1:
    final_str = "There is no number."
while i < length:
    if flag == 0:
        final_str += ", "
    else:
        flag = 0
    final_str += str(t[i])
    i += 1
print(final_str)
