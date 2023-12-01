def deleteWhiteSpace(message) -> str:
    return message.replace(" ", "")


def isExpression(message) -> bool:
    for i in message:
        if i not in '1234567890+-*/()':
            return False
    else:
        return True


def IsBracketsOkey(message) -> bool:
    lst = []
    for char in message:
        if char == '(':
            lst.append(char)
        elif char == ")":
            if len(lst) > 0 and lst[-1] == "(":
                lst.pop(-1)
            else:
                return False
    else:
        return not(len(lst))


def sumDiff(expression) -> str:

    if '+' not in expression and '-' not in expression:
        return expression
    
    result = 0
    lastInd = 0

    for idx, char in enumerate(expression):
        if char in '+-' and idx != 0:
            result += float(expression[lastInd:idx])
            lastInd = idx
            
    result += float(expression[lastInd:])
 
    return str(result)


def powDiv(expression) -> str:

    if '*' not in expression and '/' not in expression:
        return sumDiff(expression)
    
    for ind, char in enumerate(expression):
        if char in '*/':
            index = ind
            break

    leftIndex = -1
    rightIndex = len(expression)

    for lfInd in range(index - 1, 0, -1):
        if expression[lfInd] in "+-*/":
            leftIndex = lfInd
            break
                
    for rgInd in range(index + 1, len(expression)):
        if expression[rgInd] in "+-*/":
            rightIndex = rgInd
            break

    lValue = float(expression[leftIndex + 1:index])
    rValue = float(expression[index + 1:rightIndex])

    if expression[index] == "*":
        mn = lValue * rValue
    else:
        if rValue == 0:
            return 'Error'
        else:
            mn = lValue / rValue

    expression = expression[0:leftIndex + 1] + str(mn) + expression[rightIndex:]

    return powDiv(expression)


def raiseToDegree(expression) -> str:
    
    if '^' not in expression:
        return powDiv(expression)

    for ind, char in enumerate(expression):
        if char in '^':
            index = ind
            break

    leftIndex = -1
    rightIndex = len(expression)

    for lfInd in range(index - 1, 0, -1):
        if expression[lfInd] in "+-*/":
            leftIndex = lfInd
            break
                
    for rgInd in range(index + 1, len(expression)):
        if expression[rgInd] in "+-*/^":
            rightIndex = rgInd
            break

    lValue = float(expression[leftIndex + 1:index])
    rValue = float(expression[index + 1:rightIndex])

    mn = lValue ** rValue

    expression = expression[0:leftIndex + 1] + str(mn) + expression[rightIndex:]

    return raiseToDegree(expression)
    

def factorial(expression) -> str:

    if '!' not in expression:
        return raiseToDegree(expression)

    for ind, char in enumerate(expression):
        if char == '!':
            index = ind
            break

    leftIndex = -1

    for lfInd in range(index - 1, 0, -1):
        if expression[lfInd] in "+-*/^":
            leftIndex = lfInd
            break

    if '.' in expression[leftIndex + 1:index]:
        return "Error"

    lValue = int(expression[leftIndex + 1:index])

    mn = 1
    for i in range(1, lValue + 1):
        mn *= i 
    
    expression = expression[0:leftIndex + 1] + str(mn) + expression[index + 1:]

    return factorial(expression)   


def brackets(expression) -> str:

    if '(' not in expression:
        return factorial(expression)
    
    leftIndex = 0
    rightIndex = 0

    for idx, char in enumerate(expression):
        if char == '(':
            leftIndex = idx
        elif char == ')':
            rightIndex = idx
            break

    expression = expression[0:leftIndex] + factorial(expression[leftIndex + 1: rightIndex]) + expression[rightIndex + 1:]

    return brackets(expression) 


def calculate(expression):
    return brackets(expression)


print(calculate("(69*(-1)^10)^3+9000-9!"))