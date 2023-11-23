import concurrent.futures
import time

def find_primes(number):
    flag_prime=False
    for x in range(round(number/2),1,-1):
        if(number%x==0):
            flag_prime=True
            break
        else:
            flag_prime=False
    if flag_prime!=True:
        return f"{number} is Prime"
    return None


def main():
    numbers_list=[x for x in range(2,9999999) if x%2!=0]
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        futures=list(executor.map(find_primes,numbers_list))
    
    print(futures)
    
if __name__=='__main__':
    start=time.time()
    main()
    end=time.time()
    print(end-start)