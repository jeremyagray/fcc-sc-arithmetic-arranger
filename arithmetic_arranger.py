def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line_one = ""
    line_two = ""
    line_bars = ""
    line_ans = ""

    for index, problem in enumerate(problems):
        # Split the problem.
        [one, op, two] = problem.split()

        # Add/subtract only.
        if not (op == "+" or op == "-"):
            return "Error: Operator must be '+' or '-'."

        # Only digits.
        if not (one.isdigit() and two.isdigit()):
            return "Error: Numbers must only contain digits."

        # Four digits only.
        if len(one) > 4 or len(two) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(one), len(two))

        if op == "+":
            ans = int(one) + int(two)
        elif op == "-":
            ans = int(one) - int(two)

        line_one += "  " + str(one).rjust(length, " ")
        line_two += op + " " + str(two).rjust(length, " ")
        line_bars += "-".rjust(length + 2, "-")
        line_ans += str(ans).rjust(length + 2, " ")

        if (index + 1) < len(problems):
            line_one += "    "
            line_two += "    "
            line_bars += "    "
            line_ans += "    "

    if answers:
        arranged_problems = (
            line_one + "\n" + line_two + "\n" + line_bars + "\n" + line_ans
        )
    else:
        arranged_problems = line_one + "\n" + line_two + "\n" + line_bars

    return arranged_problems
