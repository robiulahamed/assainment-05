import threading
import time


counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(1000000):
        with lock:
            counter += 1


threads = []
for _ in range(5):
    thread = threading.Thread(target=increment)
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()


print("Final counter value:", counter)
