from src import all_functions as m1
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
        t = threading.Thread(target=m1.heavy_io, args=(500,i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    threaded_io(80)
    
    
    