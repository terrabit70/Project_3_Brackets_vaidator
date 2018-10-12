print('****************************************************')
print('*             Brackets Validator V 0.1             *')
print('*        It can validates only "()" brackets       *')
print('****************************************************')

input_string = input('Enter string to validate: ')

if input_string.find('(') == -1 and input_string.find(')') == -1:
    print('no brackets in your string')
elif (input_string.count('(') == input_string.count(')')) and (input_string.find('(') < input_string.find(')')):
    print('your string is valid')
else:
    print('Your string in not valid')

input('Press Enter to exit')
