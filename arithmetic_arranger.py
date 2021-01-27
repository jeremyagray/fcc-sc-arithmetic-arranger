def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    lines = [[], [], [], []]

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

        lines[0].append("  " + str(one).rjust(length, " "))
        lines[1].append(op + " " + str(two).rjust(length, " "))
        lines[2].append("-".rjust(length + 2, "-"))
        lines[3].append(str(ans).rjust(length + 2, " "))

    if answers:
        num = 4
    else:
        num = 3

    return "\n".join(map(lambda line: "    ".join(line), lines[0:num]))
