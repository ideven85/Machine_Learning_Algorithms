try:
    with open('mirror1.py', 'r') as f:
        src = f.read(60)
except FileNotFoundError as e:
    print("File Not Found, mirror1.py")
finally:
    src = "Hi"


try:
    print(f.closed, f.encoding)
except NameError as e:
    print("f not defined",e)
else:
    with open('mirror.py','r') as f:
        src=f.read(60)

# import ast
# print(src)
try:
    print(f.read())
except ValueError as e:
    print("Read operation on a closed object", e)
finally:
    print(src)
