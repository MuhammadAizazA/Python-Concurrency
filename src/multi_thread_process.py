import multiprocessing
import my_logging_module as log
import concurrent.futures
import time
import threading

def calculate_square_fun(num):
    #time.sleep(2)
    return num * num

def just_fun(num):
    #time.sleep(2)
    return (num - 2)

def main():
    log.setup_logging()
    numbers = [x for x in range(1, 6000)]
    
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as Executor:
        if __name__=='__main__':
            result = list(Executor.map(calculate_square_fun, numbers))
            num_processes = len(multiprocessing.active_children())
            print(f"Number of active Process: {num_processes}")
            result2 = list(Executor.map(just_fun, numbers))
            num_processes = len(multiprocessing.active_children())
            print(f"Number of active Process: {num_processes}")
    
    finish = time.perf_counter()
    time_e = finish - start
    log.logging.info("Process Consumed time is {}".format(time_e))
    
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as Executor1: 
        
        result = list(Executor1.map(calculate_square_fun, numbers))
        num_threads = threading.active_count()
        print(f"Number of active threads: {num_threads}")
        result2 = list(Executor1.map(just_fun, numbers))
        num_threads = threading.active_count()
        print(f"Number of active threads: {num_threads}")

    finish = time.perf_counter()
    time_e = finish - start
    log.logging.info("Thread Consumed time is {}".format(time_e))

if __name__ == "__main__":
    main()
