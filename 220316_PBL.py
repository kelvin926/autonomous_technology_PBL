'''
def foo(n):
    return n+1

a = foo
print(a(10))

def boo(f,n):
    return f(n)

a = boo
a(foo,10)
'''

'''
def boo():
    def foo(n): # 클루저
        return n+1 
    return foo
x = boo()
'''

'''
def boo(m):
    t = 0
    def foo(n): # 클루저 : 함수 안에 또 다른 함수를 반환하는 것.
        nonlocal t
        t += m + n
        return t
    return foo

x = boo(10)
x(5)
'''

'''
class T:
    def __init__(self):
        self.t = 0
    def show(self):
        print(self.t)
'''

'''
class T:
    def __init__ (self,m):
        self.t = 0
        self.m = m
    def foo(self, n):
        self.t += self.m + n
        return self.t

X = T(10)
X.foo(5)
print(X.foo(5))
'''

'''
def T(m):  # T : 클루저 객체를 반환하는 함수
    t = 0
    def foo(n): # 클루저 객체
        nonlocal t # 쓰기할 때는 nonlocal 하기
        t += m + n
        return t
    return foo

X = T(10)
X(5)
print(X(5))
'''
'''
def xrange(n):
    step = 0.1
    r = 0.0
    while r < n:
        r += step
        yield r
print(xrange(10))
'''