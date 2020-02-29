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
        tmp = inputString[left_i:right_i+1]
        left = inputString[:left_i]
        right = inputString[right_i+1:]
        print("------------------\nparts: ",left,tmp,right)
        if "(" in left: # and "((" not in left and "))" not in left:
            left = reverseInParentheses(left)
            tmp = invert(tmp)
        elif "(" in right: # and "((" not in right and "))" not in right:
            right = reverseInParentheses(right)
            tmp = invert(tmp)
        elif "(" in tmp[1:-1]:
            # print('------------------\nfound () in tmp', tmp)
            min_tmp = tmp[1:-1]
            # print('=====\nmin_tmp', min_tmp)
            some = min_tmp[:min_tmp.index("(")]
            # print('=====\nsome', some)
            inverted = some[::-1]
            # print('=====\ninverted', inverted)
            tmp = inverted + min_tmp[min_tmp.index("("):]
            # print('=====\ntmp', tmp)
            # tmp = reverseInParentheses(tmp[1:-1])
        # tmp = invert(tmp)
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

# tests "(bar)"
print('------------------\ninverted: ',reverseInParentheses("(bar)")) # expected "rab"
print('------------------\ninverted: ',reverseInParentheses("foo(bar)baz")) # expected "foorabbaz"
print('------------------\ninverted: ',reverseInParentheses("foo(bar)baz(blim)")) # expected "foorabbazmilb"
print('------------------\ninverted: ',reverseInParentheses("foo(bar(baz))blim"))  # expected "foobazrabblim"
