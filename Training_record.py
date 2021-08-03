from Function import Volume
#매일 운동 기록
print("============운동일지입니다============")
set=int(input())
event = ['Bench_press','Pull_up','Incline_bench','BB_row','Push_up','One_arm_dumble_row']
for i in range(set):
    Bench_press, reps= map(int,input("Bench_press %d Set : " % (i+1)).split())
for i in range(set):
    Pull_up, reps = map(int, input("Pull_up %d Set : " % (i + 1)).split())
for i in range(set):
    Incline_bench, reps = map(int, input("Incline_bench %d Set : " % (i + 1)).split())
for i in range(set):
    BB_row, reps = map(int, input("BB_row %d Set : " % (i + 1)).split())
for i in range(set):
    Push_up, reps = map(int, input("Push_up %d Set : " % (i + 1)).split())
for i in range(set):
    One_arm_dumble_row, reps = map(int, input("One_arm_dumble_row %d Set : " % (i + 1)).split())
for n in range(0,len(event)-1):
    for j in event:
        print(j[n],'Volumes :' ,Volume(set,reps,j[n]))
# print('Bench_press Volumes : %d kg' % (Volume(set,reps,Bench_press)))
# print('Pull_up Volumes : %d kg' % (Volume(set,reps,Pull_up)))
# print('Incline_bench Volumes : %d kg' % (Volume(set,reps,Incline_bench)))
# print('BB_row Volumes : %d kg' % (Volume(set,reps,BB_row)))
# print('Push_up Volumes : %d kg' % (Volume(set,reps,Push_up)))
# print('One_arm_dumble_row Volumes : %d kg' % (Volume(set,reps,One_arm_dumble_row)))



