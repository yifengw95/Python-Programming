input_name = input('please enter the file name')
fhandle = open(input_name)
output = dict()
for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split(' ')
        output[words[2]] = output.get(words[2],0) + 1
print(output)