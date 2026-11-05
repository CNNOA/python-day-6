users_name = input("What is your name? ")

with open("logs.txt", "a") as file:
    file.write(users_name + "\n")