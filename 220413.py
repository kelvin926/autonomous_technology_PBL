'''
a = (1, 2, 3)
b= [1, 2, 3]

b[0]=10
a[0]=10 #

a = (1, 2, 3)

x = 1
y = 2

y, x = x, y
(y, x) = (x, y) #

x = 1
y = 2 
y, x = x, y #

def foo(*args): #args = (1, 2, 3)
    print(type(agrs), len(args), agrs)

foo(1, 2, 3) #
'''
'''
def accumul(*args):
    s = 0
    i_len = (len(args))
    for i in range(i_len):
        s = s + args[i]

accumul(1, 2, 3)#

def accumul(*args):
    s = 0
    for item in args:
        s = s + item
    return s

ret = accumul(1, 2, 3)
print(ret)#

def __abs_accumul(a, b, c):
    ret = abs(a) + abs(b) + abs(c)
    return ret

    s = 0
    if len(args) == 3:
        return __abs_accumul(*args) #언패킹

    for item in args:
        s = s + item
    return s

ret = accumul(1, 2, 3) #패킹
'''
'''
l = [1, 2, 3, 4]
d = {'a':1, 'b':2, 'c':3, 'd':4}

last = len(l)-1

print(l[0] + 1[3])
print(d['a'] + d['d'])
'''
'''
def foo(): print("call foo")
def boo(): print("call boo")
d = {'a':1, 'b':2, 'c':3, 'd':4}

ret = input()
if ret == "foo":
    foo()
elif ret == "boo":
    boo()
'''
'''
def foo(): print("call foo")
def boo(): print("call boo")

call_tbl = {'foo':foo, 'boo':boo}
ret = input()
call_tbl[ret]()
'''
'''
def foo(a,b):
    print(a,b)

foo(c=0, b=1, 0)

def minx(**kwargs):
    pass
'''
'''
def minx(**kwargs):
    print(type(kwargs), len(kwargs), kwargs)
minx(a=1, c=0, b=2)
'''
'''
l = [0,1,2,3,4,5,6,7,8,9]
def foo(end):
    i = 0
    while i < end:
        i = i + 1
        yield i
for i in foo():
    print(i)
'''
'''
def foo(x):
    return x + 1

s1 = [i**22 for i in range(10)]
print(s1)
'''
def diff(x,y):
    return x - y

d1 = [diff(i, j) for i in range(3) for j in range(4)]
d2 = [lambda i, j: i - j  for i in range(3) for j in range(4)]