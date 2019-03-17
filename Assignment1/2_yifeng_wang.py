def computegrade (number_input):
    try:
        score = float(number_input)
        if (score < 0) or (score > 1):
            print('Bad score')
        else:
            if score >= 0.9:
                return('A')
            elif score >= 0.8:
                return('B')
            elif score >= 0.7:
                return('C')
            elif score >= 0.6:
                return('D')
            else:
                return('F')
    except:
        print('Bad score')