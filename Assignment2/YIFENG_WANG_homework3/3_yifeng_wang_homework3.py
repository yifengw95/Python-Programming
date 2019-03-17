input_name = input('please enter the file name')
fhandle = open(input_name)
output = dict()
for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split(' ')
        times = words[6]
        time = times.split(':')
        hour = time[0]
        output[hour] = output.get(hour,0) + 1
        
output = sorted(output.items())
for key, value in output:
    print(key, value)