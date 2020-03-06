def areSimilar(a, b):
    if a == b: return True 
    tmp = []
    match = []
    for i,v in enumerate(a):
        #for j,x in enumerate(b):
        print(f'v: {v}, x: {b[i]}, tmp length: {len(tmp)}')
        # when more than 2 elements values do not match 
        if len(tmp) > 2: return False #  result is false
        # when value of same index in both lists do not match
        if v != b[i]: tmp.append(b[i]) # remember the value that did not matched
        # if values match, remember index
        else: match.append(i)
    #check matched values have same indexes
    for x in match:
        print(f'matching values: {a[x]} = {b[x]}')
        if a[x] != b[x]: return False
    print(match)
    return False if match == [] else True
# tests
print('=========\n1) areSimilar is true =', areSimilar([2, 1, 3], [1, 2, 3]))
print('=========\n2) areSimilar is false =', areSimilar([1, 2, 2], [2, 1, 1]))
print('=========\n3) areSimilar false =', areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]))
