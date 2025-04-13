numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)
name = "Angela"
letter_list = [letter for letter in name]
print(letter_list)
range_list = [x * 2 for x in range(1, 5)]
print(range_list)
names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]
short_names = [short_name for short_name in names if len(short_name) < 5]
print(short_names)
long_names = [long_name.upper() for long_name in names if len(long_name) > 5]
print(long_names)
new_numbers = [2, 4, 6, 7, 2, 3, 1]
else_list = ["true" if num < 5 else "false" for num in new_numbers]
new_else_list = ["true" if num < 5 else "false" for num in range(1, 8)]
print(else_list)
print(new_else_list)
import random
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score > 50}
print(passed_students)
print("-------------------------")
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 92]
}
for (key, value) in student_dict.items():
    print(value)
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print("---------------------")
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student)
    print(row.score)
    print("----------------------------")
new_dict = {index: row for (index, row) in student_data_frame.iterrows()}
print(new_dict)