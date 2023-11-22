from src import all_functions as m1
import multiprocessing
import threading
import time

def decorator(func):
    def wrapper(*args,**kwarg):
        start = time.time()
        func(*args,**kwarg)
        end = time.time()
        print("Took: ", end - start)
    return wrapper

@decorator
def sequential(n):
    for i in range(n):
        m1.heavy_calculation(500, i)

@decorator
def threaded(n):
    threads = []
    for i in range(n):
        t = threading.Thread(target=m1.heavy_calculation, args=(500,i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

@decorator
def threaded_io(n):
    threads = []
    for i in range(n):
        t = threading.Thread(target=m1.heavy_io, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

@decorator
def multiproc_calcu(n):
    processes = []
    for i in range(n):
        p = multiprocessing.Process(target=m1.heavy_calculation, args=(500,i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


def doit(n):
    m1.heavy_calculation(500,n)

@decorator
def pooled(n):
    with multiprocessing.Pool() as pool:
       pool.map(doit, range(n))

if __name__ == "__main__":
    sequential(80)
    threaded(80)
    threaded_io(80)
    multiproc_calcu(80)
    pooled(80)