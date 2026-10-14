def main():
    print("Welcome to the Student Data Organizer!")
    
    students = {}       
    
    all_subjects = set()    

    while True:
        print("\n--- Menu ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nEnter student details:")
            try:
                student_id = int(input("Student ID: "))
                name = input("Name: ")
                age = int(input("Age: "))
                grade = input("Grade: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                subjects_input = input("Subjects (comma-separated): ")

                
                subjects = [sub.strip() for sub in subjects_input.split(',')]
                
                
                all_subjects.update(subjects) 

            
                students[student_id] = {
                    'name': name,
                    'age': age,
                    'grade': grade,
                    'dob': dob,
                    'subjects': subjects
                }

                print("\nStudent added successfully!")
            except ValueError:
                print("Invalid input! Please ensure Student ID and Age are numbers.")

        elif choice == '2':
            print("\n--- All Students ---")
            if not students:
                print("No students to display.")
            else:
                
                for student_id, info in students.items():
                    subs = ", ".join(info['subjects'])
                    print(f"ID: {student_id} | Name: {info['name']} | Age: {info['age']} | Grade: {info['grade']} | Subjects: {subs}")

        elif choice == '3':
            try:
                student_id = int(input("Enter Student ID to update: "))
                if student_id in students:
                    print("1. Update Age")
                    print("2. Update Subjects")
                    update_choice = input("Select an option (1 or 2): ")
                    
                    if update_choice == '1':
                        new_age = int(input("Enter new age: "))
                        students[student_id]['age'] = new_age
                        print("Age updated successfully!")
                    
                    elif update_choice == '2':
                        new_subs_input = input("Enter new subjects (comma-separated): ")
                        new_subs = [sub.strip() for sub in new_subs_input.split(',')]
                        
                        students[student_id]['subjects'] = new_subs
                        all_subjects.update(new_subs) 
                        print("Subjects updated successfully!")
                    
                    else:
                        print("Invalid choice.")
                else:
                    print("Student ID not found.")
            except ValueError:
                print("Invalid Student ID format.")

        elif choice == '4':
            try:
                student_id = int(input("Enter Student ID to delete: "))
                if student_id in students:
                    
                    del students[student_id]
                    print("Student record deleted successfully!")
                else:
                    print("Student ID not found.")
            except ValueError:
                print("Invalid Student ID format.")

        elif choice == '5':
            print("\n--- Subjects Offered ---")
            if all_subjects:
                print(", ".join(all_subjects))
            else:
                print("No subjects have been added yet.")

        elif choice == '6':
            print("Thank you for using the Student Data Organizer!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 6.")

if __name__ == "__main__":
    main()
