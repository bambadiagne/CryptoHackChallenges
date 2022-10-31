students=[{"name":"Moussa","classe":"Tle","moyenne":15},{"name":"Fatou","classe":"Tle","moyenne":18},{"name":"Sidy","classe":"Tle","moyenne":14},{"name":"Astou","classe":"Tle","moyenne":12}]
average_mark=0
for student in students:
    print(f"{ student['name'] } {student['moyenne']}")
    average_mark+=student['moyenne']
print(f"Moyenne generale {average_mark//len(students)}")      