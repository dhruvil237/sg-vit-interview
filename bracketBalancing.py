def bracketBalancing(s):
    stack = []
    openBrackets = ["[","{","("]
    closingBrackets = ["]", "}", ")"]
    for i in s:
        if i in openBrackets:
            stack.append(i)
        elif i=="]" and stack[-1] == "[":
            stack.pop()
        elif i=="}" and stack[-1] == "{":
            stack.pop()
        elif i==")" and stack[-1] == "(":
            stack.pop()
        elif i in closingBrackets:
            return False
    if not stack:
        return True
    return False
str1 = input()
print(bracketBalancing(str1))
