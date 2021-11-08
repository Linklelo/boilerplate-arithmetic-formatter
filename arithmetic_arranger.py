def arithmetic_arranger(problems, calc=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    result_aray = []
    for problem in problems:
        prob_result = []
        left = problem.split()[0]
        opt = problem.split()[1].strip()
        right = problem.split()[2]
        if not(left.isdigit() and right.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(left) >= 5 or len(right) >= 5:
            return 'Error: Numbers cannot be more than four digits.'
        if opt != "+" and opt != "-":
            return "Error: Operator must be '+' or '-'."
        spc_len = max(len(left), len(right)) + 2
        prob_result.append(left.rjust(spc_len, " "))
        prob_result.append(opt + right.rjust(spc_len - 1, " "))
        prob_result.append(spc_len * "-")
        if calc == True:
            result = eval(problem)
            prob_result.append(str(result).rjust(spc_len, " "))
        result_aray.append(prob_result)

    return "\n".join(["    ".join(item[i] for item in result_aray) for i in range(4 if calc == True else 3)])
