my_string= "hello"
my_list=list(my_string)
print(my_list)

new_list = ["Red", "Blue", "White", "Green"]
z = sorted(new_list)
d = list(z)
d[0], d[1],d[2],d[3] = d[3], d[2], d[1], d[0]