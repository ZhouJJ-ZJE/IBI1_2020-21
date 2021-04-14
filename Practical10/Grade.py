class Grade:
    def __init__(self, name, code, pre, final):
        self.__name = name
        self.__code = code
        self.__pre = pre
        self.__final = final

    def getname(self):
        return self.__name

    def getGrade(self):
        Grade = self.__code * 0.4+(self.__pre + self.__final) * 0.3
        return Grade


g1 = Grade('Jack', 78, 89, 100)
g2 = Grade(input('Name:'), int(input('Code portfolio grade :')), int(
    input('Poster presentation grade :')), int(input('Final exam grade:')))
print( 'The grade of',g2.getname(),' is', g2.getGrade())
