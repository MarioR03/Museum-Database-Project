import mysql.connector


def admin_console(cur):
    #Loop until the user wants to close the program
    while True:
        #Asks the USER what they want to do
        choice = input("\nYou are in ADMIN mode. Type\n1- To type an SQL command\n2- To provide a .sql script file to run on MySQL\n3- To exit the program\n")
        #loop to make sure USER inputs the correct value
        while choice not in ["1","2","3"]:
            choice = input("Invalid input. Must be 1, 2 or 3: ")
       
        #Clearing everything inside of the cursur
        cur.fetchall()

        if choice == "3":                                       #terminante the program
            terminate()

        elif choice == "1":   #Executing the given command
            tryagain = None
            while True:
                command = input("Type your SQL command:\n")
                try:
                    cur.execute(command)
                except Exception:
                    tryagain = input("\nERROR: SQL command not valid. Please get familiar with the database tables and MySQL syntax\n\n1- Try again\n2- Go back\n")
                else:
                    break
                if tryagain == "2":
                    break

    

            #Checking if command was a Query and then printing off the outputs from the query
            if (("select" in command) or ("SELECT" in command) or ("Select" in command)) and (tryagain != "2") :
                print_tables(cur)

        elif choice == "2":
            file_path = input("Enter the .sql file path:\n")
            #Importing the file
            user_file = open(file_path, 'r')
            usersql_File = user_file.read()
            user_file.close()
            #Turning the long string of sql commands into a list of separate strings of sql commands
            sqlcommands = usersql_File.split(';')
            #Running each command one by one
            for command in sqlcommands:
                try:
                    if command.strip() != '':
                        cur.execute(command)
                except mysql.connector.error as msg:
                    print("command skipped: ", msg)

