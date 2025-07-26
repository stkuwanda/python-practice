# stack implementation
# stack algorithm is last in first out (LIFO)
stack = []
while True:
    choice = int(input('''
    Enter a number to choose an option:
    1 for Push element
    2 for Pop element
    3 for Peek element
    4 for Display stack
    5 for Exit program
    :
    '''))
    if choice == 1:
        userInput = input('Enter a value: ')
        stack.append(userInput)
        print('You have pushed {a} to the top of the stack.'.format(a=userInput))
    elif choice == 2:
        if len(stack) == 0:
            print('Sorry, the stack is empty.')
        else:
            poppedValue = stack.pop()
            print('You have popped {a} from the top of the stack.'.format(a=poppedValue))
    elif choice == 3:
        if len(stack) == 0:
            print('Sorry, the stack is empty.')
        else:
            print('The value on top of the stack is: {b}'.format(b=stack[-1]))
    elif choice == 4:
        print('The stack:', stack)
    elif choice == 5:
        print('Exiting program...')
        break
    else:
        print('Invalid choice.')