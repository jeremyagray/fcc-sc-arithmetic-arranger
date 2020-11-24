import re


def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    pline_one = ''
    pline_two = ''
    pline_bars = ''
    pline_ans = ''
    for index, problem in enumerate(problems):
        # Split the problem.
        [one, op, two] = problem.split()

        # Add/subtract only.
        if not (op == '+' or op == '-'):
            return "Error: Operator must be '+' or '-'."

        # Only digits.
        if (re.search(r"\D", one) or re.search(r"\D", two)):
            return "Error: Numbers must only contain digits."

        # Four digits only.
        if (len(one) > 4 or len(two) > 4):
            return "Error: Numbers cannot be more than four digits."

        one_length = len(one)
        two_length = len(two)
        if one_length > two_length:
            length = one_length
        else:
            length = two_length

        pline_one += '  ' + str(one).rjust(length, ' ')
        pline_two += op + ' ' + str(two).rjust(length, ' ')
        pline_bars += '-'.rjust(length + 2, '-')
        if (op == '+'):
            ans = int(one) + int(two)
        else:
            ans = int(one) - int(two)
        pline_ans += str(ans).rjust(length + 2, ' ')

        if ((index + 1) < len(problems)):
            pline_one += '    '
            pline_two += '    '
            pline_bars += '    '
            pline_ans += '    '

    if answers:
        arranged_problems = (pline_one + '\n' + pline_two
                             + '\n' + pline_bars + '\n' + pline_ans)
    else:
        arranged_problems = pline_one + '\n' + pline_two + '\n' + pline_bars

    return arranged_problems
