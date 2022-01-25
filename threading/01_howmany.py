import multiprocessing
# each thread will run in the SAME python intance (on one CPU) - CPU bound
# each process can run on SEPARATE python intances, separate CPUs
print( multiprocessing.cpu_count() )