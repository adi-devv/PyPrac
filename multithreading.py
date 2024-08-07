import threading


def cuber(n):
    print("Cube: {}".format(n * n * n))


def squarer(n):
    print("Square: {}".format(n * n))


if __name__ == "__main__":
    # create the thread
    t1 = threading.Thread(target=squarer, args=(5,))
    t2 = threading.Thread(target=cuber, args=(5,))

    # start the thread t1

    t1.start()
    # start the thread t2
    t2.start()

    # wait until t1 is completed
    t1.join()
    # wait until t2 is completed
    t2.join()

    # both threads completed
    print("Done!")