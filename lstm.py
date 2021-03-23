import numpy as np

w_fh = 0
w_fx = 0
w_ih = 0
w_ix = 100
w_oh = 0
w_ox = 100
bf = -100
bi = 100
bo = 0
w_ch = -100
w_cx = 50
bc = 0

h_t1 = 1
c_t1 = 1
xt = 1

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def ft():
    b = w_fh*h_t1 + w_fx*xt + bf
    c = 0
    if (b >= 1):
        c = 1
    elif (b <= -1):
        c = 0
    else:
        c = 0.5
    return c
def it():
    b = w_ih*h_t1 + w_ix*xt + bi
    c = 0
    if (b >= 1):
        c = 1
    elif (b <= -1):
        c = 0
    else:
        c = 0.5
    return c
def ot():
    b = w_oh*h_t1 + w_ox*xt + bo
    c = 0
    if (b >= 1):
        c = 1
    elif (b <= -1):
        c = 0
    else:
        c = 0.5
    return c
def ct():
    z = ft()
    x = it()
    print ('ft', z)
    print ('it', x)
    b = w_ch*h_t1 + w_cx * xt + bc
    if (b >= 1):
        c = 1
    elif(b<= -1):
        c = -1
    else:
        c = 0
    return z*c_t1 + x * c

def ht():
    a = ot()
    c = ct()
    print ('ot', a)
    print ('ct', c)
    if (c >= 1):
        d = 1
    elif (c<= -1):
        d = -1
    else:
        d = 0
    return a * d


def exec():

    print('ht', ht())


exec()

