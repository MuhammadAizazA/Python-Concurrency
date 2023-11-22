import time
def check_package_working():
    print("Package is working")


def heavy_calculation(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")


def heavy_io(n, myid):  
    time.sleep(2)
    print(myid, "is done")


if __name__ == '__main__':
    check_package_working()
    
