# Title: TODO task manager
# Dev: Yuliya Kalcheuskaya
# Date: Feb, 15, 2022

# Declare my variables
listTodo = []               # In-memory list of unsaved items
strMenuChoice = ''          # Menu user input
strFileName = 'ToDo.txt'    # Data storage file name
objFile = None              # File object

# Start a loop until user decided to exit the program
while True:
    # Display a menu of choices to the user
    print("""
    Menu of Options:
    1) Add new TODO item to the in-memory list
    2) Remove the last TODO item from the in-memory list
    3) Display unsaved in-memory list
    4) Save in-memory list to the file
    5) Display the content of the TODO file
    6) Exit program
        """)

    # Read user input for the menu choice
    strMenuChoice = input("What function would you like to perform? [1-6]: ")

    # Function 1: Add new item to the in-memory list
    if strMenuChoice.strip() == "1":
        # Read the new item
        strTask = input("What is the task? ").strip()
        strPriority = input("What is the priority? [High|Medium|Low] ").strip()

        # Create a new dictionary object representing a separate row in the target list
        dicTodoEntry = {"Task": strTask, "Priority": strPriority}

        # Add the row to the list
        listTodo.append(dicTodoEntry)

    # Function 2: Remove the last item from the in-memory list
    elif strMenuChoice.strip() == "2":
        # Check if the list is empty or not
        if len(listTodo) == 0:
            print("The list is empty, so there is nothing to remove!")
        else:
            removedItem = listTodo.pop()
            print("Removed item: " + removedItem["Task"] + " (" + removedItem["Priority"] + ")")

    # Function 3: Display unsaved in-memory list
    elif strMenuChoice.strip() == "3":
        # Check if the list is empty or not
        if len(listTodo) == 0:
            print("The list is empty, so there is nothing to display!")
        else:
            print("The current items in the in-memory TODO list:")
            print("*********************")

            # Printing all the rows in the in-memory list
            for todoRow in listTodo:
                print(todoRow["Task"] + " (" + todoRow["Priority"] + ")")
            print("*********************")

    # Function 4: Save in-memory list to the file
    elif strMenuChoice.strip() == "4":
        # Check if the list is empty or not
        if len(listTodo) == 0:
            print("The list is empty, so there is nothing to save!")
        else:
            # Opening/creating the file
            objFile = open(strFileName, "a")

            # Iterating through the rows in the list
            for todoRow in listTodo:
                # Write the row values to the file
                objFile.write(todoRow["Task"] + "|" + todoRow["Priority"] + "\n")

            # Close the file
            objFile.close()

            # Delete all the in-memory items from the list
            listTodo.clear()

            # Notifying user that the data is saved successfully
            print("The data has been saved successfully!")

    # Function 5: Display the content of the file
    elif strMenuChoice.strip() == "5":
        # Adding exception handling for scenario when the file does not exist
        try:
            # Opening the file in read mode
            objFile = open(strFileName, "r")
        except FileNotFoundError:
            print(strFileName + " does not exist!")
        else:
            print("The current TODO items in the file:")
            print("*********************")

            # Read the file content line by line and display it to the user
            for line in objFile:
                rowData = line.strip().split("|")

                # Verifying that the format is valid
                if len(rowData) == 2:
                    print(rowData[0] + " (" + rowData[1] + ")")
                else:
                    print("Unexpected value detected!")
            print("*********************")

            # Close the file
            objFile.close()

    # Function 6: Exit program
    elif strMenuChoice.strip() == "6":
        print("Exiting program!")
        exit()

    # Processing unexpected user input
    else:
        print("Unexpected input!")