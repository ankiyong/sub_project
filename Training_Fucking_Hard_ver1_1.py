from Function import Volume
from datetime import datetime

#변수
Upper_body_day = ['Bench_press','Pull_up','Incline_bench','BB_row','Push_up','One_arm_dumble_row','Easy-bar_Curl','Cable_Curl']
Lower_body_day = ['squat','Dead_Lift','OHP','lunge','SaReRe','LyingTriceps','Triceps']
kind  = input()
#매일 운동 기록
print("============운동일지입니다============")
print('오늘은 %d년 %d월 %d일입니다.' % (datetime.today().year,datetime.today().month,datetime.today().day))
print('오늘은 ',kind,' Day!')
set1=input('벤치프레스 세트 수 : ')
event = ['Bench_press','Pull_up','Incline_bench','BB_row','Push_up','One_arm_dumble_row']
for i in range(int(set1)):
    Bench_press, reps= map(int,input("Bench_press %d Set : " % (i+1)).split())
set2=input('풀업 세트 수 : ')
for i in range(int(set2)):
    Pull_up, reps = map(int, input("Pull_up %d Set : " % (i + 1)).split())
set3=input('인클라인 벤치 프레스 세트 수 : ')
for i in range(int(set3)):
    Incline_bench, reps = map(int, input("Incline_bench %d Set : " % (i + 1)).split())
set4=input('바벨 로우 세트 수 : ')
for i in range(int(set4)):
    BB_row, reps = map(int, input("BB_row %d Set : " % (i + 1)).split())
set5=input('푸쉬 업 세트 수 : ')
for i in range(int(set5)):
    Push_up, reps = map(int, input("Push_up %d Set : " % (i + 1)).split())
set6=input('원 암 덤벨 로우 세트 수: ')
for i in range(int(set6)):
    One_arm_dumble_row, reps = map(int, input("One_arm_dumble_row %d Set : " % (i + 1)).split())
print('Bench_press Volumes : %d kg' % (Volume(set1,reps,Bench_press)))
print('Pull_up Volumes : %d kg' % (Volume(set2,reps,Pull_up)))
print('Incline_bench Volumes : %d kg' % (Volume(set3,reps,Incline_bench)))
print('BB_row Volumes : %d kg' % (Volume(set4,reps,BB_row)))
print('Push_up Volumes : %d kg' % (Volume(set5,reps,Push_up)))
print('One_arm_dumble_row Volumes : %d kg' % (Volume(set6,reps,One_arm_dumble_row)))



