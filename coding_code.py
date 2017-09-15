import random

variables = ['a', 'b', 'c']
operation = ['+', '-']

def var_init():
    code =''
    for i in variables:
        code += i
        code += ' = '
        code += str(random.randrange(-100,100,1))
        code += '\n'
    return code

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

def write_codes(n):
    code = var_init()
    for i in range(n):
        code += line_of_code()
    code += "print(a, b, c)"
    return code

a = write_codes(random.randrange(7,15,1))
print(a)

f = open("./code.py", 'w')
f.write(a)
f.close
