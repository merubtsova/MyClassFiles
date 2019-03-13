# -------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   merubtsova
# Date:  3/12/2019
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   merubtsova, 3/12/2019, Added code to complete assignment 5
# https://www.tutorialspoint.com/python/python_dictionary.htm
# -------------------------------------------------#

# -- Data --#
# declare variables and constants
# objFile = An object that represents a file
objFile = ""
# lstData = A list of text data from the file
lstData = ""
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
dicRow = {}
# lstTable = A dictionary that acts as a 'table' of rows
lstTable = []
# strMenu = A menu of user options
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """
# strChoice = Capture the user option selection
strChoice = ""

# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# -- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
# Open file
objFile = open("Todo.txt", "r")
for item in objFile.readlines():
    lstData = item.strip("\n").split(",")
    dicRow = {"Task":lstData[0], "Priority":lstData[1]}
    lstTable.append(dicRow)
objFile.close()
# Step 2
# Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    # Step 3 -Show the current items in the table
    if (strChoice == '1'):
        for item in lstTable:
           print(item['Task'] + "," + item['Priority'])
    # Step 4 - Add a new item to the list/Table
    elif (strChoice == '2'):
        # Ask to enter the input: the new row of data
        dicRow = {"Task": str(input("Enter Task: ")), "Priority": str(input("Enter Priority [low or high]: "))}
        # Append a new row
        lstTable.append(dicRow)
    # Step 5 - Remove existing item from the list/Table
    elif (strChoice == '3'):
        strKey = str(input("Enter a particular task you would like to delete: "))
        flag = False
        for dicRow in lstTable:
            if dicRow['Task'] == strKey:
                lstTable.pop(lstTable.index(dicRow))
                flag = True
        if not flag:
            print("Such task doesn't exist. Please try again.")
    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        objFile = open("Todo.txt", "w")
        # Use for loop to extract data and store to the file
        for item in lstTable:
            objFile.write(item['Task'] + "," + item['Priority'] + "\n")
        # Close file
        objFile.close()
    elif (strChoice == '5'):
        break  # and Exit the program