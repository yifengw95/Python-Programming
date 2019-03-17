flag = True
while(flag):
    input_meters = input('enter the distance in meters')
    try:
        meters = float(input_meters)
        feet = meters * 3.281
        print('the distance in feet is {number}'.format(number = feet))
        flag = False
    except:
        print('the input is invalid, please try it again')