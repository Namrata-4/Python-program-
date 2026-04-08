#MAP

# marks=[67,98,20,79,80,56]
# def grade(marks):
#     if marks>=90:
#         return 'A'
#     elif 80<=marks<90:
#         return 'B'
#     elif 70<=marks<80:
#         return 'C'
#     elif 60<=marks<70:
#         return 'D'
#     else:
#         return 'F'
# grades=list(map(grade,marks))
# print("exam scores: ",marks)
# print("Grades: ",grades)

#FILTER 

marks=[67,98,20,79,80,56]
def failing (score):
    return score<60
result=filter(failing,marks)
print("failing scores :",list(result))
