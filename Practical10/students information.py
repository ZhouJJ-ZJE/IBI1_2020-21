class Student:
    def __init__(self, fname, lname, course):
        self.__lname = lname
        self.__course = course
        self.__fname = fname

    def getfname(self):
        return self.__fname

    def getlname(self):
        return self.__lname

    def getcourse(self):
        return self.__course


s1 = Student('Jujie', 'Zhou', 'BMS')
print('His/Her name is ', s1.getfname(), s1.getlname(),
      ',and his/her major is', s1.getcourse())
s2 = Student(input('First name:'), input('Last name:'), input('Major:'))
print('His/Her name is ', s2.getfname(), s2.getlname(),
      ',and his/her major is', s2.getcourse())
