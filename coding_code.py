import random
import time

imports = ['random']
variables = ['a', 'b', 'c', 'd', 'e']
operation = ['+', '-', '*', '/']

import_num = len(imports)
var_num = len(variables)
op_num = len(operation)

def random_var():
    return variables[random.randrange(0, var_num, 1)]

def print_random_var():
    var = random_var()
    time.sleep(random.random()/8)
    print(var, end = '', flush=True)
    time.sleep(random.random()/8)
    return var

def random_op():
    return operation[random.randrange(0, op_num, 1)]

def print_random_op():
    op = random_op()
    time.sleep(random.random()/8)
    print(op, end = '', flush=True)
    time.sleep(random.random()/8)
    return op

def random_num(n, m):
    return str(random.randrange(n, m, 1))

def print_random_num(n, m):
    num = random_num(n, m)
    time.sleep(random.random()/8)
    print(num, end = '', flush=True)
    time.sleep(random.random()/8)
    return num

def import_init():
    if import_num == 0:
        return ''
    else:
        code = ''
        for i in imports:
            print('import ', end = '', flush=True)
            code += 'import '
            print(i, end = '', flush=True)
            code += i
            code += '\n'
        print('\n', flush=True)
        code += '\n'
        return code

def var_init():
    comment = '# variable initialization'
    for i in comment:
        print(i, end = '', flush = True)
        time.sleep(random.random()/30)
    print()
    code ='# variable initialization\n'
    for i in variables:
        print(i , end = '')
        code += i
        print(' = ', end = '')
        code += ' = '
        code += print_random_num(1, 100)
        print('\n', end = '')
        code += '\n'
    code += '\n'
    return code

def fill_line(depth, type):
    line = '    ' * depth
    for i in range(depth):
        print('    ', end = '', flush=True)
        time.sleep(random.random()/20)
    if type == 0:# var = var x var
        line += print_random_var()

        print(' = ', end = '')
        line += ' = '

        line += print_random_var()

        print(' ', end = '')
        line += ' '

        line += print_random_op()

        print(' ', end = '')
        line += ' '
        line += print_random_var()

        print('\n', end = '')
        line +='\n'
    elif type == 1:# var = var x num
        line += print_random_var()
        print(' = ', end = '')
        line += ' = '
        line += print_random_var()
        print(' ', end = '')
        line += ' '
        line += print_random_op()
        print(' ', end = '')
        line += ' '
        line += print_random_num(1,100)
        print('\n', end = '')
        line += '\n'
    elif type == 2:# add a line of if
        print('if ', end = '')
        line += 'if '
        line += print_random_var()

        print(' ', end = '')
        line += ' '

        time.sleep(random.random()/10)
        a = ['>', '<'][random.randrange(0,2,1)]
        print(a, end = '', flush=True)
        line += a

        print(' ', end = '')
        line += ' '
        line += print_random_var()
        print(':\n', end = '')
        line += ':\n'
    elif type == 3:# add a line of while
        print('while ', end = '')
        line += 'while '
        line += print_random_var()
        print(' ', end = '')
        line += ' '
        time.sleep(random.random()/10)
        a = ['>', '<'][random.randrange(0,2,1)]
        print(a, end = '')
        line += a
        time.sleep(random.random()/15)
        print(' ', end = '', flush=True)
        line += ' '
        line += print_random_var()
        print(':\n', end = '')
        line += ':\n'
    return line

def line_of_code(depth):
    line =''
    if(random.random()>0.8):
        line = fill_line(depth, 2)
        depth += 1
    elif(random.random()>0.9):
        line = fill_line(depth, 3)
        depth += 1
    if(random.random()>0.4):
        line += fill_line(depth, 0)
    else:
        line += fill_line(depth, 1)
    return (line,depth)

def write_codes(n):
    code = ''
    code += import_init()
    code += var_init()
    depth = 0
    for i in range(n):
        if depth > 0 and random.random()>0.8:
            depth -= 1
        line = line_of_code(depth)
        depth = line[1]
        code += line[0]
    code += 'print('
    code += variables[0]
    for i in range(var_num-1):
        code += ', '
        code += variables[i+1]
    code += ')'

    return code

a = write_codes(random.randrange(7,15,1))
#print(a)

f = open("./code.py", 'w')
f.write(a)
f.close
