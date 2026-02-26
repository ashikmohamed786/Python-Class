# linked list

# advantages
# 1) stored in memory
# 2) fast access by index
# 3) must traverse step by step
# 4) flexible size

# BASIC STRUCTURE
# data and address of the next node

# [10|next]->[20|next]->[30|None]

# step-by-step logic

# create a class node
# store data
# store references to next node

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# n1=node(10)
# n2=node(20)
# n3=node(30)
# n1.next=n2
# n2.next=n3
# print(n1.data)
# print(n1.next.data)

# create linkedlist class
# create head pointer
# head stores first node

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_begin(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_end(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next

        temp.next=newnode

    def insert_pos(self,pos,data):
        newnode=node(data)


        if pos==1:
            newnode.next=self.head
            self.head=newnode
            return
        temp=self.head


        for _ in range(pos-2):
            temp=temp.next

        newnode.next=temp.next
        temp.next=newnode



    def display(self):
        temp=self.head

        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("none")

li=linkedlist()
li.insert_begin(10)
li.insert_begin(5)
li.insert_begin(20)
li.insert_begin(30)
li.insert_begin(15)
li.insert_end(50)


li.display()

