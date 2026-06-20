students = []

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = int(input("Enter marks (out of 100): "))

        students.append((name, roll, marks))
        print("Student added successfully 😊")

    elif choice == "2":
        print("\n--- STUDENT RESULTS ---")
        if len(students) == 0:
            print("No students added yet 😅")
        else:
            for s in students:
                name, roll, marks = s

                percentage = (marks / 100) * 100

                if marks >= 40:
                    status = "Pass ✅"
                else:
                    status = "Fail ❌"

                print("Name:", name,
                      "| Roll:", roll,
                      "| Marks:", marks,
                      "| %:", percentage,
                      "| Status:", status)

    elif choice == "3":
        print("Exiting... 👋")
        break

    else:
        print("Invalid choice 😅")