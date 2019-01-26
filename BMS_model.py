class Student:
    """定义学生类"""

    def __init__(self, num, name, password="111111"):
        self.num = num
        self.name = name
        self.password = password


class Book:
    def __init__(self, number, bookName, author, publisher, category,
                 judge, lenderNumber=0, lendTime=0, returnTime=0):

        self.number = number
        self.bookname = bookName
        self.author = author
        self.publisher = publisher
        self.category = category
        self.judge = judge  # 表示是否外借

        self.lenderNumber = lenderNumber
        self.lendTime = lendTime
        self.returnTime = returnTime


    def register(self, num):

        if self.judge == True:
            return False

        elif self.judge == False:
            self.judge = True
            self.lenderNumber = num
            self.lendTime = time.asctime(time.localtime(time.time()))
            self.returnTime = self.lendTime

            return True


    def returnBook(self):

        self.judge = False
        self.lenderNumber = 0
        self.lendTime = 0
        self.returnTime = 0

        return True


class BMS:

    def __init__(self):

        self.students = []
        self.books = []
        self.buildBooks()



    def buildBooks(self):

        bookFile = open("books.txt", "+")
        line = bookFile.readline()
        while line:
            lyst = line.split('\t')

            book = Book(number=lyst[0], bookName=lyst[1],
                        author=lyst[2], publisher=lyst[3],
                        category=lyst[4], judge=lyst[5],
                        lenderNumber=lyst[6], lendTime=lyst[7],
                        returnTime=lyst[8])
            self.books.append(book)

            line = bookFile.readline()


    def buildStu(self):

        stuFile = open("students.txt", "+")
        line = stuFile.readline()
        while line:
            lyst = line.split('\t')

            student = Student(num=lyst[0], name=lyst[1],
                              password=lyst[2])
            self.students.append(student)

            line = stuFile.readline()


    def updateData(self):
