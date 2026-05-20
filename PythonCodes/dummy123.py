import threading
import time

def cpu_task():
    for i in range(5):
        print(f"{threading.current_thread().name} -> {i}")
        # Pretend work
        x = 0
        for _ in range(1_000_000):  # CPU-heavy loop
            x += 1
        print(f"x: {x}")

threads = []

# Create 3 threads
for n in range(3):
    t = threading.Thread(target=cpu_task, name=f"Thread-{n}")
    threads.append(t)
    print("Befor start {n}")
    t.start()
    print("after start {n}")

# Wait for all threads to finish
for t in threads:
    t.join()
print(t)
print("Done")