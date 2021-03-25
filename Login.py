"""
So this is a very simple login.
For now, we won't worry about security
But keep in mind that companies don't do this
"""

#So first, we import the module
#'csv'
import csv

#This is how to open a file in read mode, 'r'
#You would use 'w' to open it in write mode
fh = open("Users.csv",'r')

#Then we read the file
reader = csv.reader(fh)

#We define some list variables
Username = []
Password = []
Type = []

#Now we separate and add the values to
#Each of the lists
for line in reader:
    Username.append(line[0])
    Password.append(line[1])
    Type.append(line[2])

#Now we can ask for the username and password
username = input("Enter username: ")
password = input("Enter password: ")

#We define a boolean value
#And a for loop
#This allows us to search through entire list
#And if one of them matches, the "flag will be raised"

flag = False
for i in range(len(Username)):
    if Username[i] == username:
        if password[i] == password[i]:
            flag = True


#Now we check if the flag was raised
if flag == True:
    #If so, we print the welcome message
    print("Welcome User")

else:
    #Otherwise, we say the reject message
    print("Incorrect Login")