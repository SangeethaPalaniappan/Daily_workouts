# Linkedlist Reverse 
 
# Date the file was Created : 13.08.2023

class Node: # This class is for creating Node
    def __init__(self,val): # whenever this class is called these will create automatically
        self.data=val
        self.next=None
        
class Linkedlist: # this class is for link the Nodes
    def __init__(self): # whenever this class is called these will create automatically
        self.head=None
    def insert(self,val): # Inserting the value at the last in the linked list 
        newnode=Node(val)
        temp=self.head
        if temp==None:
            self.head=newnode
        else:
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
    def reverse(self): # To reverse the linkedlist
        
        if self.head==None: # If there is no linkedlist
            return "No Linkedlist exist"
        
        # Assigning three ponters
        top=None 
        head=self.head
        last=head.next
        while last.next!=None:
            head.next=top # current node pointing the previous node
            top=head      # previous node became the current node 
            head=last     # next node as current node
            last=last.next# next node's next as next node
        head.next=top
        last.next=head
        self.head=last
    def printele(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        
a=Linkedlist()
a.insert(13)
a.insert(20)
a.insert(903)
a.insert(432)
a.insert(523)
a.printele()

a.reverse()
print("\n")
a.printele()
print("\n")
m=Linkedlist()
b=m.reverse()
print(b)