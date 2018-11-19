def square(n):
    """
    Returns the square of n.
    """
    result = n ** 2
    return result

def displayRange(lower, upper):
    """
    Outputs the numbers from lower to upper.
    :param lower:
    :param upper:
    :return:
    """
    while lower <= upper:
        print(lower)
        lower = lower + 1

def displayRange_(lower, upper):
    """
    Outputs the numbers from lower to upper.
    :param lower:
    :param upper:
    :return:
    """
    if lower <= upper:
        print(lower)
        displayRange_(lower + 1, upper)

def ourSum(lower, upper):
    """
    Returns the sum of the numbers from lower to upper.
    :param lower:
    :param upper:
    :return:
    """
    if lower > upper:
        return 0
    else:
        return lower + ourSum(lower + 1, upper)

def factorial(n):
    def recurse(n, product):
        """
        Returns the factorial of n.
        :param n:
        :param product:
        :return:
        """
        if n == 1:return product
        else: return recurse(n-1, n*product)
    recurse(n, 1)

def factorial_(n, product = 1):
    """
    Returns the factorial of n.
    :param n:
    :param product:
    :return:
    """
    if n == 1:return product
    else:return factorial_(n-1, n*product)

# import functools
# product = functools.reduce(lambda x,y:x*y, range(1, 11))
# print(product)

# f = open("file.txt", "r")
# txt = f.read()
# print(txt)
"""测试数据"""
list = [4,7,6,3,8,9,1,2]

"""交换数据"""
def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

"""选择排序：时间复杂度：O(n^2)"""
def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[minIndex] > lyst[j]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1


"""冒泡排序 时间复杂度："""
def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i-1]:
                swap(lyst, i, i-1)
            i += 1
        n -= 1

"""插入排序 时间复杂度：O(n^2)"""
def insertSort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j+1] = lyst[j]
                # print(lyst)
                j -= 1
            else:
                # print(lyst)
                break
        lyst[j+1] = itemToInsert
        # print(lyst)
        # print()
        i += 1

"""快速排序 时间复杂度：O(nlogn)"""
def quickSort(lyst):
    pass
insertSort(list)
print(list)
"""约瑟夫环问题"""
def JosephRing(num, space):
    lyst = range(1, num + 1)
    for i in range(num):
        lyst[i] = i % space
