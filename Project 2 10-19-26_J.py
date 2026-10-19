
student_ids = [1000, 1001, 1002, 1003, 1004] #can i just say i find it really silly to use separate lists for ids and names? i'd like to hope there's a reason because
student_names = ["Average Joe","Alex Mercer", "Jordan Lee", "Ivo Robotnik", "Lucy Luanne"] #i think a dictionary would be so much easier. but alas, it's part of the assignment
enrolled_courses = set(["CS101", "MATH201", "ENG102"])

student_grades = { #create a dictionary which maps student id to grades
    1000:[85.5, 80.3, 82.0, 79.7],
    1001:[66.1, 72.0, 79.0, 95.5],
    1002:[49.0, 82.5, 75.5, 63.0],
    1003:[92.0, 85.0, 92.5, 98.5],
    1004:[86.5, 80.0, 81.5, 83.5]
}
student_gpas = { #default values for gpa, option 2 needs to be able to update these
    1000:3.0,
    1001:2.0,
    1002:1.0,
    1003:4.0,
    1004:3.0,
}
GRADE_BOUNDARIES = tuple([90.0, 80.0, 70.0, 60.0]) #create tuple for grade boundaries, i hope i did this right
WEIGHTED_GPAS = tuple([4.0, 3.0, 2.0, 1.0])        #tuple for gpas on a 4.0 scale
GRADE_LETTERS = tuple(["A", "B", "C", "D"])        #tuple for letter grades

application_isactive = True #Set to true by default or else the program doesn't run :P


def format_student_name(full_name): #Matthew M
    """
    Parameters: 
    Full name (string)
    \nReturns:
    Full name with each word capitalized
    """

    qux = [name.capitalize() for name in full_name.strip().split()]
    fred = " ".join(qux)
    return fred #i would recommend against using nonsense names for your temporary variables like i do unless youre sure you understand them

def calculate_gpa(scores, scale=4.0): #Matthew M
    """
    Parameters: scores (list) and scale (float). scale is set by default, not sure if we need it but we'll see.
    \nReturns: tuple containing numeric gpa average at index 0, letter grade as string at index 1, gpa weighted on scale at index 2.
    """

    returned_gpa_letter = "F"
    gpa_avg = sum(scores)/len(scores)
    returned_scaled_gpa = 0.0

    for (i, cutoff) in enumerate(GRADE_BOUNDARIES): 
        if(gpa_avg >= cutoff): #example: if gpa_avg = 91 then 91 >= 90, i is 0 and GRADE_LETTERS[0] is "A"
            returned_gpa_letter = GRADE_LETTERS[i] 
            returned_scaled_gpa = WEIGHTED_GPAS[i]
            break #break out of the loop, or else it just keeps going and overwrites the correct grade
            

    return tuple([gpa_avg, returned_gpa_letter, returned_scaled_gpa])

def evaluate_risk_standing(gpa, probation_cutoff=2.0, deans_cutoff = 3.5): #Matthew M
    """
    Parameters: gpa (float), probation cutoff (float), deans cutoff (float)
    \nReturns: Academic status as a string. Probation risk if below probation cutoff. 
    Dean's list if above deans cutoff. Good standing otherwise.
    """
    qux = "Good Standing"

    if gpa < probation_cutoff:
        qux = "Probation Risk"
    elif gpa >= deans_cutoff:
        qux = "Dean's List"
    return qux

def filter_students_by_status(student_ids, gpas, target_status): #Matthew M
    """
    Parameters: student_ids(list), gpas(dict), target_status(str)
    \nReturns: list of students who match target_status
    """
    tmp_dict = {} #initialize a temporary master dictionary as empty

    for id, num in gpas.items():
        tmp_dict[id] = evaluate_risk_standing(num) #tmp_dict now contains id-status pairs. easy to compare against target_status

    tmp_dict = {id:status for id, status in tmp_dict.items() if status == target_status} #rearrange tmp_dict only keeping ids with statuses matching target
    returned_list = list(tmp_dict.keys())
    return returned_list

def generate_analytics_summary(parameter_grades=student_grades): #Matthew M

    """
    Parameters: parameter_grades(dict)
    \nReturns: dict containing count of scores in parameter grades, highest, lowest and average as a dict
    """

    allscores = [score for list in parameter_grades.values() for score in list]

    returned_summary = {
        "Count":len(allscores),
        "Highest":max(allscores),
        "Lowest":min(allscores),
        "Average":(sum(allscores)/len(allscores))
    }
    return returned_summary

def rearrange_student_ids(): #Matthew M
    list_of_tuples_to_sort = []

    for index, ID in enumerate(student_ids):
        tmp_tuple = tuple([ID, student_names[index]])
        list_of_tuples_to_sort.append(tmp_tuple) #create tuple containing the student name and ID

    list_of_tuples_to_sort = sorted(list_of_tuples_to_sort) #sort list of tuples based on ID 
    for index, sorted_student in enumerate(list_of_tuples_to_sort):           
        student_ids[index] = sorted_student[0]
        student_names[index] = sorted_student[1]
    #print(student_ids, "\n", student_names) #print statement to check if the database is internally correct or if the displays later just so happen to fix them

