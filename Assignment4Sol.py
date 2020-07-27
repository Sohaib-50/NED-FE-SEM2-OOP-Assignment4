## Q2
class Publication:
    def getdata(self):
        self.title = input("Title: ")
        self.price = float(input("Price: "))
    def putdata(self):
        print(f"Title: {self.title}\nPrice: {self.price}")

class Book(Publication):
    def getdata(self):
        print("Enter data for Book:")
        super().getdata()
        self.pageCount = int(input("Number of pages: "))
        print()
        
    def putdata(self):
        Publication.putdata(self)
        print(f"Number of pages: {self.pageCount}")
        print()

class Tape(Publication):
    def getdata(self):
        print("Enter data for audio cassette:")
        super().getdata()
        self.playingTime = float(input("Playing time (minutes):  "))
        print()
        
    def putdata(self):
        Publication.putdata(self)
        print(f"Playing time (in minutes): {self.playingTime}")
        print()

### Test Code      
##book_a = Book()
##book_a.getdata()
##
##casette_d = Tape()
##casette_d.getdata()
##
##book_a.putdata()
##casette_d.putdata()


## Q6
class Date:
    def setDay(self, day):
        self.day = day

    def setMonth(self, month):
        self.month = month

    def setYear(self, year):
        self.year = year

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def __str__(self):
        return f"{self.day:02}-{self.month:02}-{self.year}"

### test code
##today = Date()
##today.setMonth(7)
##today.setYear(2020)
##today.setDay(13)
##print(today)


## Q7
class Date:
    def setDay(self, day):
        self.day = day

    def setMonth(self, month):
        self.month = month

    def setYear(self, year):
        self.year = year

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def __str__(self):
        printFormat = self.format or 1
        if printFormat == 1: 
            return f"{self.day:02}-{self.month:02}-{self.year}"
        elif printFormat == 2:
            return f"{self.month:02}-{self.day:02}-{self.year}"
        else:
            return f"{self.year}-{self.month:02}-{self.day:02}"

# test code
today = Date()
today.setMonth(7)
today.setYear(2020)
today.setDay(13)
print(today)
            
