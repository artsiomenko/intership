operators = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: 0 if y == 0 else x / y)}


def parse(formula_string):
    number = ''
    formula = []
    for s in formula_string:
        if s.isdigit():
            number += s
        elif number:
            formula.append(float(number))
            number = ''
        if s in operators or s in "()":
            formula.append(s)
    if number:
        formula.append(float(number))
    return formula


def sorting(parsed_formula):
    stack = []
    sort_formula = []
    for i in parsed_formula:
        if i in operators:
            while stack and stack[-1] != "(" and operators[i][0] <= operators[stack[-1]][0]:
                sort_formula.append(stack.pop())
            stack.append(i)
        elif i == ")":
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                sort_formula.append(x)
        elif i == "(":
            stack.append(i)
        else:
            sort_formula.append(i)
    while stack:
        sort_formula.append(stack.pop())
    return sort_formula


def calculation(sort_formula):
    stack = []
    for elem in sort_formula:
        if elem in operators:
            y, x = stack.pop(), stack.pop()
            stack.append(operators[elem][1](x, y))
        else:
            stack.append(elem)
    return stack[0]


def check_calculation(text):
    if '(' in text or ')' in text:
        counter = 0
        for s in text:
            if s == '(':
                counter += 1
            if s == ')':
                counter -= 1
            if counter < 0:
                return False
        if counter != 0: return False
    return calculation(sorting(parse(text)))


print(check_calculation('1+1'))
print(check_calculation('1+1+(2/1)+3'))
print(check_calculation(')(1+1+(2/1)+3'))

