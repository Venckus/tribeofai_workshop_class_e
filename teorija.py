# --- theory ---
# recursion factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# tests
print("5! is", factorial(5))
print("10! is", factorial(10))

# recursion countdown
def count_down(start):
    if start <= 0:
        print(start)
    else:
        print(start)
        count_down(start - 1)
# tests
count_down(5)

# recusrion fibonacci
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
# tests
print("fib(5) is", fib(5))
print("fib(10) is", fib(10))

# recursion exponent
def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        return base * exponent_calc(base, expo-1)
# test
print('recursion exponent: ',exponent_calc(5, 3)) #print: 125

# bubble sort
def sort_with_bubbles(lst):
    #Set swap_occurred to True to guarantee the loop runs once
    swap_occurred = True

    #Run the loop as long as a swap occurred the previous time
    while swap_occurred:

        #Start off assuming a swap did not occur
        swap_occurred = False

        #For every item in the list except the last one...
        for i in range(len(lst) - 1):

            #If the item should swap with the next item...
            if lst[i] > lst[i + 1]:

                #Then, swap them! But these lines aren't
                #quite right: fix this code!
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                #One more line is needed here; add it!
                swap_occurred = True

    return lst
# tests
print('buble sort',sort_with_bubbles([5, 3, 1, 2, 4])) # print: [1, 2, 3, 4, 5]

# selection sort
def sort_with_select(a_list):

    #For each index in the list...
    for i in range(len(a_list)):

        #Assume first that current item is already correct...
        minIndex = i

        #For each index from i to the end...
        for j in range(i + 1, len(a_list)):

            #Complete the reasoning of this conditional to
            #complete the algorithm! Remember, the goal is
            #to find the lowest item in the list between
            #index i and the end of the list, and store its
            #index in the variable minIndex.
            #
            #Write your code here!
            if (a_list[minIndex] > a_list[j]):
                minIndex = j

        #Save the current minimum value since we're about
        #to delete it
        minValue = a_list[minIndex]

        #Delete the minimum value from its current index
        del a_list[minIndex]

        #Insert the minimum value at its new index
        a_list.insert(i, minValue)

    #Return the resultant list
    return a_list
# tests
print('selection sort',sort_with_select([5, 3, 1, 2, 4])) # print: [1, 2, 3, 4, 5]

# merge sort
def mergesort(lst):
    #Then, what does it do? mergesort should recursively run mergesort on the left and right sides of lst until
    #it's given a list only one item. So, if lst has only one item, we should just return that one-item list.
    if len(lst) <= 1:
        return lst
    #Otherwise, we should call mergesort separately on the left and right sides. Since each successive call to
    #mergesort sends half as many items, we're guaranteed to eventually send it a list with only one item, at
    #which point we'll stop calling mergesort again.
    else:
        #Floor division on the length of the list will find us the index of the middle value.
        midpoint = len(lst) // 2
        #lst[:midpoint] will get the left side of the list based on list slicing syntax. So, we want
        #to sort the left side of the list alone and assign the result to the new smaller list left.
        left = mergesort(lst[:midpoint])
        #And same for the right side.
        right = mergesort(lst[midpoint:])
        #So, left and right now hold sorted lists of each half of the original list. They might
        #each have only one item, or they could each have several items.
        #Now we want to compare the first items in each list one-by-one, adding the smaller to our new
        #result list until one list is completely empty.
        newlist = []
        while len(left) and len(right) > 0:
            #If the first number in left is lower, add it to the new list and remove it from left
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]
            #Otherwise, add the first number from right to the new list and remove it from right
            else:
                newlist.append(right[0])
                del right[0]
        #When the while loop above is done, it means one of the two lists is empty. Because both
        #lists were sorted, we can now add the remainder of each list to the new list. The empty list
        #will have no items to add, and the non-empty list will add its items in order.
        newlist.extend(left)
        newlist.extend(right)
        #newlist is now the sorted version of lst! So, we can return it. If this was a recursive call
        #to mergesort, then this sends a sorted half-list up the ladder. If this was the original
        #call, then this is the final sorted list.
        return newlist
#Let's try it out!
print('merge sort',mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))

# linear search
def linear(a_list, num):

    for i in range(len(a_list)):
        print(i)
        if a_list[i] == num:
            return i
    return False
# test
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print('linear search for index of nr: 6 is: ',linear(a_list, 6)) # print: 3

# binary search
def binary_search(searchList, searchTerm):
    #First, the list must be sorted.
    searchList.sort()
    #Now, each iteration of the loop, we want to narrow down the part of the list to look at. So, we need to
    #keep track of the range we've narrowed down to so far. Initially, that will be the entire list, from
    #the first index to the last.
    min = 0
    max = len(searchList) - 1
    #Now, we want to loop as long as our range has any numbers left to investigate. As long as there is
    #more than one number between minimum and maximum, we're not done searching.
    while min <= max:
        #We want to check the middle item of the current range, which is the average of the
        #current minimum and maximum index. For example, if min was 5 and max was 15, our
        #middle number would be at index 5. We'll use floor division because indices must be integers.
        currentMiddle = (min + max) // 2
        #If the term in the middle is the term we're looking for, we're done!
        if searchList[currentMiddle] == searchTerm:
            return True
        #If not, we want to check if the term we're looking for should come earlier or later.
        #If the term we're looking for is less than the current middle, then search the first
        #half of the list:
        elif searchTerm < searchList[currentMiddle]:
            max = currentMiddle - 1
        #If the term we're looking for is greater than the current middle, search the second
        #half of the list:
        else:
            min = currentMiddle + 1
        #Each iteration of the loop, one of three things happens: the term is found, max
        #shrinks, or min grows. Eventually, either the term will be found, or min will be
        #equal to max.
    #If the search term was found, this line will never be reached because the return statement
    #will end the function. So, if we get this far, then the search term was not found, and
    #we can return False.
    return False
#Let's try it out!
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))
#Want to see something else interesting? Because of the way Python handles types, this exact same
#function works for any sortable data type. Check it out with strings:
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))
#Or with dates!
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))
