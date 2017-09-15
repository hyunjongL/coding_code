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

def line_of_code(depth):
    line = ''
    if(random.random()>0.8):
        line += '    '*depth
        line += 'if '
        line += variables[random.randrange(0,3,1)]
        line += ' '
        line += ['>', '<'][random.randrange(0,2,1)]
        line += ' '
        line += variables[random.randrange(0,3,1)]
        line += ':\n'
        depth += 1
    elif(random.random()>0.9):
        line += '    '*depth
        line += 'while '
        line += variables[random.randrange(0,3,1)]
        line += ['>', '<'][random.randrange(0,2,1)]
        line += variables[random.randrange(0,3,1)]
        line += ':\n'
        depth += 1
    line += '    '*depth
    line += variables[random.randrange(0,3,1)]
    line += ' = '
    line += variables[random.randrange(0,3,1)]
    line += ' '
    line += operation[random.randrange(0,2,1)]
    line += ' '
    line += variables[random.randrange(0,3,1)]
    line += '\n'
    return (line,depth)

def write_codes(n):
    code = var_init()
    depth = 0
    for i in range(n):
        if depth > 0 and random.random()>0.8:
            depth -= 1
        line = line_of_code(depth)
        depth = line[1]
        code += line[0]
    code += "print(a, b, c)"
    return code

a = write_codes(random.randrange(7,15,1))
print(a)

f = open("./code.py", 'w')
f.write(a)
f.close
