# simple calculator app demonstrating control flow
val1 = input('Enter a number: ')
val2 = input('Enter another number: ')
oper = input('Enter operator: ')
val1 = eval(val1)
val2 = eval(val2)
if oper == '+':
    print(val1 + val2)
elif oper == '-':
    print(val1 - val2)
elif oper == '*':
    print(val1 * val2)
elif oper == '/':
    print(val1 / val2)
elif oper == '//':
    print(val1 // val2)
elif oper == '**':
    print(val1 ** val2)
else:
    print('Invalid input.')