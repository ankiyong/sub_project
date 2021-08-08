from Function import Volume
from datetime import datetime
from Function import choose_day
from Function import VolumeCal
#변수
Upper_body_day = ['Bench_press','Pull_up','Incline_bench','BB_row','Push_up','One_arm_dumble_row','Easy-bar_Curl','Cable_Curl']
Lower_body_day = ['squat','Dead_Lift','OHP','lunge','SaReRe','LyingTriceps','Triceps']
excercise =input('운동부위 입력(상/하체) :')
# choose_day(excercise)

ToDayVolume = VolumeCal(excercise)
print(ToDayVolume)