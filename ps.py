import sys
def func(str):
    stack = []
    for i in range(0, len(str)):
        if str[i] == '(' or str[i] == '[':
            stack.append(str[i])
        elif str[i] == ')':
            if not stack or stack.pop() != '(':
                return False
        elif str[i]==']':
            if not stack or stack.pop() != '[':
                return False
    return True

while True:

    s = input()
    print(s)
    if s =='.':
        break

    if func(s) == True:
        print("yes")
    else:
        print("no")



