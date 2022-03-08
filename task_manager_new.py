#  Capstone Project IV (Task Manager)
'''Program that managers all the user and task details
   depending on user privilege. The user is able to perform the following operations
   Register users
   Add tasks
   View all or just there tasks
   Generate and then display Task and user Information
    '''


# import modules
import datetime
import os.path


# Functions used in register
def check_file_line(user_name):
    # assigning base variable
    duplicate_user = False

    # opens the users files to read though
    users_file = open("user.txt", "r")
    users = users_file.readlines()

    # through each iteration checks if username is in the text file
    for line in users:
        users_file.seek(0)
        line_list = line.split(",")
        list_line_username = line_list[0]

        # compares each username and returns "True" if is a duplicate
        if user_name.lower() == list_line_username.lower():
            duplicate_user = True

    #closes file
    users_file.close()

    return duplicate_user


# Functions used in register
def enter_name():
    # user is notified that the username already exists and is prompted to enter another name
    print(" ")
    print("User already exists ")
    new_username = str(input("Please enter a new user name: "))

    return new_username


# Main set of functions

# Function - used to varify the user log in credentials
def log_in():
    # Opening the user text in read mode to check all the user and passwords
    users_file = open("user.txt", "r")

    # assigning base values
    user_name = " "

    # assigning base boolean value to compare
    login_credential = False

    # displaying the context and instruction to the user
    print("________________________________________________________")
    print(" Task manager Program")
    print("________________________________________________________")
    print(" ")
    print("Please Enter Username and Password , to log in: ")

    # while loop . allowing all the lines in the text file be checked for user and password
    while login_credential == False:

        # requesting user input for user and password, to check against the user .txt file
        user_name = (input("Enter your Username: "))
        password = (input("Enter your Password: "))

        # loop that runs through all the line of the txt file,
        for line in users_file:
            # splits the sting from a line in a file into two variables
            valid_user, valid_password = line.split(", ")

            # striping the variables from any hidden white spaces from the file
            valid_user_strip = valid_user.strip()
            valid_password_strip = valid_password.strip()

            # comparing the user entered variables to the variables from the user file
            # to check for user and password match
            if valid_user_strip == user_name and valid_password_strip == password:
                login_credential = True

        # if the user and password did not match the loop starts again allowing use to re-enter the details
        if login_credential == False:
            print("Incorrect Username and Password , Please Try again  ")
        # sets the position back to the top of the list so that all lines can be searched again
        users_file.seek(0)

    # close file
    users_file.close()

    return user_name

# Function -  used as Main Menu to get around through all the options
def main_menu(user_select):
    while user_select != "e":

        # call menu_options
        user_select = menu_option(user_name)

        if user_select == "r":
            register_user()

        elif user_select == "a":
            add_task()

        elif user_select == "va":
            view_all_user()

        elif user_select == "vm":
            view_my_task(user_name)

        elif user_select == "gr":
            generate_reports()

        elif user_select == "ds":
            display_statistics()

        elif user_select == "e":
            quit()

# function - called to decide if user sees admin or user menu opetion
def menu_option(user_name):
    if user_name == "admin":
        user_select = admin_menu(user_name)

    else:
        user_select = user_menu(user_name)

    return user_select

# Function - displays the admin menu options
def admin_menu(user_name):
    # selection screen - allowing the user to choose an option
    print("________________________________________________________")
    print("Enter the Option from the Admin Selection menu")
    print("________________________________________________________")

    user_select = input("""
       |r | -> To Register New User
       |a | -> To Add a Task 
       |va| -> To View all the Tasks 
       |vm| -> To View my Tasks
       |gr| -> To Generate reports
       |ds| -> To Display Statistics
       |e | -> To Exit 

       """).lower()

    return user_select