# ^^ this last one isnt necessary for the grade but i didnt like how the use of lists meant we could get a database thats out of order

while application_isactive == True: 

    print("\nMENU:\n\n1. Add New Student Record\n\n2. Compute GPAs & Academic Averages\n\n3. Display Grade Roster\n")
    print("4. Search for Student & Flag Academic Risk\n\n5. Class Statistics\n")

    while True: #this loop will repeat forever until the user enters a valid input
        try: #try statements attempt to do whatever is inside them. if it gets the error expected in the except block, it will do that instead
            user_input = int(input("Select an option (1-5), 0 to exit: "))
            break      #this lets us escape the infinite loop caused by writing "while True:"
        except ValueError:
            print("ERROR: Invalid Command")


    if(user_input == 0):              #this is our input check. start by checking if its the exit command.
        application_isactive = False
    elif(user_input in range(1,6)):   #this actually checks if its 1 through 5. The 6 at the end is exclusive.


        if user_input==1: #Option 1: Add New Student Record by Matthew M.
            new_id = input("Input new student ID: ")

            if new_id.isdigit() and len(new_id) == 4: #if new id is the correct format
                new_id = int(new_id) #cast input from string to int type

                if new_id not in student_ids:
                    print("Valid new ID.")

                    new_name = format_student_name(input("Input full student name: "))
                    new_courses = [course.upper() for course in input("Input course names separated by space: ").strip().split()]
                    new_grades = []

                    scores_input_list = input("Input grades separated by commas. Only accepts digits and one decimal: ").strip().split(',')
                    successful_loop_count = 0 #gonna use this to make sure at the end that we only add the new student data if nothing went wrong.

                    for score in scores_input_list:
                        score = score.strip() #each score needs to be individually stripped of whitespace or else it fails the check below

                        if score.count('.') <= 1 and score.replace('.','').isdigit() and (0 <= float(score) <= 100): #check if score is in valid format
                            new_grades.append(float(score))
                            successful_loop_count += 1

                        else:
                            print(f"[ERROR] {score} was not an acceptable input and was rejected. Aborting Option 1.")
                            break

                    if successful_loop_count == len(scores_input_list): #if no errors were encountered during the score addition loop
                        student_ids.append(new_id)
                        student_names.append(new_name)

                        student_grades[new_id] = new_grades
                        student_gpas[new_id] = calculate_gpa(new_grades)[2]
                        enrolled_courses.update(new_courses)

                        print("\n---New Student Added---")
                        print(f"{student_ids[student_ids.index(new_id)]:04d} || {student_names[student_names.index(new_name)]}")
                        print("Student's grades:", student_grades[new_id])
                        print(f"Student's GPA: {student_gpas[new_id]}\n{'-'*23}")
                        rearrange_student_ids()
                else:
                    print("[ERROR] Student ID already exists.")
            else:
                print("Invalid input (Must be 4 digit number).")

        elif user_input==2: #Option 2: Compute GPAs and Averages by Matthew M.
            if student_ids: #True if student_ids contains any items. this should never be False in our case.
                for sid in student_ids:
                    student_gpas[sid] = calculate_gpa(student_grades[sid])[2]
                    print(f"{sid:04d} || {calculate_gpa(student_grades[sid])[0]:04.1f} || {calculate_gpa(student_grades[sid])[1]} || {student_gpas[sid]}")
            else:
                print("[ERROR] no student IDs present in database.")

        elif user_input==3: #Option 3 Display Formatted Roster by Matthew M.

            border_character = input("Enter border character: ")
            if border_character=="":
                border_character="*"
            if len(border_character)>1:
                border_character="*"

            status_to_target = input("\nSelect status to filter students by:\n1. All Students\n2. Dean's list\n3. Good Standing\n4. Probation Risk\nChoose: ").strip()
            filtered_list = []

            if status_to_target.isdigit() and int(status_to_target) in range(1,5): #only executes if its one of the allowed choices
                status_to_target = int(status_to_target)

                #this block gets our filtered list of students
                if status_to_target==1:
                    filtered_list = student_ids
                elif status_to_target==2:
                    filtered_list = filter_students_by_status(student_ids, student_gpas, "Dean's List")
                    print(filtered_list)
                elif status_to_target==3:
                    filtered_list = filter_students_by_status(student_ids, student_gpas, "Good Standing")
                    print(filtered_list)
                elif status_to_target==4:
                    filtered_list = filter_students_by_status(student_ids, student_gpas, "Probation Risk")
                    print(filtered_list)
                #this block gets our filtered list of students

                list_of_student_tuples = []
                for sid in filtered_list: #for every sid (1000, 1001, etc.) in filtered list, create a tuple out of their info.
                    tmp_tuple_name = student_names[student_ids.index(sid)]
                    tmp_tuple_gpa = student_gpas[sid]
                    tmp_tuple_status = evaluate_risk_standing(tmp_tuple_gpa)
                    list_of_student_tuples.append(tuple([sid, tmp_tuple_name, tmp_tuple_gpa, tmp_tuple_status]))
                    #packing all of this stuff into a tuple seems like extra to me, since its all globally accessible variables anyway.
                    #but i guess maybe its specifically to make the sorting feature easier. 


                sorting_order = input("\nSelect a sorting order:\n1. Sort by Student ID (Ascending)\n2. Sort by GPA(Descending)\n3. Sort by Name\nChoice: ")

                if sorting_order.isdigit() and int(sorting_order) in range(1,4):
                    sorting_order = int(sorting_order)

                    if sorting_order==1:
                        list_of_student_tuples = sorted(list_of_student_tuples, key =lambda st_tuple: st_tuple[0])
                        #apparently keys are functions, so we need to make a function to return a value. 
                        #lambda is like a temp function that can be defined to return a value.
                        #i learned this by searching it up because i thought wasting lines on individual functions for each key was messy and ugly
                    elif sorting_order==2:
                        list_of_student_tuples = sorted(list_of_student_tuples, key =lambda st_tuple: st_tuple[2], reverse=True)
                    elif sorting_order==3:
                        list_of_student_tuples = sorted(list_of_student_tuples, key =lambda st_tuple: st_tuple[1])

                    
                    print(f"\n{border_character*60}\n")
                    print(f"{'ID':<10}{'Name':<25}{'GPA':<10}{'Status':<15}")
                    print(f"\n{border_character*60}\n")

                    for st_tuple in list_of_student_tuples:
                        print(f"{f'{st_tuple[0]:04d}':<10}{st_tuple[1]:<25}{st_tuple[2]:<10}{st_tuple[3]:<15}")

                    print(f"\n{border_character * 60}")

                else:
                    print("[ERROR] Invalid choice")

            else:
                print("[ERROR] Invalid choice")


        elif user_input==4:

            Student_lookup = input("\nEnter Student ID or name Substring to search for: ").strip()
        

            if Student_lookup.isdigit() and int(Student_lookup) in student_ids and Student_lookup is not "": #match found for an ID
                Student_lookup = int(Student_lookup)
                qux = calculate_gpa(student_grades[Student_lookup])

                print(f"----{student_names[student_ids.index(Student_lookup)]}----")
                
                print(f"{"Student ID":<13}:{Student_lookup}")
                print(f"{"Scores":<13}:{student_grades[Student_lookup]}")
                print(f"{"Average":<13}:{qux[0]:.1f}")
                print(f"{"Letter Grade":<13}:{qux[1]}")
                print(f"{"GPA":<13}:{qux[2]:.1f}")
                print(f"{"Standing":<13}:{evaluate_risk_standing(qux[2])}")

                if qux[2] < 2.0:
                    print("[ALERT] Academic intervention is required.")
                elif qux[2]>= 3.5:
                    print("[Excellent] Honor roll recognition.")                
   
            elif any(Student_lookup.lower() in name.lower() for name in student_names) and Student_lookup is not "" and not Student_lookup.isdigit():  

                tmp_student_index = 0000 #default value just in case

                for name in student_names:
                    if Student_lookup.lower() in name.lower():
                        tmp_student_index = student_names.index(name)
                qux = calculate_gpa(student_grades[student_ids[tmp_student_index]])

                print(f"----{student_names[tmp_student_index]}----")
                
                print(f"{"Student ID":<13}:{student_ids[tmp_student_index]}")
                print(f"{"Scores":<13}:{student_grades[student_ids[tmp_student_index]]}")
                print(f"{"Average":<13}:{qux[0]:.1f}")
                print(f"{"Letter Grade":<13}:{qux[1]}")
                print(f"{"GPA":<13}:{qux[2]:.1f}")
                print(f"{"Standing":<13}:{evaluate_risk_standing(qux[2])}")

                if qux[2] < 2.0:
                    print("[ALERT] Academic intervention is required.")
                elif qux[2]>= 3.5:
                    print("[Excellent] Honor roll recognition.")

            else:
                print("No match was found")
            
                               


        elif user_input==5: #Option 5 by Macario Esparza
            dgas = generate_analytics_summary()
            print("\n<<<OPTION 5: Class Analytics & Score Metrics>>>\n")
            print(f"Total Individual Scores Recorded : {dgas['Count']}")
            print(f"Highest Individual Score : {dgas['Highest']:.1f}")
            print(f"Lowest Individual Score : {dgas['Lowest']:.1f}")
            print(f"Overall Class Score Average : {dgas['Average']:.1f}%")
            print("Enrolled System Courses:")
            course_counter = 0
            for course in enrolled_courses:
                course_counter += 1
                if course_counter != len(enrolled_courses):
                    print(f"{course}", end=", ")
                elif course_counter == len(enrolled_courses):
                    print(f"{course}")
                
            pass

    else:
        print(f"ERROR: {user_input} is not a valid input.")

    if application_isactive:
        input("\nPress Enter to continue: ")


#if we get here, presumably we have broken the main program loop
print("\nApplication Exited Successfully.")