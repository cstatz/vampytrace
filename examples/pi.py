# Intrumentation:
# mpirun -np <NP> vtpython -vt:mpi pi.py

from mpi4py import MPI
from numpy import array

def main(): 

    comm = MPI.COMM_WORLD

    rank = comm.Get_rank()
    comm_size = comm.Get_size()
 
    ppi = array(0, dtype=float)
    pi = array(0, dtype=float)

    n_intervals = 1000 
       
    h = 1.0 / float(n_intervals) 
    s = 0.0
     
    for i in range(rank+1,n_intervals,comm_size): 
        x = h*(float(i)-0.5) 
        s += 4./(1.+x**2) 
     
    _ppi = h*s 
    ppi.fill(_ppi)

    comm.Reduce([ppi, MPI.DOUBLE], [pi, MPI.DOUBLE], op=MPI.SUM, root=0)

    if rank==0:  
        print pi 

if __name__=="__main__":
    main() 
