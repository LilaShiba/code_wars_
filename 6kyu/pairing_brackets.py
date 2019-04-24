def bracket_pairs(string):
    # return a dictionary with open/close position pairs
    if string.count('(') != string.count(')'):
        return False
    ans = dict()
    stack = []
    i = 0
    while i < len(string):
        if string[i] == '(':
            stack.append(i)
        if string[i] == ')':
            if len(stack) == 0:
                return False
            else:
                ans[stack[-1]] = i
                del stack[-1]
        i += 1
    return ans
