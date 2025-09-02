# ex1

class A:
    def __init__(self):
        self.a = 1


class B(A):
    def __init__(self):
        # Coloque a linha selecionada aqui.
        self.b = 2

# ex2
class A:
    def __init__(self,v):
        self.__a = v + 1


a = A(0)
print(a.__a)

# ex3

def __init__(self,v):
self.__a = v + 1
a = A(0)
print(a.__a)

#ex4 
class A:
    def __init__(self,v = 1):
        self.v = v

    def set(self,v):
        self.v = v
        return v


a = A()
print(a.set(a.v + 1))

#ex5

class A:
    X = 0
    def __init__(self,v = 0):
        self.Y = v
        A.X += v


a = A()
b = A(1)
c = A(2)
print(c.X)

# ex6

class A:
    A = 1


print(hasattr(A,'A'))

#ex7

class A:
     def __init__(self):
        pass


a = A(1)
print(hasattr(a,'A'))

#ex8

class A:
    def __str__(self):
        return 'a'


class B(A):
    def __str__(self):
        return 'b'


class C(B):
    pass
 

o = C()
print(o)

# ex 9

class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(C,A))

#ex 10

class A:
    def a(self):
        print('a')


class B:
    def a(self):
        print('b')


class C(B,A):
    def c(self):
        self.a()


o = C()
o.c()


#ex 11
class A:
    def __str__(self):
        return 'a'


class B:
    def __str__(self):
        return 'b'


class C(A, B):
    pass


o = C()
print(o)

#ex 12

class A:
    v = 2


class B(A):
    v = 1


class C(B):
    pass


o = C()
print(o.v)

#ex13

def f(x):
    try:
        x = x / x
    except:
        print("a",end='')
    else:
        print("b",end='')
    finally:
        print("c",end='')


f(1)
f(0)

# ex 14

try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))

# ex 15

class Ex(Exception)
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)


try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)

# ex 15
class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x,end='')

#ex16

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x,end='')

