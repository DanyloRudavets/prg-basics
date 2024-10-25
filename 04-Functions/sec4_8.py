def time_string(hours, minutes, time_format):
    if time_format==12:
        if int(hours)==12:
            print(f'{12}+{minutes}+pm')
        elif int(hours)==0:
            print(f'{12}+{minutes}+am')
        if int(hours)<12 and int(hours)!=0:
            print(f'{str(hours)}+{minutes}+am')
        elif int(hours)>12:
            for i in range(1,13):
                if int(hours)-i==12:
                    print(f'{str(i)},{minutes},pm')
    elif time_format==24:
        print(f'{str(hours)}+{minutes}+')
    
time_string(4,24,12)