# Function - displays the user menu options
def user_menu(user_name):
    # selection screen - allowing the user to choose an option
    print("________________________________________________________")
    print("Enter the Option from the Selection menu")
    print("________________________________________________________")
    user_select = input("""
    |a | -> To Add a Task 
    |va| -> To View all the Tasks 
    |vm| -> To View amy Tasks
    |e | -> To Exit 
    """).lower()

    return user_select

# Function - used to register a user
def register_user():
    # displaying what the user has chosen
    print("________________________________________________________")
    print("Register a new User:")
    print("________________________________________________________")

    # requested user to enter name
    new_username = str(input("Please enter a new user name: "))

    # set boolean base value
    duplicate_user = True

    # loop through two functions designed to ensure that it will not accept duplicated username (only new ones)
    while duplicate_user == True:

        # function that checks of name is a duplicate
        duplicate_user = check_file_line(new_username)

        # if the username already exists , Function is called to enter a new username
        if duplicate_user == True:
            new_username = enter_name()

    # open the file append new username details to the next free line of the file
    users_file = open("user.txt", "a+")

    # set boolean base value
    password_match = False

    # while loop used to allow the user to re-enter / varify the users password
    while password_match == False:

        # requesting the users'  password twice so that it can be verified
        new_user_password = str(input("Please Enter the Password: "))
        confirm_user_password = str(input("Please Re-Enter the Password: "))

        # check if both instance of password input match
        if new_user_password == confirm_user_password:
            password_match = True

            # appending the data (string) to next line of the file
            users_file.write(f"\n{new_username}, {new_user_password}")

        # looping back to enter details should passwords not match
        if password_match == False:
            print("The Passwords did not match ")

    # closing the file
    users_file.close()

# Function - used to add user tasks
def add_task():
    # open the file to append data to the next free line of the file
    task_file = open("tasks.txt", "a+")

    # displaying what the user has chosen
    print("________________________________________________________")
    print("Task Input")
    print("________________________________________________________")

    # requesting the user to enter Task related details
    assigned_to_username = str(input("Enter the user: "))
    task_title = str(input("Enter the Task Title: "))
    task_description = str(input("Enter the Description of the Task: "))
    print("Enter the Due Date as promoted: 'year' (eg.2021) then 'month' (eg.2) then 'date' (eg.10)")
    year = int(input("Please enter year: "))
    month = int(input("Please enter the month: "))
    date = int(input("Please enter date: "))
    task_due_date = datetime.date(year, month, date)

    # setting the assigned task date to the current calendar date
    task_assigned_date = datetime.date.today()
    task_completed = str(input("Please enter a Yes or No to indicate if task completed : "))

    # appending the data (string) to next line of the file
    task_file.write(f"\n{assigned_to_username}, {task_title}, {task_description}, {task_due_date},"
                    f" {task_assigned_date}, {task_completed} ")

    # close file
    task_file.close()

# Function - used to display all user tasks
def view_all_user():
    # open file to read
    task_file = open("tasks.txt", "r+")

    # Setting up base values
    user_and_task_no = 0

    print("________________________________________________________")

    #  Loop that runs through all the lines of txt file to pull out and display the information
    for line in task_file:
        # in each iteration a line in the file is read and string variables are set  to match
        assigned_to_username, task_title, task_description, task_due_date, task_assigned_date, task_completed \
            = line.split(", ")

        # Displaying per user / task number in order through each iteration
        user_and_task_no += 1

        # through each iteration , displaying the one line after next information frm text file
        print(f"User Task No{user_and_task_no}")
        print(" ")
        print(f"Assigned to :          {assigned_to_username}")
        print(f"Task Title:            {task_title} ")
        print(f"Date Assigned:         {task_assigned_date}")
        print(f"Due Date:              {task_due_date}")
        print(f"Task Completed:        {task_completed}")
        print(f"Task Description:      \n{task_description} ")
        print("________________________________________________________")

    # closing the file
    task_file.close()

