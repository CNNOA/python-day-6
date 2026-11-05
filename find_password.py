line_number = 0

with open("logs.txt", "r") as file:
    for each_line in file:
        line_number = line_number + 1
        if "password" in each_line:
            print(each_line)
            print("The line number is:", line_number)

#Challenge #2
#Creat file called line_counter.py
#Copy and paste song lyrics into a lyrics.txt file
#Write a program that outputs the TOTAL number of lines

