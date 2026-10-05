students = {}

while True:
    print("\n===== STUDENT GRADE BOOK =====")
    print("1. Add student")
    print("2. Show class average")
    print("3. Show top student(s)")
    print("4. Show bottom scorer")
    print("5. Look up student grade")
    print("6. Show all students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        try:
            score = float(input("Enter student's score: "))

            if 0 <= score <= 100:
                students[name] = score
                print(f"{name} has been added with a score of {score}.")
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        if students:
            average = sum(students.values()) / len(students)
            print(f"Class Average: {average:.2f}")
        else:
            print("No student records available.")

    elif choice == "3":
        if students:
            highest_score = max(students.values())

            top_students = [
                name for name, score in students.items()
                if score == highest_score
            ]

            print(f"Top Score: {highest_score}")
            print("Top Student(s):")

            for name in top_students:
                print(f"- {name}")
        else:
            print("No student records available.")

    elif choice == "4":
        if students:
            lowest_score = min(students.values())

            bottom_students = [
                name for name, score in students.items()
                if score == lowest_score
            ]

            print(f"Lowest Score: {lowest_score}")
            print("Bottom Scorer(s):")

            for name in bottom_students:
                print(f"- {name}")
        else:
            print("No student records available.")

    elif choice == "5":
        name = input("Enter student name to look up: ")

        if name in students:
            print(f"{name}'s score: {students[name]}")
        else:
            print("Student not found.")
    elif choice == "6":
        if students:
            print('\nALL STUDENTS')
            for name,score in students.items():
                print(f"{name}:{score}")
        else:
            print("No student records available.")
    elif choice == "7":
        print("Thank you for using Student Grade Book!")
        break
    else:
        print("Invalid choice. Please try again.")