# Function - that allows users (who is logged in ) to see there tasks
def view_my_task(user_name):
    # open file to read
    task_file = open("tasks.txt", "r+")
    task_content = task_file.readlines()

    # Setting up base values
    user_and_task = {}
    count = 1

    #  Loop that runs through all the lines of txt file to pull out and display the appropriate information
    for line in task_content:

        # in each iteration a line in the file is read and string variables are set to match
        assigned_to_username, task_title, task_description, task_due_date, task_assigned_date, task_completed \
            = line.split(", ")
        # removes the "\n" at the end of the line
        task_completed = task_completed.strip()

        # the information in each line is checked and filtered to only show the signed-in user
        # and only tasks that are not yes completed
        if user_name.lower() == assigned_to_username.lower() and task_completed.lower() == "no":
            user_and_task[count] = task_title
            count += 1

    # displays the list of tasks the user is able to edit
    # as well as the instructions
    print("________________________________________________________")
    print(f"{user_name.upper()}'s \nTask list")
    print("________________________________________________________")
    print("Using the numbers bellow , choose the task details \nthat you would like to edit ")
    # print(f"Example type '1' to change task '{user_and_task[1]}' details  ")
    print(f"Example type '1' to change task '____________' details  ")
    print("Or enter '-1' to get back to the mean menu")
    print(" ")
    print("Please *Note* only incomplete tasks are visible to edit:")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print(" ")

    # prints the key and values as tasks for user to choose
    [print(key, ':', value) for key, value in user_and_task.items()]
    print(" ")

    # takes in the user input , and gos to main menu if required
    key_choice = int(input(""))
    if key_choice == -1:

        # return the user to the main menu
        main_menu(user_name)
        print(" ")
    else:
        # assigned usable base value
        task_value = user_and_task[key_choice]

        # assigned base value to be used to indicate which line in text file is over-writen
        index_count = -1

        #  Loop that runs through all the lines of txt file to pull out and display the appropriate information
        for line in task_content:
            # in each iteration a line in the file is read and string variables are set  to match
            assigned_to_username, task_title, task_description, task_due_date, task_assigned_date, task_completed \
                = line.split(", ")

            # counts increase through each iteration to keep track of tex line to over-write
            index_count += 1

            # through each iteration filters through each line and separate line data
            # to only display the full details of the task  for editing
            if assigned_to_username.lower() == user_name.lower() and \
                    task_value.lower() == task_title.lower() or \
                    task_completed.lower() == "no":
                print("________________________________________________________")
                print(f"{user_name.upper()}'s ({task_title.upper()}-Task) Details ")
                print("________________________________________________________")
                print("Press '0' to edit the Task details \nor '-1' to return tp the main menue: ")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
                print(f"Date Assigned:         {task_assigned_date}")
                print(f"Due Date:              {task_due_date}")
                print(f"Task Description:      {task_description} ")
                print(f"Task Completed:        {task_completed.upper()}")

                # break the code loop to ensure that (index_count variable is usable)
                break

        # takes in users selection to edit oir return to main menu
        choice = str(input(" "))

        # assigning base variables
        task_reassignment = assigned_to_username
        due_date_change = task_due_date
        complete_status_change = task_completed

        #  allows user to go to main menu
        if choice == '-1':
            main_menu(user_name)

        # user gains access to edit select menu
        if choice == '0':

            # assigning base variables
            edit_choice = "0"

            # loop to ensure that the edit menu selection comes up until user finally exits to the main menu
            while edit_choice != '-1':

                # display title and instructions
                print("________________________________________________________")
                print("Enter the number or letter to select an option ")
                print("________________________________________________________")

                # displays the available options and accepts there choice
                edit_choice = input("""
        |1 | -> To Change User task assigned to:  
        |2 | -> To Change Due Date :
        |3 | -> To change Completed Status :
        |s | -> to Confirm new details : 
        |-1| -> To Exit to main menu :
                """)

                # displayed the current information and allows the task to be reassigned to a new user
                if edit_choice == '1':
                    task_reassignment = input(
                        f"Task currently assigned to {assigned_to_username} , Please enter the new User name: ")

                # displayed the current information and allows the user to change the due date details
                elif edit_choice == '2':
                    print(f"Current date is {task_due_date}")
                    print(
                        "Enter the New Due Date as promoted: 'year' (eg.2021) then 'month' (eg.2) then 'date' (eg.10):")
                    year = int(input("Please enter year: "))
                    month = int(input("Please enter the month: "))
                    date = int(input("Please enter date: "))
                    due_date_change = datetime.date(year, month, date)
                    due_date_change = str(due_date_change)

                # displayed the current information and allows the user to change the completed status
                elif edit_choice == '3':
                    complete_status_change = input(f"Currently set as {task_completed},  ")
                    complete_status_change = complete_status_change + "\n"

                # allows user to check and confirm the edited information before writing to file
                elif edit_choice == 's':
                    print("________________________________________________________")
                    print(
                        "Please enter 's' again to save these details and go to \n"
                        "main menu or '-1' to go to main menu: ")
                    print("________________________________________________________")
                    print(f"Assigned to :          {task_reassignment}")
                    print(f"Task Title:            {task_title} ")
                    print(f"Date Assigned:         {task_assigned_date}")
                    print(f"Due Date:              {due_date_change}")
                    print(f"Task Description:      {task_description} ")
                    print(f"Task Completed:        {complete_status_change}")
                    print("____________________________________________________")
                    save_choice = str(input(""))

                    # after to user confirms new information , the new line is writen to text file
                    if save_choice == 's':
                        replacement_line = (task_reassignment + ", " + task_title + ", " + task_description
                                            + ", " + due_date_change + ", " + task_assigned_date
                                            + ", " + complete_status_change)

                        task_content[index_count] = replacement_line
                        task_file = open("tasks.txt", "w")
                        task_file.writelines(task_content)
                        task_file.close()

                    # returns user to main menu
                    elif save_choice == '-1':
                        main_menu(user_name)

                # returns user to main menu
                elif edit_choice == '-1':
                    main_menu(user_name)

        # closing the file
        task_file.close()

