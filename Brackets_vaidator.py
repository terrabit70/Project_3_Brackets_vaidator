'''
print('****************************************************')
print('*             Brackets Validator V 0.2             *')
print('*        It can validates only "()" brackets       *')
print('*       It have a validate function and tests      *')
print('****************************************************')


def is_valid(text):
    brackets_counter = 0
    for ch in text:
        if ch == '(':
            brackets_counter += 1
        elif ch == ')':
            brackets_counter -= 1
            if brackets_counter < 0:
                return False
    return brackets_counter == 0


text_1 = '(n(o(r)m)a)s'
text_2 = '(()))()()( zalupa'
text_3 = ')()( zalupa'
text_4 = '())(() zalupa'
text_5 = '((()))'


assert (is_valid(text_1))
assert (not is_valid(text_2))
assert (not is_valid(text_3))
assert (not is_valid(text_4))
assert (is_valid(text_5))
print('SUCCESS!')

'''

opened_brackets = '([{'
closed_brackets = ')]}'

def bracket_index(bracket):
    temporary_index = 0
    if bracket in opened_brackets:
        for ch in opened_brackets:
            if opened_brackets[temporary_index] == bracket:
                return temporary_index
            else:
                temporary_index += 1
    else:
        for ch in closed_brackets:
            if closed_brackets[temporary_index] == bracket:
                return temporary_index
            else:
                temporary_index += 1

def validation(string):
    temporary_string = []
    global is_valid

    for ch in string:
        if ch in opened_brackets + closed_brackets:
            temporary_string.append(ch)

    if (temporary_string[0] in closed_brackets) or (temporary_string[len(temporary_string) - 1] in opened_brackets):
        is_valid = False
        print('GOVNO')
        return False

    for i in range(len(opened_brackets)):
        if temporary_string.count(opened_brackets[i]) != temporary_string.count(closed_brackets[i]):
            is_valid = False
            print('ZHOPA')
            return False

    for i in range(len(temporary_string)):
        if (temporary_string[i] in closed_brackets) and (
                bracket_index(temporary_string[i]) != bracket_index(temporary_string[i - 1])):
            is_valid = False
            print('pizdes')
            return False

    is_valid = True
    return True


input_string = input()
#index = 0

validation(input_string)
print(is_valid)


