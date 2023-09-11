def isValid(s):
    stack=[]
    for i in range(len(s)):
        if (s[i]==')' or s[i]==']' or s[i]=='}' )and (len(stack)==0):
            return False
        if s[i]=='(' or s[i]=='{' or s[i] =='[':
            stack.append(s[i])
        if s[i]==')' and  stack[len(stack)-1]=='(':
            stack.pop()
        elif s[i]==')' and stack[len(stack)-1]!='(':
            return False
        elif s[i]==']' and stack[len(stack)-1]=='[':
            stack.pop()
        elif s[i]==']' and stack[len(stack)-1]!='[':
             return False
        elif s[i]=='}' and stack[len(stack)-1]=='{':
            
            stack.pop()
        elif s[i]=='}' and stack[len(stack)-1]!='{':
            return False
    if len(stack)>0:
        return False
    else:
        return True


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("("))
# print(isValid("("))
print(isValid("]"))
# print(isValid("()"))