def data_entry(cur):
    table_dict = {1:"ART_OBJECTS", 2:"ARTIST", 3:"EXHIBITION", 4:"PAINTING", 5:"OTHER", 6:"SCULPTURE_STATUE", 7:"PERMANENT_COLLECTION", 8:"BORROWED", 9:"COLLECTIONS"}
    while True:
        print("\n\nYou are in DATA_ENTRY mode.")
        choice = int(input("What would you like to do?\n1- Look up tables\n2- Insert new tuples\n3- Update or delete tuples\n4- Exit the program\n"))
        while choice not in list(range(1,5)):
            choice = int(input("Invalid input. Must be 1, 2, 3 or 4\n"))
        
        if choice == 1:
            table = int(input("Which table would you like to look up?\n1- ART_OBJECTS\n2- ARTIST\n3- EXHIBITION\n4- PAINTING\n5- OTHER\n6- SCULPTURE_STATUE\n7- PERMANENT_COLLECTION\n8- BORROWED\n9- COLLECTIONS\n"))
            while table not in list(range(1,10)):
                table = input("invalid input. Must be 1, 2, 3, 4, 5, 6, 7, 8 or 9: ")
            
            command = "SELECT * FROM "
            if table == 1:
                command = command + "ART_OBJECTS"
            if table == 2:
                command = command + "ARTIST"
            if table == 3:
                command = command + "EXHIBITION"
            if table == 4:
                command = command + "PAINTING"
            if table == 5:
                command = command + "OTHER"
            if table == 6:
                command = command + "SCULPTURE_STATUE"
            if table == 7:
                command = command + "PERMANENT_COLLECTION"
            if table == 8 :
                command = command + "BORROWED"
            if table == 9:
                command = command + "COLLECTIONS"
            cur.execute(command)
            print_tables(cur)

        if choice == 2:
            choice2 = int(input("\nWould you like to\n1- Pass in a file\n2- Use the premade prompts\n"))
            table = int(input("\n\nWhich table do you wish to insert data?\n1- ART_OBJECTS\n2- ARTIST\n3- EXHIBITION\n4- PAINTING\n5- OTHER\n6- SCULPTURE_STATUE\n7- PERMANENT_COLLECTION\n8- BORROWED\n9- COLLECTIONS\n10- To go back\n"))

            if choice2 == 1:                        #Only works if file consists of lines of individual tuples that fit into the attributes of the table selected
                if table in list(range(1,9)):
                    file_path = input("Enter the file path: ")
                    fd = open(file_path, 'r')
                    sqlFile = fd.read()
                    fd.close()
                    #Create the DataBase
                    sqltuples = sqlFile.split('\n')
                    for tuple in sqltuples:
                        try:
                            if tuple.strip() != '':
                                command = "INSERT INTO " + table_dict[table] + " VALUES " + tuple
                                cur.execute(command)
                        except mysql.connector.error as msg:
                            print("command skipped: ", msg)
                    cnx.commit()

            if choice2 == 2:
                while table not in list(range(1,11)):
                    table = int(input("Invalid input. Must be 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10: "))
                if table == 1:                      #ART_OBJECTS
                    command = "INSERT INTO ART_OBJECTS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    val1 = input("Enter the Identification Number: ") or None
                    val2 = input("Enter the Exhibition Name: ") or None
                    val3 = input("Enter the Artist Name: ") or None
                    val4 = input("Enter the Country/Culture of Origin: ") or None
                    val5 = input("Enter the Epoch: ") or None
                    val6 = input("Enter the Year: ") or None
                    val7 = input("Enter the Title: ") or None
                    val8 = input("Enter the Description: ") or None

                    table_tuple = (val1,val2,val3,val4,val5,val6,val7,val8)
                
                elif table == 2:                    #ARTIST
                    command = "INSERT INTO ARTIST VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val1 = input("Enter the Artist Name: ") or None
                    val2 = input("Enter the Epoch: ") or None
                    val3 = input("Enter the Birth Date: ") or None
                    val4 = input("Enter the Death Date: ") or None
                    val5 = input("Enter the Country: ") or None
                    val6 = input("Enter the Main Style: ") or None
                    val7 = input("Enter the Description: ") or None

                    table_tuple = (val1,val2,val3,val4,val5,val6,val7)
                
                elif table == 3:                    #EXHIBITION
                    command = "INSERT INTO EXHIBITION VALUES (%s, %s, %s)"
                    val1 = input("Enter the Exhibition Name: ") or None
                    val2 = input("Enter the Start Date: ") or None
                    val3 = input("Enter the End Date: ") or None

                    table_tuple = (val1,val2,val3)

                elif table == 4:                    #PAINTING

                    command = "INSERT INTO PAINTING VALUES (%s, %s, %s, %s)"
                    val1 = input("Enter the Identification Number: ") or None
                    val2 = input("Enter the Paint Type: ") or None
                    val3 = input("Enter the Drawn on: ") or None
                    val4 = input("Enter the Style: ") or None

                    table_tuple = (val1,val2,val3,val4)     

                elif table == 5:                    #OTHER
                    command = "INSERT INTO OTHER VALUES (%s, %s, %s)"
                    val1 = input("Enter the Identification Number: ") or None
                    val2 = input("Enter the Type: ") or None
                    val3 = input("Enter the Style: ") or None

                    table_tuple = (val1,val2,val3)
                
                elif table == 6:                    #SCULPTURE_STATUE
                    command = "INSERT INTO SCULPTURE_STATUE VALUES (%s, %s, %s, %s, %s)"
                    val1 = input("Enter the identification number: ") or None
                    val2 = input("Enter the Material: ") or None
                    val3 = input("Enter the Height: ") or None
                    val4 = input("Enter the Style: ") or None
                    val5 = input("Enter the Weight: ") or None

                    table_tuple = (val1,val2,val3,val4,val5)
                
                elif table == 7:                    #PERMANENT_COLLECTION
                    command = "INSERT INTO PERMANENT_COLLECTIONS VALUES (%s, %s, %s, %s)"
                    val1 = input("Enter the Identification Number: ") or None
                    val2 = input("Enter the Date aquired: ") or None
                    val3 = input("Enter the Cost: ") or None
                    val4 = input("Enter the Status: ") or None
                
                    table_tuple = (val1,val2,val3,val4)
                
                elif table == 8:                    #BORROWED
                    command = "INSERT INTO BORROWED VALUES (%s, %s, %s, %s)"
                    val1 = input("Enter the Identification Number: ") or None
                    val2 = input("Enter the Collection Name: ") or None
                    val3 = input("Enter the Date Borrowed: ") or None
                    val4 = input("Enter the Date Returned: ") or None

                    table_tuple = (val1,val2,val3,val4)
                
                elif table == 9:                    #COLLECTIONS
                    command = "INSERT INTO COLLECTIONS VALUES (%s, %s, %s, %s, %s, %s)"
                    val1 = input("Enter the Collection Name: ") or None
                    val2 = input("Enter the Type: ") or None
                    val3 = input("Enter the Description ") or None
                    val4 = input("Enter the Address: ") or None
                    val5 = input("Enter the Phone: ") or None
                    val6 = input("Enter the Contant Person: ") or None

                    table_tuple = (val1,val2,val3,val4,val5,val6)

                elif table == 10:                   #Do nothing
                    pass

                if table in list(range(1,10)):        #execute the command
                    try:
                        cur.execute(command, table_tuple)
                    except Exception as msg:
                        print("command skipped, against constraint rules: ", msg)
                    
                cnx.commit()

        if choice == 3:
            table = int(input("\n\nWhich table do you wish to update/detete data?\n1- ART_OBJECTS\n2- ARTIST\n3- EXHIBITION\n4- PAINTING\n5- OTHER\n6- SCULPTURE_STATUE\n7- PERMANENT_COLLECTION\n8- BORROWED\n9- COLLECTIONS\n10- To go back\n"))
            while table not in list(range(1,11)):
                table = int(input("Invalid input. Must be 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10\n"))

            choice1 = int(input("\nDo you wish to\n1- Update\n2- Delete\n3- Go back\n"))
            while choice1 not in list(range(1,4)):
                choice1 = int(input("Invalid input. Must be 1, 2 or 3"))
    
            if choice1 == 1:                                           #CODE TO UPDATE TUPLES
                command = "UPDATE " + table_dict[table] + " SET "

                if table == 1:
                    id = input("Enter the ID number of the tuple you wish to update: ")
                    attribute = int(input("\nWhich attribute do you wish to update?\n1- ID_no\n2- ExName\n3-ArName\n4-Country/Culture of Origin\n5- Epoch\n6- Year\n7- Title\n8- Description\n9- Go back\n"))
                    while attribute not in list(range(1,10)):
                        attribute = int(input("Invalid input. Must be 1, 2, 3, 4, 5, 6, 7, 8, or 9: "))

                    attribute_dict = {1: "ID_no", 2: "ExName", 3: "ArName", 4:"Country_Culture_Origin", 5: "Epoch", 6: "Year_made", 7: "Title", 8: "Descript"}
                    
                if table == 2:
                    id = input("Enter the name of the artist you wish to update: ")
                    attribute = int(input("\nWhich attribute do you wish to update?\n1- AName\n2- BirthDate\n3- DeathDate\n4- Country\n5- Epoch\n6- Main_Style\n7- ADescript\n8- Go back\n"))
                    while attribute not in list(range(1,9)):
                        attribute = int(input("Invalid input. Must be 1, 2, 3, 4, 5, 6, 7 or 8: "))

                    attribute_dict = {1: "AName", 2: "BirthDate", 3: "DeathDate", 4: "Country", 5:"Epoch", 6: "Main_Style", 7:"ADescript"}

                if table == 3:
                    id = input("Enter the name of the exhibition you wish to update: ")
                    attribute = int(input("\nWhich attribute do you wish to update?\n1- EName\n2- End_Date\n3- Start_Date\n4- Go back\n"))
                    while attribute not in list(range(1,5)):
                        attribute = int(input("Invalid input. Must be 1, 2, 3 or 4: "))

                    attribute_dict = {1:"EName", 2:"End_Date", 3: "Start_Date"}
                
                if table == 4:
                    id = input("Enter the ID number of the tuple you wish to update: ")
                    attribute = int(input("\nWhich attribute do you wish to update?\n1- ID_no\n2- Paint_type\n3- Drawn_on\n4- Style\n5- Go back\n"))
                    while attribute not in list(range(1,6)):
                        attribute = int(input("Invalid input. Must be 1, 2, 3, 4 or 5: "))
                    
                    attribute_dict = {1: "ID_no", 2: "Paint_type", 3: "Drawn_on", 4: "Style"}

                if table == 5:
                    id = input("Enter the ID number of the tuple you wish to update: ")
                    attribute = int(input("Which attribute do you wish to update?\n1- ID_no\n2- Type_of_art\n3- Style\n4- Go back\n"))
                    while attribute not in list(range(1, 5)):
                        attribute = int(input("Invalid input. Must be 1, 2, 3 or 4: "))

                    attribute_dict = {1: "ID_no", 2: "Type_of_art", 3: "Style"}

                if table == 6:
                    id = input("Enter the ID number of the tuple you wish to update: ")
                    attribute = int(input("\nWhich attribute do you wish to update?\n1- ID_no\n2- Material\n3- Style\n4- Height\n5- Weight\n6- Go back\n"))
                    while attribute not in list(range(1,7)):
                        attribute = int(input("Invalid input. Must be 1, 2, 3, 4, 5 or 6: "))
                    
                    attribute_dict = {1: "ID_no", 2: "Material", 3:"Style", 4:"Height", 5:"Weight"}

                if table == 7:
                    id = input("Enter the ID_no of the tuple you wish to update: ")
                    attribute = int(input("\nWhich attribute do you wish to update?\n1- ID_no\n2- Date_aquired\n3- Cost\n4- Status_is\n5- Go back\n"))
                    while attribute not in list(range(1,6)):
                        attribute = int(input("Invalid input. Must be 1, 2, 3, 4 or 5: "))
                    
                    attribute_dict = {1:"ID_no", 2:"Date_aquired", 3: "Cost", 4: "Status_is"}

                if table == 8:
                    id = input("Enter the ID_no of the tuple you wish to update: ")
                    attribute = int(input("\nWhich attribute do you wish to update?\n1- ID_no\n2- CoName\n3- Date_Borrowed\n4- Date_returned\n5- Go back\n"))
                    while attribute not in list(range(1,6)):
                        attribute = int(input("Invalid input. Must be 1, 2, 3, 4 or 5: "))
                    
                    attribute_dict = {1:"ID_no", 2:"CoName", 3: "Date_Borrowed", 4: "Date_Returned"}

                if table == 9:
                    id = input("Enter the Collection name of the tuple you wish to update: ")
                    attribute = int(input("Which attribure do you wish to update?\n1- CName\n2- Type_of_art\n3- Descript\n4- Address\n5- Phone\n6- Contact_person\n7- Go back\n"))
                    while attribute not in list(range(1,8)):
                        attribute = int(input("Invalid input. Must be 1, 2, 3, 4, 5, 6 or 7"))
                    
                    attribute_dict = {1:"CName", 2:"Type_of_art", 3:"Description", 4:"Address", 5:"Phone", 6:"Contact_person"}
                
                if table in list(range(1,9)):
                    change_to = input("Enter new value: ")
                    command = command + attribute_dict[attribute] + " = '" + change_to + "' WHERE " + attribute_dict[1] + " = '" + str(id) + "';"
                    try:
                        cur.execute(command)
                        print("SUCCESSFUL")
                        cnx.commit()
                    except mysql.connector.errors.IntegrityError as err:
                        print("\nERROR: INTEGRITY CONSTRAINT WAS VIOLATED. SKIPPED COMMAND.", err)
                        
                    cnx.commit()

            if choice1 == 2:
                if table == 1:
                    id = input("Enter the ID number of the tuple you wish to delete: ")
                    id = "ID_no = " + "'" + id + "'"
                if table == 2:
                    id = input("Enter the name of the artist you wish to delete: ")
                    id = "AName = " + "'" + id + "'"
                if table == 3:
                    id = input("Enter the name of the exhibition you wish to delete: ")
                    id = "EName = " + "'" + id + "'"
                if table == 4:
                    id = input("Enter the ID number of the tuple you wish to delete: ")
                    id = "ID_no = " + "'" + id + "'"
                if table == 5:
                    id = input("Enter the ID number of the tuple you wish to delete: ")
                    id = "ID_no = " + "'" + id + "'"
                if table == 6:
                    id = input("Enter the ID number of the tuple you wish to delete: ")
                    id = "ID_no = " + "'" + id + "'"
                if table == 7:
                    id = input("Enter the ID_no of the tuple you wish to delete: ")
                    id = "ID_no = " + "'" + id + "'"
                if table == 8:
                    id = input("Enter the ID_no of the tuple you wish to delete: ")
                    id = "ID_no = " + "'" + id + "'"
                if table == 9:
                    id = input("Enter the Collection name of the tuple you wish to delete: ")
                    id = "CName = " + "'" + id + "'"
                if table in list(range(1,10)):
                    command = "DELETE FROM " + table_dict[table] + " WHERE " + id
                    print(command)
                    try:
                        cur.execute(command)
                        print("SUCCESSFUL")
                        cnx.commit()
                    except mysql.connector.errors.IntegrityError as err:
                        print("FAILED")
                        print("\nERROR: INTEGRITY CONSTRAINT WAS VIOLATED. SKIPPED COMMAND.", err)

        if choice == 4:
            terminate()

