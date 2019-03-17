input_name = input('please enter the file name')
fhandle = open(input_name)
output = dict()
for line in fhandle:
    if line.startswith('From:'):
        line = line.rstrip()
        words = line.split(' ')
        output[words[1]] = output.get(words[1],0) + 1
max_num = 0
for (index, content) in output.items():
    if content > max_num:
        output_index = index
        output_content = content
        max_num = content
print(output_index, output_content)