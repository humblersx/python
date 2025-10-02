# List Comprehension
# add 1 to each number in list
old_list = [1, 2, 3]
new_list = [n + 1 for n in old_list]
print(new_list)

# takes string and puts each character into list
name = "Joe"
new_list = [letter for letter in name]
print(new_list)

# double each item in range
new_range = [2 * item for item in range(1,5)]
print(new_range)


# Conditional List Comprehension
names = ["Joe", "John", "Matthew", "Mark", "Paul"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# CAPS LOCK all names in list
all_caps = [name.upper() for name in names if len(name) > 4]
print(all_caps)

# int the strings and print evens
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']

numbers = [int(number) for number in list_of_strings]

result = [number for number in numbers if number % 2 == 0]

print(result)

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
names = ["Joe", "John", "Matthew", "Mark", "Paul"]
import random
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score > 70}
print(passed_students)
