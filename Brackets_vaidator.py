print('****************************************************')
print('*             Brackets Validator V 0.2             *')
print('*        It can validates only "()" brackets       *')
print('*       It have a validate function and tests      *')
print('****************************************************')


def is_valid(text):
    brackets_counter = 0
    iterator = 0
    while iterator in range(len(text)):
        if text[iterator] == '(':
            brackets_counter += 1
        elif text[iterator] == ')':
            brackets_counter -= 1
            if brackets_counter < 0:
                break
        iterator += 1
    if brackets_counter == 0:
        string_valid = True
    else:
        string_valid = False
    return string_valid


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