# Function - when called will create two new files "task_overview.txt" and "user_overview.txt"
#            these newly created files will contain up-to-date user and task details
#            that can be viewed ising the "ds" option in admin menu
def generate_reports():
    # (part1) generate information for task_overview.txt

    # open to read through
    task_file = open("tasks.txt", "r")
    task_content = task_file.readlines()

    user_file = open("user.txt", "r")
    users = user_file.readlines()

    # assigning base value (part one)
    total_task = 0
    total_completed = 0
    total_incomplete = 0
    total_overdue = 0

    # assigning base value (part two)
    total_users = 0
    user_list = []
    user_total_task = 0
    user_total_dictionary = {}
    user_task_percentage = {}
    user_task_percentage_dictionary = {}
    #
    user_total_completed = 0
    user_completed_task_percentage = 0
    user_total_completed_dictionary = {}
    user_completed_task_percentage_dictionary = {}
    #
    user_total_uncompleted = 0
    user_uncompleted_task_percentage = 0
    user_total_uncompleted_dictionary = {}
    user_uncompleted_task_percentage_dictionary = {}
    #
    user_total_overdue = 0
    user_total_overdue_dictionary = {}
    user_overdue_task_percentage = 0
    user_overdue_task_percentage_dictionary = {}

    # iterate through all the lines in the task file to and split the information in a usable format
    for line in task_content:
        total_task += 1
        assigned_to_username, task_title, task_description, task_due_date, task_assigned_date, task_completed \
            = line.split(", ")
        task_completed = task_completed.strip()

        # adds up through each iteration to get the total completed
        if task_completed.lower() == "yes":
            total_completed += 1

        # adds up through each iteration to get the total uncompleted
        if task_completed.lower() == "no":
            total_incomplete += 1

        # breaks down the assigned date into (date) comparable variables
        if task_completed.lower() == "no":
            year, month, date = task_due_date.split("-")
            year = int(year)
            month = int(month)
            date = int(date)
            due_date = datetime.date(year, month, date)
            todays_date = datetime.date.today()

            # checks if the due date is passed todays date, and hence overdue
            is_over_due = due_date < todays_date
            if is_over_due == True:
                # add up through each iteration to give you an overdue total
                total_overdue += 1

    # calculates users incomplete percentage
    percentage_incomplete = (total_incomplete / total_task) * 100
    percentage_incomplete = round(percentage_incomplete, 2)

    # calculates  users overdue percentage
    percentage_task_overdue = (total_overdue / total_task) * 100
    percentage_task_overdue = round(percentage_task_overdue, 2)

    # writing all extrapolated user information to next line of a text file ("task_overview.txt")
    text_line = (
            str(total_task) + ", " + str(total_completed) + ", " + str(total_incomplete) + ", " + str(total_overdue)
            + ", " + str(percentage_incomplete) + ", " + str(percentage_task_overdue))
    task_overview_file = open("task_overview.txt", "w+")

    task_overview_file.write(text_line)

    # generate information for user_overview.txt

    # getting the usernames in a list
    for line in users:

        # adding through each loop to also get the total user count
        total_users += 1

        # going through each line in users.txt and getting a username list
        text_line = line.split(", ")
        user_list.append(text_line[0])

    # getting per user totals
    for name in user_list:

        # re-assigning base values for each loop
        user_total_overdue = 0
        user_total_task = 0
        user_total_completed = 0
        user_total_uncompleted = 0

        # running through each line of task.txt and splitting the data into usable variables
        for line in task_content:
            assigned_to_username, task_title, task_description, task_due_date, task_assigned_date, task_completed \
                = line.split(", ")
            task_completed = task_completed.strip()

            # getting the total tasks per user
            if name == assigned_to_username.lower():
                user_total_task += 1

            # dictionary to store each user's total
            user_total_dictionary[name] = user_total_task

            # user total completed
            if name == assigned_to_username.lower() and task_completed.lower() == "yes":
                user_total_completed += 1

            # dictionary to store each user's completed total
            user_total_completed_dictionary[name] = user_total_completed

            # user total incomplete
            if name == assigned_to_username.lower() and task_completed.lower() == "no":
                user_total_uncompleted += 1

            # dictionary to store each user's uncompleted total
            user_total_uncompleted_dictionary[name] = user_total_uncompleted

            # dictionary for user and total task percentage
            user_task_percentage = (user_total_dictionary[name] / total_task) * 100
            user_task_percentage = round(user_task_percentage, 2)
            user_task_percentage_dictionary[name] = user_task_percentage

            # getting the total for overdue
            # splitting the data into usable variables
            if name == assigned_to_username.lower() and task_completed.lower() == "no":
                year, month, date = task_due_date.split("-")
                year = int(year)
                month = int(month)
                date = int(date)

                # checking if it is overdue
                due_date = datetime.date(year, month, date)
                todays_date = datetime.date.today()
                is_over_due = due_date < todays_date

                # getting the total of overdue
                if is_over_due == True:
                    user_total_overdue += 1

            # dictionary for user and total overdue
            user_total_overdue_dictionary[name] = user_total_overdue

    # getting the Percentage dictionary
    for name in user_list:
        # dictionary for user and total completed task percentage
        user_completed_task_percentage = (user_total_completed_dictionary[name] / user_total_dictionary[name]) * 100
        user_completed_task_percentage = round(user_completed_task_percentage, 2)
        user_completed_task_percentage_dictionary[name] = user_completed_task_percentage

    for name in user_list:
        # dictionary for user and total uncompleted task percentage
        user_uncompleted_task_percentage = (user_total_uncompleted_dictionary[name] / user_total_dictionary[name]) * 100
        user_uncompleted_task_percentage = round(user_uncompleted_task_percentage, 2)
        user_uncompleted_task_percentage_dictionary[name] = user_uncompleted_task_percentage

    for name in user_list:
        # dictionary for user total uncompleted and overdue task percentage
        user_overdue_task_percentage = (user_total_overdue_dictionary[name] / user_total_dictionary[name]) * 100
        user_overdue_task_percentage = round(user_overdue_task_percentage, 2)
        user_overdue_task_percentage_dictionary[name] = user_overdue_task_percentage

    # getting the final string to write to file
    for n in user_list:
        text_line = (str(total_users)
                     + ", " + str(total_task)
                     + ", " + str(user_total_dictionary[n])
                     + ", " + str(n)
                     + ", " + str(user_task_percentage_dictionary[n])
                     + ", " + str(user_completed_task_percentage_dictionary[n])
                     + ", " + str(user_uncompleted_task_percentage_dictionary[n])
                     + ", " + str(user_overdue_task_percentage_dictionary[n]))

        # opeing frile to write
        user_overview_file = open("user_overview.txt", "a+")

        # writing each user line details to the next line of the file
        user_overview_file.write(f"{text_line}\n")

    # closing the files
    user_file.close()
    task_file.close()

