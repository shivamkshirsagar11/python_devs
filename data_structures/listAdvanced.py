from list import *

class ContainerUpperBuilt(Container):
    def getByData(self,key):
        traveler = self.start
        all = []
        while traveler is not None:
            if traveler.data == key: 
                all.append(traveler.index)
            traveler = traveler.next
        print(f'Your data is at index/s: {all}')
    def deleteByIndex(self,id):
        traveler = self.start
        behind = self.start
        while traveler is not None:
            if traveler.index == id: 
                behind.next = traveler.next
            behind = traveler
            traveler = traveler.next
    def refreshIndex(self):
        traveler = self.start
        index=0
        while traveler is not None:
            traveler.index = index
            index = index+1
            traveler = traveler.next
    def replaceByIndex(self,id,data):
        traveler = self.start
        while traveler is not None:
            if traveler.index == id: 
                traveler.data = data
            traveler = traveler.next

# if __name__ == '__main__':
#     container = ContainerUpperBuilt()
#     data = -1
#     print("Type exit to stop")
#     while True:
#         data = input("Enter data: ")
#         if data.lower() == "exit": break
#         data = int(data)
#         container.forward(data)
#     container.traverse()
#     container.getByData(5)
#     container.deleteByIndex(3)
#     container.refreshIndex()
#     container.replaceByIndex(0,69)
#     container.traverse()