#Linked_list
import time
start = time.time()
print(start)
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def addfirst(self,val):
        newnode=Node(val)
        if self.head==None:#if the list is empty
            self.head=newnode
        else:
            temp=self.head
            newnode.next=temp
            self.head=newnode
    def addlast(self,val):
        newnode=Node(val)
        temp=self.head
        if self.head==None:#if the list is empty
            self.head=newnode
        else:
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
    
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        
obj=linked_list()

obj.addlast("A")
obj.addlast("P")
obj.addlast("P")
obj.addlast("A")

obj.display()
end = time.time()
print('\n')
print(end)
print("Time:" , end - start)
print(obj)