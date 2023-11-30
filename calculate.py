def deleteWhiteSpace(message) -> str:
    return message.replace(" ", "")


def isExpression(message) -> bool:
    for i in message:
        if i not in '1234567890+-*/':
            return False
    else:
        return True


def IsBracketsOkey(message) -> bool:
    lst = []
    for char in message:
        if char in "({[":
            lst.append(char)
        elif char == ")":
            if len(lst) > 0 and lst[-1] == "(":
                lst.pop(-1)
            else:
                return False
        elif char == "}":
            if len(lst) > 0 and lst[-1] == "{":
                lst.pop(-1)
            else:
                return False
        elif char == "]":
            if len(lst) > 0 and lst[-1] == "[":
                lst.pop(-1)
            else:
                return False
    else:
        if len(lst) == 0:
            return True
        else:
            return False


def sumDiff(expression, result = 0) -> str:

    if '+' not in expression and '-' not in expression:
        return expression
    
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


def calculate(expression):
    return powDiv(expression)
