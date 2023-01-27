time = list(map(int,input().split()))
hr = 0
if time[1] == 45 :
    print(time[0],'0')

elif time[1] > 45 :
    min = time[1]-45
    print(time[0],min)
elif time[1] < 45: 
    if time[0] == 0:
        hr == 23
        min = time[1] +15
        print("23",min)
    else :
        min = time[1] +15
        print((time[0]-1),min)
