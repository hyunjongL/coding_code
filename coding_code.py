import random


variables = ['a', 'b', 'c', 'd', 'e']
operation = ['+', '-']

var_num = len(variables)
op_num = len(operation)

def var_init():
    code =''
    for i in variables:
        code += i
        code += ' = '
        code += str(random.randrange(-100,100,1))
        code += '\n'
    return code

def fill_line(depth, type):
    line = '    ' * depth
    if type == 0:# var = var x var
        line += variables[random.randrange(0, var_num, 1)]
        line += ' = '
        line += variables[random.randrange(0, var_num, 1)]
        line += ' '
        line += operation[random.randrange(0, op_num, 1)]
        line += ' '
        line += variables[random.randrange(0, var_num, 1)]
        line +='\n'
    elif type == 1:# var = var x num
        line += variables[random.randrange(0, var_num, 1)]
        line += ' = '
        line += variables[random.randrange(0, var_num, 1)]
        line += ' '
        line += operation[random.randrange(0, op_num, 1)]
        line += ' '
        line += str(random.randrange(0,100,1))
        line += '\n'
    elif type == 2:# add a line of if
        line += 'if '
        line += variables[random.randrange(0,3,1)]
        line += ' '
        line += ['>', '<'][random.randrange(0,2,1)]
        line += ' '
        line += variables[random.randrange(0,3,1)]
        line += ':\n'
    elif type == 3:# add a line of while
        line += 'while '
        line += variables[random.randrange(0,3,1)]
        line += ' '
        line += ['>', '<'][random.randrange(0,2,1)]
        line += ' '
        line += variables[random.randrange(0,3,1)]
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
    code = var_init()
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
print(a)

f = open("./code.py", 'w')
f.write(a)
f.close