def view(cur):
    #Loop to keep the program going until the user stops
    while True:
        print("\n\nYou are in VIEW mode. What would you like to browse?")

        choice_1 = input("1- Art pieces\n2- Exhibitions\n3- To exit the program\n")
        #loop to get the correct input from the user
        while choice_1 not in ["1","2","3"]:
            choice_1 = input("Invalid input. Must be 1, 2 or 3: ")
        
        if choice_1 == "1":
            choice_2 = int(input("\nWhat kind of art pieces would you like to see?\n1- Paintings\n2- Sculptures and Statues\n3- Other\n4- Search by ID_number\n5- To exit the program\n"))   #Had to change the input to be an integer type so I don't have to manually create the "IN list"
            while choice_2 not in list(range(1,6)):
                choice_2 = int(input("Invalid input. Must be 1, 2, 3, 4 or 5: "))

            command = "SELECT ID_no"
            if choice_2 == 1:
                choice_3 = input("\nWould you like see the name of the art piece? 'Y' or 'N'\n")
                if (choice_3 == 'Y') or (choice_3 == 'y'):
                    command = command + "," + " Title"
                
                choice_3 = input("\nWould you like see the name of the artist? 'Y' or 'N'\n")
                if (choice_3 == 'Y') or (choice_3 == 'y'):
                    command = command + "," +" ArName"

                command = command + " FROM ART_OBJECTS NATURAL JOIN PAINTING"

                cur.execute(command)
            elif choice_2 == 2:
                choice_3 = input("\nWould you like see the name of the art piece? 'Y' or 'N'\n")
                if (choice_3 == 'Y') or (choice_3 == 'y'):
                    command = command + "," + " Title"
                
                choice_3 = input("\nWould you like see the name of the artist? 'Y' or 'N'\n")
                if (choice_3 == 'Y') or (choice_3 == 'y'):
                    command = command + "," +" ArName"

                command = command + " FROM ART_OBJECTS NATURAL JOIN SCULPTURE_STATUE"

                cur.execute(command)
            elif choice_2 == 3:
                choice_3 = input("\nWould you like see the name of the art piece? 'Y' or 'N'\n")
                if (choice_3 == 'Y') or (choice_3 == 'y'):
                    command = command + "," + " Title"
                
                choice_3 = input("\nWould you like see the name of the artist? 'Y' or 'N'\n")
                if (choice_3 == 'Y') or (choice_3 == 'y'):
                    command = command + "," +" ArName"
            
                command = command + " FROM ART_OBJECTS NATURAL JOIN OTHER"
                cur.execute(command)
            elif choice_2 == 4:
                command = "SELECT * FROM ART_OBJECTS WHERE ID_no = %(ID_number)s"
                search_id = input("\nInsert the ID_number of the art piece you are looking for: ")
                cur.execute(command, {"ID_number":search_id})
            else:
                terminate()
            print_tables(cur)
            
        if choice_1 == "2":
            print("\nThese are the up and comming exhibitions and their contents\n")
            command = "SELECT EName, Start_Date, End_Date, Title FROM EXHIBITION, ART_OBJECTS WHERE Ename = Exname"
            cur.execute(command)
            print_tables(cur)
        
        if choice_1 == "3":
            terminate()

