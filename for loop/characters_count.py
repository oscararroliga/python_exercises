string = input("Enter the words to count: ")

count = 0

for i in string:
    count = count + 1
print("La cantidad de carácteres en tu contenido es " + str(count))

if count > 200:
    print("Content too big")
else:
    print("You are ok")    