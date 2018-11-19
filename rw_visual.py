import matplotlib.pyplot as plt
from MyClass import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=(10, 6))
    plt.scatter(rw.x_values, rw.y_values, s=5)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
