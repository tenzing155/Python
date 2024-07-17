# data = ['ram','sita','ram','hari','laxmi','laxmi']
# # data.pop(2)
# # data.pop(4)
# # data.remove('ram')
# # data.remove('laxmi')
# # print(data)
# data = list(dict.fromkeys(data))
# print(data)

students = [ 
    {'name':'ram', 'gender':'male','status':True},
    {'name':'sita', 'gender':'female', 'status':True},
    {'name':'hari', 'gender':'male','status':False},
    {'name':'laxmi', 'gender':'female', 'status':False},
    {'name':'gopal', 'gender' :'male', 'status':True},  
]
#total_users
#total_active_user
#total_inactive_user
#total_male
#total_female
#total_active_male
#total_active_female
#total_inactive_male
#total_inactive_female


total_users = len(students)
total_active_user = 0 
total_inactive_user = 0
total_male = 0
total_female = 0
total_active_male = 0
total_active_female = 0
total_inactive_male = 0
total_inactive_female = 0

for student in students:
    if student['status'] == True:
        total_active_user += 1
    else:
        total_inactive_user += 1
    if student['gender'] == 'male':
        total_male += 1
    else:
        total_female += 1
    if student['status'] == True and student['gender'] == 'male':
        total_active_male += 1
    else:
        total_inactive_female +=1
    if student['status'] == False and student['gender'] == 'male':
        total_inactive_male += 1
    else:
        total_inactive_female +=1
    if student['status'] == False and student['gender'] == "female":
        total_active_female += 1
    else:
        total_inactive_female +=1

print("Total users: ",total_users)
print("Total active users: ",total_active_user)
print("Total inactive users: ",total_inactive_user)
print("Total male users: ",total_male)
print("Total female users: ",total_female)
print("Total active male: ",total_active_male)
print("Total active female: ",total_active_female)
print("Total inactive male: ",total_inactive_male)
print("Total inactive female: ",total_inactive_female)





