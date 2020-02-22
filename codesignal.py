# codesignal level1 n2
def centuryFromYear(year):
    return (year - 1) // 100 + 1
# tests
print('century from hear 1905: ',centuryFromYear(1905)) # expected 20
print('century from hear 1700: ',centuryFromYear(1700)) # expected 17

#  codesignal level1 n3
def checkPalindrome(inputString):
    length = len(inputString)
    mid = length // 2
    return inputString[:mid-1:-1] == inputString[:mid] if length%2 == 0 else inputString[:mid] == inputString[:mid:-1]
# tests
print('checkPalindrome: "aabaa", expected True is: ',checkPalindrome("aabaa"))
print('checkPalindrome: "abac",  expected False is: ',checkPalindrome("abac"))
print('checkPalindrome: "a", expected True is: ',checkPalindrome("a"))
print('checkPalindrome: "abacaba", expected True is: ',checkPalindrome("abacaba"))

# codesignal level2 n1
def adjacentElementsProduct(inputArray):
    result = 0
    temp = 0
    for i in range(len(inputArray)):
        if i == 0:
            continue
        temp = inputArray[i-1] * inputArray[i]
        if result == 0:
            result = temp
        else :
            result = temp if temp > result else result
    return result
# tests
print('max of two multiplied members in list: [3, 6, -2, -5, 7, 3] is 21 = ',adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
print('max of two multiplied members in list: [5, 1, 2, 3, 1, 4] is 6 = ',adjacentElementsProduct([5, 1, 2, 3, 1, 4]))

# codesignal level2 n2 - polygon shape area calculator
def shapeArea(n):
    return (n * n) + ((n - 1) * (n - 1))
# tests
print('polygon area of 2 squares is 5 = ',shapeArea(2))
print('polygon area of 7000 squares is 97986001 = ',shapeArea(7000))

# codesignal level2 n3 - find missing numbers count if list becomes sorted
def makeArrayConsecutive2(statues):
    full = list( range( min(statues), max(statues) ) )
    result = []
    for i in range( 0, len(full) ):
        if full[i] not in statues:
            result.append( full[i] )
    return len( result )
# tests
print('missing numbers count in list [6, 2, 3, 8] is 3 = ',makeArrayConsecutive2([6, 2, 3, 8]))
print('missing numbers count in list [6, 2, 10, 3, 15, 8] is 8 = ',makeArrayConsecutive2([6, 2, 10, 3, 15, 8]))

# codesignal level2 n4 - is it possible to get increasing sequence by removing only 1 member
def almostIncreasingSequence(sequence):
    j = first_bad_pair(sequence)
    if j == -1:
        return True  # List is increasing
    if first_bad_pair(sequence[j - 1:j] + sequence[j + 1:]) == -1:
        return True  # Deleting earlier element makes increasing
    if first_bad_pair(sequence[j:j + 1] + sequence[j + 2:]) == -1:
        return True  # Deleting later element makes increasing
    return False
# additional function for l2 n2 - almostIncreasingSequence
def first_bad_pair(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return i
    return -1
# tests
print('almostIncreasingSequence of [1, 3, 2, 1] is false = ',almostIncreasingSequence([1, 3, 2, 1]))
print('almostIncreasingSequence of [123, -17, -5, 1, 2, 3, 12, 43, 45] is true = ',almostIncreasingSequence([123, -17, -5, 1, 2, 3, 12, 43, 45]))

# codesignal level2 n5 - matrix of ghosts
def matrixElementsSum(matrix):
    result = 0
    ignore = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0 and j not in ignore:
                result += matrix[i][j]
            elif matrix[i][j] == 0 and j not in ignore:
                ignore.append(j)
    return result
# tests
print('matrix of ghosts [[0,1,1,2],[0,5,0,0],[2,0,3,3]] sum is 9 = ',matrixElementsSum([[0,1,1,2],[0,5,0,0],[2,0,3,3]]))
print('matrix of ghosts [[4,0,1],[10,7,0],[0,0,0],[9,1,2]] sum is 15 = ',matrixElementsSum([[4,0,1],[10,7,0],[0,0,0],[9,1,2]]))

# codesignal level3 n1 - find longest string in list and how many have same length
def allLongestStrings(inputArray):
    result = []
    longest = max(inputArray, key=len)
    length = len(longest)
    for i in inputArray:
        if len(i) == length:
            result.append(i)
    return result
# tests
print('all longest strings of ["aba","aa","ad","vcd","aba"] is ["aba","vcd","aba"] = ',allLongestStrings(["aba","aa","ad","vcd","aba"]))
print('all longest strings of ["abc","eeee","abcd","dcd"] is ["eeee","abcd"] = ',allLongestStrings(["abc","eeee","abcd","dcd"]))

# codesignal level3 n2
def commonCharacterCount(s1, s2):
    result = 0
    ignore = []
    for i in s1:
        for j in range(len(s2)):
            if i == s2[j] and j not in ignore:
                ignore.append(j)
                result += 1
                break
    return result
# tests
print('commonCharacterCount of "aabcc" and "adcaa" is 3 = ',commonCharacterCount("aabcc","adcaa"))
print('commonCharacterCount of "zzzz" and "zzzzzzz" is 4 = ',commonCharacterCount("zzzz","zzzzzzz"))
print('commonCharacterCount of "abca" and "xyzbac" is 3 = ',commonCharacterCount("abca","xyzbac"))
