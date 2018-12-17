import sys

def add(a, b):
    return a + b
    
def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b


if __name__ == '__main__':
    assert len(sys.argv) >= 4
    
    operation = sys.argv[1]
    x = int(sys.argv[2])
    y = int(sys.argv[3])

    if operation == 'add':
        print(add(x, y))        

    elif operation == 'sub':
        print(sub(x, y))

    elif operation == 'mult':
        print(mult(x, y))

    elif operation == 'div':
        print(div(x, y))
    
    elif operation == 'mod':
        print(mod(x, y))
