# codesignal level3 n4 - sort low to high humans ignoring trees
def reverseInParentheses(inputString):
    if inputString == "()":
        return ""
    new = []
    tmp = []
    left = []
    right = []
    if "(" in inputString:
        left_i = inputString.index("(")
        right_i = inputString.index(")")
        # right_i = right_i + 1
        tmp = inputString[left_i:right_i+1]
        left = inputString[:left_i]
        right = inputString[right_i+1:]
        print("parts: ",left,tmp,right)
        if "(" in left: # and "((" not in left and "))" not in left:
            left = reverseInParentheses(left)
        elif "(" in right: # and "((" not in right and "))" not in right:
            right = reverseInParentheses(right)
        tmp = invert(tmp)
        # combine final string
        new = left + tmp + right
        return new
    else:
        return inputString
def invert(tmp):
    # remove parentheses
    tmp = tmp[1:-1]
    # invert string
    return tmp[::-1]

# tests
print('inverted: ',reverseInParentheses("foo(bar)baz"))
print('inverted: ',reverseInParentheses("foo(bar)baz(blim)"))
print('inverted: ',reverseInParentheses("foo(bar(baz))blim"))
