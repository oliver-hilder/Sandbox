LENGTH_LIMIT = 5

password = str(input("Enter Password: "))
while len(password) < LENGTH_LIMIT:
    print("Length too small. Try again.")
    password = str(input("Enter Password: "))
for character in password:
    print("*", end='')
