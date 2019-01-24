import datetime

class Document:
    def __init__(self,authors = []):
        self.__authors = authors
        self.__date= datetime.datetime.now()

    def getAuthors(self):
        return self.__authors

    def addAuhor(self,name):
        self.__authors.append(name)

    def getDate(self):
        return self.__date

class Book:
    def __init__(self, title= ""):
        self.__title = title

    def getTitle(self):
        return self.__title

class Email:
    def __init__(self, subject= "",to = []):
        self.__subject = subject
        self.__to = to

    def getSubject(self):
        return self.__subject

    def getTo(self):
        return self.__to
