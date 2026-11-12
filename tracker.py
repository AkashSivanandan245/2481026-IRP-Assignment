"""
Placement Readiness Tracker
Industry Readiness Programme-II (CSE2596) - Assignment
Name: Akash Sivanandan, URN: 2481026

Records students' practice-test scores (aptitude, verbal, coding).
"""

SUBJECTS = ["aptitude", "verbal", "coding"]

students = [
    {"name": "Akash Sivanandan", "roll_no": "2481026", "aptitude": 95, "verbal": 88, "coding": 99},
    {"name": "Dhananjay Kumar", "roll_no": "2481033", "aptitude": 82, "verbal": 72, "coding": 90},
    {"name": "Girish Khanna", "roll_no": "2481150", "aptitude": 85, "verbal": 80, "coding": 87},
    {"name": "Soumen Kumar Dutta", "roll_no": "2481248", "aptitude": 91, "verbal": 85, "coding": 87},
    {"name": "Pulkit", "roll_no": "2481135", "aptitude": 77, "verbal": 92, "coding": 88}
]

def read_score(subject):
    while True:
        try:
            score = int(input(subject + " score: "))
            if 0 <= score <= 100:
                return score
        except:
            pass
        print("Enter a number between 0 and 100")

def add_student():
    student = {
        "name": input("Name: "),
        "roll_no": input("Roll Number: ")
    }

    for subject in SUBJECTS:
        student[subject] = read_score(subject)

    students.append(student)

def average(student):
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3


def main():
    add_student()
  
if __name__ == "__main__":
    main()