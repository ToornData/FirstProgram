fn = ["JOHN", "AMELIA", "RANDOLF"]
#THIS IS THE LIST WHERE ALL FIRST NAMES ARE STORED, ABOVE ARE THE NAMES I HAVE ADDED IN ADVANCE

ln = ["DOE", "GOODWIN", "SMITH"]
#THIS IS THE LIST WHERE ALL LAST NAMES ARE STORED, ABOVE ARE THE NAMES I HAVE ADDED IN ADVANCE

phone = ["111-111-1111", "232-323-2333", "800-888-8988"]
#THIS IS THE LIST WHERE ALL PHONE NUMBERS ARE STORED, ABOVE ARE THE PHONE NUMBERS I HAVE ADDED IN ADVANCE

age = ["42", "29", "18"]
#THIS IS THE LIST WHERE ALL AGES ARE STORED, ABOVE ARE THE AGES I HAVE ADDED IN ADVANCE

popped_item = []
#THIS IS THE LIST WHERE ALL POPPED ITEMS WILL BE PUT WHILE DELETING RECORDS

truelist = []
#THS IS THE LIST WHERE NAMES THAT ARE FOUND WILL BE TEMPORARILY STORED -- SEE CHOICE 1 RAM 1 FOR MORE INFO

i = 1
#i IS WHAT I USE FOR RUNNING THE PROGRAM

