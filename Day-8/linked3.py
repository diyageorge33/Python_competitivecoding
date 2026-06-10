class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head= new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp=temp.next
        print(None)

    def sum1(self):
        esum=0
        temp=self.head
        while(temp):
            if temp.data%2==0:
                esum=esum+1
            temp=temp.next
        return esum
    
    def sum2(self):
        osum=0
        temp=self.head
        while(temp):
            if temp.data%2!=0:
                osum=osum+1
            temp=temp.next
        return osum
 

n=int(input("Enter number of nodes:"))
l1=LinkedList()
for i in range(n):
    data=int(input())
    l1.append(data)
l1.display()

evensum=l1.sum1()
oddsum=l1.sum2()

print("Even numbers:",evensum)
print("Odd numbers:",oddsum)