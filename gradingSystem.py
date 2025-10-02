class StudentGradingSystem:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        """Add a valid grade to the list."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        elif grade != -1:
            print(f"Invalid grade {grade}! Ignored.")

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def point_grade(self, avg):
        return round(((100 - avg) + 10) / 10, 2)

    def remarks(self, avg):
        if avg < 50:
            return "Dropped"
        elif avg < 75:
            return "Failed"
        elif avg <= 79:
            return "Passed – Satisfactory"
        elif avg <= 84:
            return "Passed – Good"
        elif avg <= 89:
            return "Passed – Average"
        elif avg <= 99:
            return "Passed – Very Good"
        else:
            return "Passed – Excellent"

    def evaluate(self):
        if not self.grades:
            return "No valid grades entered!"

        avg = round(self.average_grade(), 2)
        point = self.point_grade(avg)
        remark = self.remarks(avg)

        print("\n--- STUDENT GRADING RESULT ---")
        print("Grades Entered:", self.grades)
        print(f"Average Grade: {avg}")
        print(f"Point Grade: {point}")
        print(f"Remarks: {remark}")


# ---- Main Program ----
def main():
    system = StudentGradingSystem()
    print("Enter grades (0–100). Enter -1 to finish:")

    while True:
        try:
            grade = int(input("Enter grade: "))
            if grade == -1:
                break
            system.add_grade(grade)
        except ValueError:
            print("Invalid input. Please enter a number.")

    system.evaluate()


if __name__ == "__main__":
    main()
