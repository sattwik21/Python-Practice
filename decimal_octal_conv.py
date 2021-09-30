def decimal_octal_conv(number_input):

    '''
    KeyWord:
    number_input : Giving a certain decimal number to be convert
    n_base : N base number you want to convert
    '''
    result = []
    while True:
        divide = number_input//8
        mod = number_input % 8
        number_input = divide
        result.append(mod)
        if number_input == 0:
            result = result[::-1]
            result = [str(i) for i in result]
            result = ''.join(result)
            break

    return result


