def count (input_string, input_letter):
    output = 0 
    for letter in input_string:
        if letter == input_letter:
            output = output + 1
    return output