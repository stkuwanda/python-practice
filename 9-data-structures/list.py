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


