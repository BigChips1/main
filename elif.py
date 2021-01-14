x = object()
y = object()

# TODO: (multlipes the x and y object 10 times and add them both together in big_list)
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# checks if x and y list are equal to 10 by counting and also checks if the
# count of objects from x and y is equal to 10 each (together 20)
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