# Function - when called  check if the info files exist, if not it requestes use to use "gr" option to generate
# them , once created you can then use the "ds" option to read through all the latest data stored in
# "task_overview.txt" and "user_overview.txt"
def display_statistics():
    file_check_task = os.path.isfile('./task_overview.txt')
    file_check_user = os.path.isfile('./user_overview.txt')

    if file_check_task == False and file_check_user == False:
        print("________________________________________________________")
        print("The information you seek needs to be generated ")
        print("Please select 'gr' in the Admin Menu to generate \nthe information to report ")
        main_menu(user_select)
        ######################
    else:
        task_overview_file = open("task_overview.txt", "r")
        task_overview_content = task_overview_file.readline()
        total_task, total_completed, total_incomplete, total_overdue, percentage_incomplete, percentage_task_overdue \
            = task_overview_content.split(", ")

        print("________________________________________________________")
        print("Task over view Information ")
        print("________________________________________________________")
        print(f"Total number of Tasks:               {total_task}")
        print(f"Total number of completed Tasks:     {total_completed}")
        print(f"Total number of incomplete Tasks:    {total_incomplete}")
        print(f"Total number of Over Due Tasks:      {total_overdue}")
        print(f"Percentage incomplete Tasks:         {percentage_incomplete}")
        print(f"Percentage of Overdue Tasks:         {percentage_task_overdue}")
        print(" ")

        user_overview_file = open("user_overview.txt", "r")
        user_overview_content = user_overview_file.readlines()

        for line in user_overview_content:
            total_users, total_task, user_total_dictionary, user_name, user_task_percentage, \
            user_completed_task_percentage, user_uncompleted_task_percentage, user_overdue_task_percentage \
                = line.split(", ")

            print("__________________________________________________________")
            print(f"{user_name.upper()} Overview Information: ")
            # print("________________________________________________________")

            # print(f"total number of users is {total_users}")
            # print(f"total task  is {total_task}")

            print("| Total | Task % | Completed % | Incomplete % | Over Due % ")
            print(f"    {user_total_dictionary}     {user_task_percentage}       {user_completed_task_percentage}"
                  f"           {user_uncompleted_task_percentage}         {user_overdue_task_percentage}")
            '''print(f"list of usernames {user_name}")
            print(f"username and task total {user_total_dictionary}")
            print(f"username and task percentage {user_task_percentage}")
            print(f"username and completed task percentage {user_completed_task_percentage}")
            print(f"username and uncompleted task percentage {user_uncompleted_task_percentage}")
            print(f"username and overdue task percentage {user_overdue_task_percentage}")'''

        task_overview_file.close()
        user_overview_file.close()


# Main Program

# assigning base values
user_select = "o"

# call log in function
user_name = log_in()

user_select = "o"
main_menu(user_select)
