str = 'X-DSPAM-Confidence: 0.8475'
num_index  = str.find(':')
num = str[num_index+1:]
num = float(num)