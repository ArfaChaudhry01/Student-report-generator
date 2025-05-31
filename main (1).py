# Project 3: Student Report Card Generator

students = {}

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def add_student():
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()

    try:
        roll = int(roll)
    except ValueError:
        print("❌ Roll number must be a number.")
        return

    marks = []
    print("Enter marks for 5 subjects:")
    for i in range(5):
        try:
            mark = int(input(f"Subject {i+1}: "))
            if mark < 0 or mark > 100:
                print("❌ Marks must be between 0 and 100.")
                return
            marks.append(mark)
        except ValueError:
            print("❌ Invalid input. Please enter numeric marks.")
            return

    students[name] = {
        "roll": roll,
        "marks": marks
    }
    print(f"✅ Student {name} added successfully.")


def view_report_card():
    if not students:
        print("📭 No student records available.")
        return

    for name, details in students.items():
        marks = details["marks"]
        total = sum(marks)
        average = total / len(marks)
        grade = calculate_grade(average)

        print("\n📝 Report Card")
        print("--------------------------")
        print(f"Student Name: {name}")
        print(f"Roll No: {details['roll']}")
        print(f"Marks: {marks}")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
        print("--------------------------")


def main():
    print("📘 Welcome to the Student Report Card System")

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. View Report Cards")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_report_card()
        elif choice == "3":
            print("Exiting Report Card System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
