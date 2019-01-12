from tkinter import *
from time import sleep


def Move(a, b, c, n):
    if n == 0:
        return
    Move(a, c, b, n - 1)
    print("Take the %dth from %c to %c" % (n, a, c))
    sleep(0.5)
    Move(b, a, c, n - 1)


def main():
    n = 8
    root = Tk()
    root.title("The Tower of Hanoi")
    c = Canvas(root, height=500, width=800)
    c.create_rectangle(50, 490, 250, 500, fill="black")
    c.create_rectangle(300, 490, 500, 500, fill="black")
    c.create_rectangle(550, 490, 750, 500, fill="black")
    dishs = []
    num = [n, 0, 0]
    height = 400 / n
    for i in range(n):
        dish = c.create_rectangle(50 + 7 * (n - i),
                                  490 - height * (n - i),
                                  250 - 7 * (n - i),
                                  490 - height * (n - i - 1), fill="red")

        dishs.append(dish)

    c.pack()
    Move("A", "B", "C", 4)

    root.mainloop()


main()
