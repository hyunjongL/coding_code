import random

code = ''
variables = ['a', 'b', 'c']
operation = ['+', '-']

for i in variables:
    code += i
    code += ' = '
    code += str(random.randrange(-100,100,1))
    code += '\n'

def line_of_code():
    line = ''
    line += variables[random.randrange(0,3,1)]
    line += ' = '
    line += variables[random.randrange(0,3,1)]
    line += ' '
    line += operation[random.randrange(0,2,1)]
    line += ' '
    line += variables[random.randrange(0,3,1)]
    line += '\n'
    return line

for i in range(10):
    code = code + line_of_code()


print(code)
