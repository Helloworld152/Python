"""
File:timing1.py
Prints the running times for problem sizes that double,using a single loop.
"""
import time

problemSize = 1000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    start = time.time()

    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    elapsed = time.time() - start

    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2

