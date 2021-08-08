import datetime
days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
a = datetime.datetime.today().weekday()
print(days[a])


def Volume(set,reps,weight):
    if weight == 0:
        volume = (set * reps)
    else:
        volume = (set * reps * weight)
    return volume
#변수
Upper_body_day = ['Bench_press','Pull_up','Incline_bench','BB_row','Push_up','One_arm_dumble_row','Easy-bar_Curl','Cable_Curl']
Lower_body_day = ['squat','Dead_Lift','OHP','lunge','SaReRe','LyingTriceps','Triceps']

def VolumeCal(kind):
    weight = []
    reps = []
    if kind == '하체':
        for i in range(0,len(Lower_body_day)):
            set = input(Lower_body_day[i]+'세트 수 :')
            for k in range(int(set)):
                weight.append(int(input('Weight : ')))
                reps.append(int(input('Reps : ')))

                print(Lower_body_day[i],'set:',set,'weight:',weight[k],'kg','reps: ',reps[k],'kg')
    elif kind == '상체':
        for i in range(0,len(Upper_body_day)):
            set = input(Lower_body_day[i]+'세트 수 :')
            for _ in range(int(set)):
                weight,reps = map(int,input('무게 X 횟수:').split())

    else:
        print('~상/하체를 입력해주세요~')