while i > 0 :

    print()
    print("MAIN MENU")
    print("Please select an option")
    print("(1) Exit")
    print("(2) Check in a new patient") 
    print("(3) Check out a patient") 
    print("(4) Patient inquiry")
    print("(5) About the program/dev")
    print()
    choice = input()
    try :
        choice = int(choice)

        #CHOICE 1 IS IF YOU WANT TO EXIT THE SYSTEM -- I HAVE ADDED THE UPPER COMMAND IN CASE THE USER IS LAZY AND JUST TYPES "y"
        if choice == 1 :
            print()
            print("WARNING: Continuing will delete all modified data, do you want to proceed?")
            print("Select (Y)es or (N)o.")
            print()
            ram = input()
            ram = ram.upper()
            if ram == "Y":
                exit()
            elif ram == "N" :
                print("Returning to main menu.")
                print()
            else :
                print("Entry not valid, returning to main menu") 
                print()

        #CHOICE 2 IS IF YOU WANT TO ADD A NEW PATIENT -- ONE THING OF INTEREST IS THAT ALL NAMES INPUT ARE AUTOMATICALLY CAPITALIZED FOR STORAGE & EASE OF SEARCHING
        elif choice == 2 :
            print("ADD A NEW PATIENT")
            ram = input("What is the patient's first name? ") 
            fn.append(str(ram).upper())
            print()
            ram = input("What is the patient's last name? ") 
            ln.append(str(ram).upper())
            print()
            print("What is the patient's phone number? ")
            print("Please use the format ###-###-####")
            ram = input() 
            phone.append(ram)
            print()
            ram = input("What is the patient's age? ")
            age.append(ram)
            print()
            #AS YOU CAN SEE, IT IS A VERY SIMPLE SET OF STEPS WHERE YOU JUST APPEND THE LISTS

        #CHOICE 3 IS IF YOU WANT TO REMOVE A PATIENT      
        elif choice == 3 :
            j = 1
            while j > 0:
                #BELOW IS THE MAIN MENU
                print()  
                print("PATIENT REMOVAL MENU")
                print("How would you like to search for the patient?")
                print("(1) First Name")
                print("(2) Last Name")
                print("(3) Phone Number")
                print("(4) Return to main menu")
                ram = input()
                print ()

                #RAM1 SELECTION WILL CHECK FIRST NAMES AND, IF THERE ARE DUPLICATES, WILL REQUEST A LAST NAME TO CORRELATE RECORDS
                if ram == "1":
                    print("What is the patient's first name?")
                    nameram = input()
                    nameram = nameram.upper()
                    truelist = []
                    #I MADE A "c" LOOP FUNCTION TO CHECK IF EACH ITEM IN THE LIST CONTAINS THE NAME THAT HAS BEEN INPUT -- IF IT DOES, ITS INDEX IS ADDED TO TRUELIST
                    try :
                        c = 0
                        while c < len(fn) :
                            j = fn[c].__contains__(nameram)
                            if j == True :
                                truelist.append(c)
                                c += 1
                            else:
                                c+= 1
                        if len(truelist) > 1 :
                            #TRUELIST WOULD ONLY REACH A LENGTH OF 2+ IF THERE ARE MULTIPLE HITS, HENCE WHY THIS SECONDARY FUNCTION RUNS TO NARROW THE SEARCH
                            print(f"{len(truelist)} results have been found for this search")
                            print("Please enter patient's last name.")
                            nameram1 = input()
                            nameram1 = nameram1.upper()
                            nameram1 = ln.index(nameram1)
                            if nameram == fn[nameram1] :
                                print()
                                fn_ram = fn[nameram1]
                                ln_ram = ln[nameram1]
                                popped_item.append(fn.pop(nameram1)) 
                                popped_item.append(ln.pop(nameram1))
                                age.pop(nameram1)
                                phone.pop(nameram1)
                                print(f"{fn_ram} {ln_ram}'s records have been deleted, returning to main menu")
                                popped_item.clear()
                                print()                             
                            else :
                                print()
                                print("That name could not be found, returning to main menu.")  
                                print()                           

                        elif len(truelist) == 1 :
                        #IF TRUELIST ONLY HAS ONE ENTRY, IT MUST BE THE CORRECT NAME, THEREFORE I USE TRUELIST[0] AS THE INDEX FOR THE POPPING
                            print()
                            fn_ram = fn[truelist[0]]
                            ln_ram = ln[truelist[0]]
                            popped_item.append(fn.pop(truelist[0])) 
                            popped_item.append(ln.pop(truelist[0]))
                            age.pop(truelist[0])
                            phone.pop(truelist[0])
                            print(f"{fn_ram} {ln_ram}'s records have been deleted, returning to main menu")
                            popped_item.clear()
                            print()
                        elif len(truelist) < 1 :
                            print()
                            print("That name could not be found, returning to main menu.")  
                            print()
                    except : 
                        print("Error, nothing found with that search criteria.")

                #RAM2 SELECTION WILL DO THE SAME BUT INVERSE (LAST NAME SEARCH WITH A FIRST NAME SECONDARY)
                if ram == "2":
                    print("What is the patient's last name?")
                    nameram = input()
                    nameram = nameram.upper()
                    truelist = []
                    try :
                        c = 0
                        while c < len(ln) :
                            j = ln[c].__contains__(nameram)
                            if j == True :
                                truelist.append(c)
                                c += 1
                            else:
                                c+= 1
                        if len(truelist) > 1 :
                            print(f"{len(truelist)} results have been found for this search")
                            print("Please enter patient's first name.")
                            nameram1 = input()
                            nameram1 = nameram1.upper()
                            nameram1 = fn.index(nameram1)
                            if nameram == ln[nameram1] :
                                print()
                                fn_ram = fn[nameram1]
                                ln_ram = ln[nameram1]
                                popped_item.append(fn.pop(nameram1)) 
                                popped_item.append(ln.pop(nameram1))
                                age.pop(nameram1)
                                phone.pop(nameram1)
                                print(f"{fn_ram} {ln_ram}'s records have been deleted, returning to main menu")
                                popped_item.clear()
                                print()                          

                        elif len(truelist) == 1 :
                            print()
                            fn_ram = fn[truelist[0]]
                            ln_ram = ln[truelist[0]]
                            popped_item.append(fn.pop(truelist[0])) 
                            popped_item.append(ln.pop(truelist[0]))
                            age.pop(truelist[0])
                            phone.pop(truelist[0])
                            print(f"{fn_ram} {ln_ram}'s records have been deleted, returning to main menu")
                            popped_item.clear()
                            print()

                        elif len(truelist) < 1 :
                            print()
                            print("That name could not be found, returning to main menu.")  
                            print()
                    except : 
                        print("Error, nothing found with that search criteria.")

                #RAM3 SELECTION WILL CHECK PHONE NUMBERS AND CORRELATE THEM WITH FIRST NAMES (EX. A FAMILY IS SHARING A PHONE NUMBER)
                if ram == "3":
                    print("What is the patient's phone number?")
                    print("Please use the format ###-###-####")
                    nameram = input()
                    nameram = nameram.upper()
                    truelist = []
                    try :
                        c = 0
                        while c < len(phone) :
                            j = phone[c].__contains__(nameram)
                            if j == True :
                                truelist.append(c)
                                c += 1
                            else:
                                c+= 1
                        if len(truelist) > 1 :
                            print(f"{len(truelist)} results have been found for this search")
                            print("Please enter patient's first name.")
                            nameram1 = input()
                            nameram1 = nameram1.upper()
                            nameram1 = fn.index(nameram1)
                            if nameram == phone[nameram1] :
                                print()
                                fn_ram = fn[nameram1]
                                ln_ram = ln[nameram1]
                                popped_item.append(fn.pop(nameram1)) 
                                popped_item.append(ln.pop(nameram1))
                                age.pop(nameram1)
                                phone.pop(nameram1)
                                print(f"{fn_ram} {ln_ram}'s records have been deleted, returning to main menu")
                                popped_item.clear()
                                print()                         
                            else :
                                print()
                                print("That name could not be found, returning to main menu.")  
                                print()                           

                        elif len(truelist) == 1 :
                            print()
                            fn_ram = fn[truelist[0]]
                            ln_ram = ln[truelist[0]]
                            popped_item.append(fn.pop(truelist[0])) 
                            popped_item.append(ln.pop(truelist[0]))
                            age.pop(truelist[0])
                            phone.pop(truelist[0])
                            print(f"{fn_ram} {ln_ram}'s records have been deleted, returning to main menu")
                            popped_item.clear()
                            print()

                        elif len(truelist) < 1 :
                            print()
                            print("That name could not be found, returning to main menu.")  
                            print()
                    except : 
                        print("Error, nothing found with that search criteria.")
                #RAM 4 IS TO EXIT TO THE MAIN MENU -- I HAVE ACHIEVED THIS BY HAVING THE J LOOP STOP WHEN 4 RAM 4 IS SELECTED
                elif ram == "4":
                    j = 0

        #CHOICE 4 IS IF YOU WANT TO DISPLAY A PATIENT'S RECORDS
        elif   choice == 4 :
            j = 1
            while j > 0:
                print()  
                print("PATIENT SEARCH MENU")
                print("How would you like to search for the patient?")
                print("(1) First Name")
                print("(2) Last Name")
                print("(3) Phone Number")
                print("(4) Return to main menu")
                ram = input()
                print ()

                #RAM1 SELECTION WILL CHECK FIRST NAMES AND, IF THERE ARE DUPLICATES, WILL REQUEST A LAST NAME TO CORRELATE RECORDS
                if ram == "1":
                    print("What is the patient's first name?")
                    nameram = input()
                    nameram = nameram.upper()
                    truelist = []
                    try :
                        c = 0
                        while c < len(fn) :
                            j = fn[c].__contains__(nameram)
                            if j == True :
                                truelist.append(c)
                                c += 1
                            else:
                                c+= 1
                        if len(truelist) > 1 :
                            print(f"{len(truelist)} results have been found for this search")
                            print("Please enter patient's last name.")
                            nameram1 = input()
                            nameram1 = nameram1.upper()
                            nameram1 = ln.index(nameram1)
                            if nameram == fn[nameram1] :
                                print ()
                                print(f"Patient's name : {fn[nameram1]} {ln[nameram1]}")
                                print("Age: ", age[nameram1])
                                print("Phone number: ", phone[nameram1])
                                print()                           
                            else :
                                print()
                                print("That name could not be found, returning to main menu.")  
                                print()                           

                        elif len(truelist) == 1 :
                            print()
                            print(f"Patient's name : {fn[truelist[0]]} {ln[truelist[0]]}")
                            print("Age: ", age[truelist[0]])
                            print("Phone number: ", phone[truelist[0]])
                            print()
                        elif len(truelist) < 1 :
                            print()
                            print("That name could not be found, returning to main menu.")  
                            print()
                    except : 
                        print("Error, nothing found with that search criteria.")

                #RAM2 SELECTION WILL DO THE SAME BUT INVERSE (LAST NAME SEARCH WITH A FIRST NAME SECONDARY)
                if ram == "2":
                    print("What is the patient's last name?")
                    nameram = input()
                    nameram = nameram.upper()
                    truelist = []
                    try :
                        c = 0
                        while c < len(ln) :
                            j = ln[c].__contains__(nameram)
                            if j == True :
                                truelist.append(c)
                                c += 1
                            else:
                                c+= 1
                        if len(truelist) > 1 :
                            print(f"{len(truelist)} results have been found for this search")
                            print("Please enter patient's first name.")
                            nameram1 = input()
                            nameram1 = nameram1.upper()
                            nameram1 = fn.index(nameram1)
                            if nameram == ln[nameram1] :
                                print ()
                                print(f"Patient's name : {fn[nameram1]} {ln[nameram1]}")
                                print("Age: ", age[nameram1])
                                print("Phone number: ", phone[nameram1])
                                print()                           
                            else :
                                print()
                                print("That name could not be found, returning to main menu.")  
                                print()                           

                        elif len(truelist) == 1 :
                            print()
                            print(f"Patient's name : {fn[truelist[0]]} {ln[truelist[0]]}")
                            print("Age: ", age[truelist[0]])
                            print("Phone number: ", phone[truelist[0]])
                            print()
                        elif len(truelist) < 1 :
                            print()
                            print("That name could not be found, returning to main menu.")  
                            print()
                    except : 
                        print("Error, nothing found with that search criteria.")

                #RAM3 SELECTION WILL CHECK PHONE NUMBERS AND CORRELATE THEM WITH FIRST NAMES (EX. A FAMILY IS SHARING A PHONE NUMBER)
                if ram == "3":
                    print("What is the patient's phone number?")
                    print("Please use the format ###-###-####")
                    nameram = input()
                    nameram = nameram.upper()
                    truelist = []
                    try :
                        c = 0
                        while c < len(phone) :
                            j = phone[c].__contains__(nameram)
                            if j == True :
                                truelist.append(c)
                                c += 1
                            else:
                                c+= 1
                        if len(truelist) > 1 :
                            print(f"{len(truelist)} results have been found for this search")
                            print("Please enter patient's first name.")
                            nameram1 = input()
                            nameram1 = nameram1.upper()
                            nameram1 = fn.index(nameram1)
                            if nameram == phone[nameram1] :
                                print ()
                                print(f"Patient's name : {fn[nameram1]} {ln[nameram1]}")
                                print("Age: ", age[nameram1])
                                print("Phone number: ", phone[nameram1])
                                print()                           
                            else :
                                print()
                                print("That name could not be found, returning to main menu.")  
                                print()                           

                        elif len(truelist) == 1 :
                            print()
                            print(f"Patient's name : {fn[truelist[0]]} {ln[truelist[0]]}")
                            print("Age: ", age[truelist[0]])
                            print("Phone number: ", phone[truelist[0]])
                            print()
                        elif len(truelist) < 1 :
                            print()
                            print("That name could not be found, returning to main menu.")  
                            print()
                    except : 
                        print("Error, nothing found with that search criteria.")

                elif ram == "4":
                    j = 0
        
        #CHOICE 5 IS FOR THE README TEXTS
        elif   choice == 5 :
            j = 1
            while j > 0 :
                print()
                print("README MAIN MENU")
                print("Please select an option")
                print("(1) Program Function")
                print("(2) About the Dev") 
                print("(3) Exit") 
                print()
                ram = input()

                if ram == "1" :
                    mar = 19873425987984375987549238725
                    while mar == 19873425987984375987549238725 :
                        print()
                        print("This is a program I made for 'Hospital X' to keep records of their patients. The information collected includes the patient's")
                        print("first name, last name, phone number, and age. The users of this program are able to add patients, remove patients, and access")
                        print("patient records. This program allows users to narrow the search terms by adding a second keyword if there are multiple people")
                        print("that share the first keyword. The program does, however, not allow you to search by age as that would just be silly.")
                        print()
                        print()
                        print("Known errors that I ran out of time to fix today:")
                        print("1) If there are people that share the second keyword, it will only pull the records if they are the first one in the list. This is")
                        print("due to the limitations on .index() and I ran out of timme to find a workaround. It is my first project after all...")
                        print("2) Hospital 'X' isn't real.")
                        print()
                        print()
                        print("Press enter to exit.")
                        mar = input()

                elif ram == "2" :
                    mar = 19873425987984375987549238725
                    while mar == 19873425987984375987549238725 :
                        print()
                        print("If you are reading this, welcome! This is my very first Python project and I am excited to share it with whoever is reading this. This ")
                        print("project has taken me about 5 hours to complete and while there is more I can do, I am happy with where it is at for a first project.")
                        print("In the actual code I have written how it functions so if you delve into it and can find better ways to accomplish functions, please")
                        print("reach out! My only Python experience is a 1 hour youtube video so I know there are better ways to code & I just need to find them")
                        print("My eventual goal is to get good with python and transition into cybersecurity but I know that is a ways away right now. Anywho, thank")
                        print("you for taking the time to look at my program and read through this.")
                        print()
                        print("All the best,")
                        print("-Toorn")
                        print()
                        print()
                        print("Press enter to exit")
                        mar = input()

                elif ram == "3" :
                    j = 0
    
    except :
        print("Error, please select another option")
