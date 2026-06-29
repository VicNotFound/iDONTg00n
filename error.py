def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score < 60:
        return "F"

students = {}
print("Student Grade Manager")
while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Calculate Class Average")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grades_input = input("Enter grades separated by spaces: ")
        grades_list = grades_input.split()
        for i in range(len(grades_list)):
            grades_list[i] = int(grades_list[i])
        students[name] = grades_list
        print(f"Added {name} with grades {grades_list}")

    elif choice == "2":
        if not students:
            print("No students found")
        else:
            for name, grades in students:
                avg = calculate_average(grades)
                letter = assign_letter_grade(avg)
                print(f"{name}: {grades} - Average: {avg:.1f} - Grade: {letter}")

    elif choice == "3":
        if not students:
            print("No students to calculate")
        else:
            all_grades = []
            for grades in students.values():
                all_grades.extend(grades)
            class_avg = calculate_average(all_grades)
            print(f"Class Average: {class_avg:.1f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")