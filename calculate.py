def sumDiff(expression, result = 0) -> float:
    if expression == 'Error':
        return 'Error'

    if '+' not in expression and '-' not in expression:
        return float(expression)
    
    lastInd = 0

    for idx, char in enumerate(expression):
        if char in '+-' and idx != 0:
            result += float(expression[lastInd:idx])
            print(f"Srt: {expression[lastInd:idx]}")
            lastInd = idx
            
    result += float(expression[lastInd:])
 
    return result

    