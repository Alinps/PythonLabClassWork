attendance = [18,20,19,15,21]

full_days = 0

total_attendance = 0

for student in attendance:
    total_attendance +=student
    if student>20:
        full_days +=1
        print("Full")
    else:
        print("Not full")
        
print("number of full days: ",full_days)
print("total attendance for 5 days:",total_attendance)