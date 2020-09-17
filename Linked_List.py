class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,size=None):
        self.head = None
        self.size = 0
    def append(self,elem):
        #inserção quando já possui elementos.
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
                pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self.size = self.size +1

    def __len__(self):
        #retorna o tamanho da lista
        return self.size
    def get(self,index):
        pass
    def getitem(self,index):
        pointer = self.head
        for n in range(index):
            if pointer:
                pointer = pointer.next
            else:
                #raise = modifica mensagem de erro(nesse caso coloquei o index out range)
                raise IndexError("list index out range")
        if pointer:
            return pointer.data
        raise IndexError("list index out range")        
    def setitem(self,index,elem):
        #modifica em posição especifica 
        pointer = self.head
        for n in range(index):
            if pointer:
                pointer = pointer.next
            else:
                #raise = modifica mensagem de erro(nesse caso coloquei o index out range)
                raise IndexError("list index out range")
            if pointer:
                pointer.data = elem
            else:
                raise IndexError("list index out range")   
    def seach(self,elem):
        #retorna posição de um elemnto na lista
        pos=0
        pointer = self.head
        while(pointer):
            if pointer.data == elem:
                return pos
            else:    
                pointer = pointer.next
                pos+=1
        raise ValueError("elemento não existe na lista")    


def display(self):
    contents = self.head
    if contents is None:
        print("lista vazia")
    while contents:
        print(contents.data)
        contents = contents.next     
def InsertFirst(self,new):
    NewNode = Node(new)
    NewNode.next = self.head
    self.head = NewNode         

lista= LinkedList()
InsertFirst(lista,9)
InsertFirst(lista,2)
print(len(lista))
display(lista)
print(lista.seach(9))

                