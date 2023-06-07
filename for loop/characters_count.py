##Catch the text to count
string = input("Enter the words to count: ")

count = 0

##Iterate with the for loop
for i in string:
    count = count + 1
print("The numbers of characters in your text is: " + str(count))

##Warning mode, in case we need to notice an exceed of characters. 

if count > 200:
    print("Content too big")
else:
    print("You are ok")    