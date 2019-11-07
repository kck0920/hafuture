""" def fn():
    print('fn called')
fn()

def exp(x):
    return x ** 2
print(exp(9))

def get_fruits():
    return ['오렌지', '사과', '바나나']
print(get_fruits()[1])

def get_name():
    return 'kent', 'beck'
print(get_name())

def full_name(first_name, last_name):
    return first_name + '' + last_name
print(full_name('김','창균'))

def var_param(a, *vp):
    print(type(vp))
    print(a, len(vp), vp[len(vp) - 1])  # len(vp)의 값은 a값(AA)을 제외한 BBB, CCC 2개가 된다. 
var_param('AA','BBB', 'CCC')

def default_parma(a, b = 'BBB'):
    print(a, b)

default_parma('AAA')
default_parma('AAA', 'bbbbbbbbbb') """


# Recursive Funciton : 반복되는 함수
def factorial(n):
    if n == 1:
        return 1
 
    else:
        return n * factorial(n-1)
   
    pass
n=int(input("값을 입력하세요: "))
print(factorial(n))