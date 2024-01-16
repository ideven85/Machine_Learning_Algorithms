x = 100

def foo(y):
    return x+y

z = foo(307)
print(x,z,foo)
def bar(x):
    x=1000
    return foo(308)
w=bar(349)
print(x,w)

def apply_n_times(f,n,x):
    out = x
    for i in range(n):
        out=f(out)

    return out

def double(x):
    return x*2

print(apply_n_times(double,3,3)) # 12