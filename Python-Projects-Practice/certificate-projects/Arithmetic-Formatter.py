def arithmetic_arranger(problems, show_answers=False):
    line1_list = []
    line2_list = []
    line3_list = []
    line4_list = []

    # Verificar que no sean mas de 5 problemas
    length = len(problems)
    if length > 5 :
        return "Error: Too many problems."

    #Verificar que sea suma y resta solo
    divided_list = [s.split(' ') for s in problems]
    for problem in divided_list:
        operator = problem[1]
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

    #Verificar que los numeros no sean mas grande de 4 digitos
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not problem[0].isdigit() or not problem[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(problem[0]) > len(problem[2]):
            width = len(problem[0]) + 2
        else:
            width = len(problem[2]) + 2

        line1 = problem[0].rjust(width)
        line2 = problem[1] + ' ' + problem[2].rjust(width-2)
        line3 = "-"*width

        problem_list = [line1, line2, line3]


        if show_answers:
            if problem[1] == '+':
                result = int(problem[0]) + int(problem[2])
            else:
                result = int(problem[0]) - int(problem[2])
            result = str(result)
            line4 = result.rjust(width)
            line4_list.append(line4)


        line1_list.append(line1)
        line2_list.append(line2)
        line3_list.append(line3)

    top = "    ".join(line1_list)
    mid = "    ".join(line2_list)
    dash = "    ".join(line3_list)
    result = "    ".join(line4_list)

    if show_answers:
        final = top + "\n" + mid + "\n" + dash + "\n" + result
    else:
        final = top + "\n" + mid + "\n" + dash

    return final

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))