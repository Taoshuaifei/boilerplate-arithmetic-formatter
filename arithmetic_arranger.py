def arithmetic_arranger(problems,key_switch = False):
    error_string = ''
    if len(problems) > 5:
        error_string = 'Error: Too many problems.'
        return error_string 
    arranged_problems = ''
    result_1 = ''
    result_2 = ''
    result_3 = ''
    result_4 = ''
    try:
        for temp in problems:
            front_part,op,back_part = temp.split()
            front_part,op,back_part = str(front_part),str(op),str(back_part)
            if op != '+' and op != '-':
                error_string = "Error: Operator must be '+' or '-'."
                break
            if front_part.isdigit() == False or back_part.isdigit() == False:
                error_string = "Error: Numbers must only contain digits."
                break
            if len(front_part) > 4 or len(back_part) > 4:
                error_string = "Error: Numbers cannot be more than four digits."
                break
            temp = temp.replace(' ','')
            front_length = len(front_part)
            back_length = len(back_part)
            longest = [front_length,back_length][front_length<back_length]
            result_1 = result_1 + (str('%' + str(longest+2) + 's') % front_part) + ' '*4
            result_2 = result_2 + (str(op + '%' + str(longest+1) + 's') % back_part) + ' '*4
            result_3 = result_3 + '-'*(longest+2) + ' '*4
            result_4 = result_4 + (str('%' + str(longest+2) + 's') % str(eval(temp))) + ' '*4
        if key_switch == True:
            arranged_problems = result_1.rstrip() + '\n' + result_2.rstrip() + '\n' + result_3.rstrip() + '\n' + result_4.rstrip()
        else:
            arranged_problems = result_1.rstrip() + '\n' + result_2.rstrip() + '\n' + result_3.rstrip()
    except Exception as e:
        return str(e)
    else:
        if error_string == '':
            return arranged_problems
        else:
            return error_string
