class List:
    def __init__(self,data=0):
        self.data = data
        self.index = 0
        self.next = None

class Container:
    def __init__(self):
        self.start = None
        self.end = None
        self.engage = False
        self.index = 0
    def getIndex(self,add=0): 
        self.index = self.index + add
        return self.index-1
    def forward(self,data=0):
        if(not self.engage):
            list = List(data)
            list.index = self.getIndex(1)
            list.next = None
            self.engage = True
            self.start = list
            self.end = list
        else:
            list = List(data)
            list.index = self.getIndex(1)
            list.next = None
            self.end.next = list
            self.end = list
    def traverse(self):
        traveler = self.start
        print("Head->",end="")
        while traveler != None:
            print(f' ({traveler.data},index:{traveler.index})->',end="")
            traveler = traveler.next
        else:
            print("<-End")

if __name__ == '__main__':
    container = Container()
    data = -1
    print("Type exit to stop")
    while True:
        data = input("Enter data: ")
        if data.lower() == "exit": break
        data = int(data)
        container.forward(data)
    container.traverse()