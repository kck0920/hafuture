# 입력한 숫자를 사칙연산을 이용해서 계산하는 법 - 1
""" def p_arithmetic(a, b):
    return a + b
def m_arithmetic(a, b):
    return a - b
def mu_arithmetic(a, b):
    return a * b
def d_arithmetic(a, b):
    return a / b

a=int(input('1번째 숫자를 입력하세요:'))
b=int(input('2번째 숫자를 입력하세요:'))
c=input('입력한 두 수의 원하는 사칙연산자를 입력하세요(Usage: + or - or * or /): ')

if c == '+':
    print(p_arithmetic(a, b))
elif c == '-':
    print(m_arithmetic(a, b))
elif c == '*':
    print(mu_arithmetic(a, b))
else:
    print(d_arithmetic(a, b))  """

# 입력한 숫자를 사칙연산을 이용해서 계산하는 법 - 2

def p_arithmetic(a, b):
    return a + b

def m_arithmetic(a, b):
    return a - b

def mu_arithmetic(a, b):
    return a * b

def d_arithmetic(a, b):
    if b == 0:   # did.0 error 방지를 위해
        return a
    return a / b



def input_calc():
    cmd = input('Input(usage 4 + 5 >>>) ')
    cmds = cmd.split(' ')
    # print(cmds)

    # a = int(cmds[0])
    # op = cmds[1]
    # b = int(cmds[2])

    # @ToDo cmds 하나만으로 set해보기! -----------------
    a,op,b = cmds
    a,b= int(a),int(b)
    # a,op,b = int(cmds[0]), cmds[1], int(cmds[2])  이렇게 하는 것보다 위에 것이 코딩하기 쉽다. --------

    # if op == '+':
    #     print(reply.format(p_arithmetic(a ,b)))

    # elif op == '-':
    #     print(reply.format(m_arithmetic(a ,b)))

    # elif op == '*':
    #     print(reply.format(mu_arithmetic(a ,b)))

    # else:
    #     print(reply.format(d_arithmetic(a ,b)))

    if op == '+':
        r = p_arithmetic(a, b)

    elif op == '-':
        r = m_arithmetic(a, b)

    elif op == '*':
        r = mu_arithmetic(a, b)

    else:
        r = d_arithmetic(a, b)

    # reply = 'Answer is {}'

    if op in '/': 
        print("Answer is {:.2f}".format(r))  # 실수를 표현하기 위해 {:.2f} 사용 소수점 2자리까지

    else:
        print("Answer is {:d}".format(r))  # w정수를 표현하기 위해 {:f} 사용

while(True):
    input_calc()