from vampytrace.instruments import seq as inst
import os

os.environ['VT_FILE_PREFIX']='trace_without_vtpython__'

def add(a,b):
    inst.VT_User_start('add','trace_without_vtpython.py',4) 
    c = a+b
    inst.VT_User_end('add')
    return c

def mul(a,b):
    inst.VT_User_start('mul','trace_without_vtpython.py',9)
    c = a*b
    inst.VT_User_end('mul')
    return c

def main():
    inst.VT_User_start('main','trace_without_vtpython.py',14)

    a=1.1
    b=1.2

    print add(mul(a,add(a,b)),add(a,b))

    inst.VT_User_end('main')

if __name__ == "__main__":
    inst.VT_User_trace_on()
    main()
    inst.VT_User_trace_off()
