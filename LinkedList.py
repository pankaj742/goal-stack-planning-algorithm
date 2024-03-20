import random
class LinkedList:
    def __init__(self,v=None):
        self.value=v
        self.next=None

    def is_empty(self):
        if self.value == None:
            return True
        else:
            return False
    def add_node(self,v):
        if self.is_empty():
            self.value=v
            return self
        elif self.next ==None:
            node=LinkedList(v)
            self.next=node
            return self
        else:
            temp=self
            while(temp.next != None):
                temp=temp.next
            
            node=LinkedList(v)
            temp.next=node
            return self
    def find(self,v):
        self.previous=None
        if(self.is_empty()):
            return False
        elif(self.next == None and self.value==v):
            return 1
        elif(self.next != None and self.value==v):
            return 2
        else:
            temp=self
            while(temp.next != None):
                previous=temp
                temp=temp.next
                if(temp.value == v):
                    return(3)
    def delete(self,v):
        pos=self.find(v)
        if(pos == False):
            print("empty list")
        elif(pos ==1):
            self.value=None
        elif(pos == 2):
            (self.value,(self.next).value)=((self.next).value,self.value)
            self.next=self.next.next
        else:
            self.previous.next=self.previous.next.next
        

    def __str__(self):
        nodes=[]
        temp=self
        nodes.append(temp.value)
        while(temp.next != None):
            temp=temp.next
            nodes.append(temp.value)
        return(str(nodes))

lst=LinkedList()
for i in range(10):
    #v=random.randint(1,100)
    print(lst.add_node(i) is lst)
print(str(lst))
print(lst.delete(5) is lst)
print(str(lst))

