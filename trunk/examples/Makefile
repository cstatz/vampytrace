MPIRUN=mpirun
VTPYTHON=vtpython
PYTHON=python
NPROCS=8


all: pi simple_example trace_without_vtpython clean

pi:
	${MPIRUN} -np ${NPROCS} ${VTPYTHON} -vt:mpi pi.py

simple_example:
	${VTPYTHON} simple_example.py


trace_without_vtpython:
	${PYTHON} trace_without_vtpython.py

clean:
	rm -f *__.*
