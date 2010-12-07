# Intrumentation: vtpython simple_example.py

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def main():
    
    a=1.1
    b=1.2

    print add(mul(a,add(a,b)),add(a,b))

if __name__ == "__main__":
    main()
