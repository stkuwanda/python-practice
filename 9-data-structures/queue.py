# queue implementation
# queue algorithm is last in first out (FIFO)
queue = []
while True:
    choice = int(input('''
    Enter a number to choose an option:
    1 to Enqueue element
    2 to Dequeue element
    3 to Display Front element
    4 to Display Back element
    5 to Display queue
    6 to Exit program
    :
    '''))
    if choice == 1:
        userInput = input('Enter a value: ')
        queue.insert( 0, userInput)
        print('You have enqueued {a} to the back of the queue.'.format(a=userInput))
    elif choice == 2:
        if len(queue) == 0:
            print('Sorry, the queue is empty.')
        else:
            poppedValue = queue.pop()
            print('You have dequeued {a} from the first position of the queue.'.format(a=poppedValue))
    elif choice == 3:
        if len(queue) == 0:
            print('Sorry, the queue is empty.')
        else:
            print('The value at the front of the queue is: {b}'.format(b=queue[-1]))
    elif choice == 4:
        if len(queue) == 0:
            print('Sorry, the queue is empty.')
        else:
            print('The value at the back of the queue is: {b}'.format(b=queue[0]))
    elif choice == 5:
        print('The queue:', queue)
    elif choice == 6:
        print('Exiting program...')
        break
    else:
        print('Invalid choice.')

