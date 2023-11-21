from sys import argv

state = 0

def exec(op):
    global state
    if op == '#': state += 1
    elif op == '@': state -= 1
    elif op == '*': state *= state
    elif op == '&': return str(state)
    return ''

print(''.join(map(exec, argv[1])))
