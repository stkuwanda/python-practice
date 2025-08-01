# list
# ordered: maintains the order of insertion
# mutable: it is changeable and items can be modified
# heterogeneous: list can contain items of different types
# duplicable items: items can be duplicated within the list

# empty list
list1 = []
print(list1)
print('type:', type(list1))

# index access
list1.append(1)
list1.append(2)
print('list1[1]:', list1[1])

# sublist
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 80, 90, 'Hello world!', 100]
print('sublist list2[3:6]:', list2[3:6])
print('sublist list2[2::3]:', list2[2::3])
print('sublist list2[1:5:3]:', list2[1:5:3])

# length of list
# returns the size of the list
# that is the number of items it can hold
print(len(list2))

# list iteration
list3 = [2, 4, 11, 24, 56, 67, 12, 45, 55, 27, 78, 89, 101, 97]
print(len(list3))
print('iteration 1:')
for i in range(len(list3)):
    print(list3[i])
print('iteration 2 (reversed list):')
list4 = list3[-1::-1]
for i in list4:
    print(i)
print('iteration 3 (reversed list2):')
for i in range(len(list3) - 1, -1, -1):
    print(list3[i])

# syntax of list comprehension
# [expression for item in list]
# it is more performant than using a for loop
list5 = [i for i in range(1, 21)]
print('new list', list5)
list6 = [i for i in range(1, 21) if i % 2 == 0]
print('even numbers list', list6)

# even numbers list with for loop
# this approach is slower than list comprehension
list7 = []
for i in range(1, 21):
    if i % 2 == 0:
        list7.append(i)

# count func
# returns an int count of the number of times an item
# occurs in the list
list8 = [12, 200, 45, 40, 4, 9, 31, 345,10, 10, 11, 30, 40, 50, 10, 60, 70, 80, 90, 100, 10, 110, 1]
print(list8.count(10))

# max func
# returns highest int item in a list
maxNumber = max(list8)
print('biggest item in list8:', maxNumber)

# min func
# returns highest int item in a list
minNumber = min(list8)
print('smallest item in list8:', minNumber)

# sort func
# by default rearranges list items in place in a sort order
list8.sort()
print('sorted list8:', list8)
print('sorted list8 (reversed):', list8[::-1])
list9 = [i for i in range(1, 21)]
list9.reverse()
print('sorted list9 (reversed):', list9)
list8.sort(reverse=True)
print('sorted list8 (reversed):', list8)

# index func
# returns index of input param
# errors if input param is not found in list
print('index of number 345:', list8.index(345))

# zip func
# allows to iterate over multiple lists
# expects all lists to have same length
# or works with the smallest list length
list10 = [10, 20, 30, 40, 50]
list11 = [11, 12, 13, 14, 15]
list12 = [1, 2, 3, 4, 5]
for a, b, c in zip(list10, list11, list12):
    print(a, b, c)

# split func
# split a string into a list
# by default will split on white space
wordMessage = 'My name is Simbarashe Kuwanda'
wordList = wordMessage.split()
print(wordList)

# list func
# split a string to individual chars into a list
wordList1 = list(wordMessage)
print(wordList1)