def print_tables(cur):
    #Print off attribute names
    print()
    col_names = cur.column_names
    header_size = len(col_names)
    for attribute in col_names:
        if len(attribute) > 30:
            attribute = attribute[0:28]
        print( "{:<30s}".format(attribute), end = '')
    print()
    print(30*header_size*"-")
    print()


    rows = cur.fetchall()
    for row in rows:
        print()
        for val in row:
            if val == None:
                val = "null"
            elif len(str(val)) > 30:
                val = str(val)[0:28]
            print( "{:30s}".format(str(val)), end = '')
    print()

def terminate():
    '''TERMINATES THE PROGRAM'''
    print("\nPROGRAM TERMINANTED...")
    exit(1)



if __name__=="__main__":

    print("\n\n\nWelcome to the museum_novaecho Database")
    print("\n\nTo access the Database, you must specify what kind of USER you are")
    print("\nEnter the number\n1- DB ADMIN")
    print("2- DATA ENTRY")   
    print("3- DATA BROWSING") 
    user_type = input("\n")

    #Connect to Server
    username = None
    var_pass = None
    print("\nEnter your database username and password")
    if user_type in ["1","2"]:
        username = input("\nuser name: ")
        var_pass = input("\npassword: ")
    else:
        var_guest = input("\nEnter 1 if you would like to log in as a guest. Otherwise, press enter.\n")
        if var_guest == 1:
            username = input("\nuser name: ")
            var_pass = input("\npassword: ")
        else:
            username = input("\nuser name: ")
            var_pass = input("\npassword: ")

    cnx = mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        user = username,                                                        
        password = var_pass)
    

    #Create Cursur
    cur = cnx.cursor()
    #Import the sql file
    fd = open('museum_novecho_database.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    #Create the DataBase
    sqlcommands = sqlFile.split(';')
    for command in sqlcommands:
        try:
            if command.strip() != '':
                cur.execute(command)
        except mysql.connector.error as msg:
            print("command skipped: ", msg)

    if user_type == "1":
        admin_console(cur)
    elif user_type == "2":
        data_entry(cur)
    elif user_type == "3":
        view(cur)