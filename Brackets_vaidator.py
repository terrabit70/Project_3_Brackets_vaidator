opened_brackets = '([{'
closed_brackets = ')]}'

stack = []

def brackets_equal(opened_bracket, closed_bracket):
    return opened_brackets.find(opened_bracket) == closed_brackets.find(closed_bracket)

def validate(string):
    if len(string) == 1:
        return False
    for symbol in string:
        if symbol in opened_brackets:
            stack.append(symbol)
        if symbol in closed_brackets:
            if not brackets_equal(stack[len(stack)-1], symbol):
                return False
            else:
                stack.pop()

    return True


valid_tests = [
'()',
'[]',
'{}',
'()[]{}',
'([{}])',
'{([])}',
'[{()}]',
'(qwe)  [qwe]  {qwe}',
'1(2[3{4}5]6)7',
'1{2(3[4]5)6}7',
'1[2{3(4)5}6]7',
'({{}}[[[({})]]])',
'(n(o(r)m)a)s',
'((()))'
]

for test in valid_tests:
    print ('valid text: ' + test)
    assert validate(test)

invalid_tests = [
'(',
'}',
'({)}',
'[(])',
'{[[]}]',
'({)[}]',
'(1[2{3{}4]5)',
'{([(])})',
'[{({)}]',
'[qwe)  {qwe]  (qwe}',
'(()))()()( zalupa',
')()( zalupa',
'())(() zalupa'
]

for test in invalid_tests:
    print ('invalid text: ' + test)
    assert not validate(test)