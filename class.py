class Course:

    def __init__(self, course_name, course_teacher, course_code, course_site, course_week, course_day):
        self.c_name = course_name
        self.c_teacher = course_teacher
        self.c_code = course_code
        self.c_site = course_site
        self.c_week = course_week
        self.c_day = course_day


class Date:

    def __init__(self, m, d):
        day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while d > day_list[m]:
            d = d - day_list[m]
            m = m + 1
        self.year = 2019
        self.month = m
        self.day = d
        self.week = 0

