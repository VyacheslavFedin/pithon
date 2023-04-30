class Node:
    def __init__(self, data):

        self.next = None
        self.prev = None
        self.data = data


class List_2:
    def __init__(self):

        self.start_node = None

    def print_l(self):

        n = self.start_node
        while n is not None:
            print(n.data, end=' ')
            n = n.next
        print()
    
          
        

    def insert_start(self, data):

        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return

        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_end(self, data):

        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return

        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def delete_start(self):

        if self.start_node is None:
            print("no element")
            return
        if self.start_node.next is None:
            self.start_node = None
            return

        self.start_node = self.start_node.next
        self.start_node.prev = None

    def delete_end(self):

        if self.start_node is None:
            print("no element")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next.next is not None:
            n = n.next
        n.next = None

    def search(self, x):

        n = self.start_node
        while n is not None:
            if n.data == x:
                print("+")
                return
            n = n.next
        print("-")

    def revers(self):                    # разворот--------------------------------
        n = self.start_node
        while n is not None:
            
            l2.insert_start(n.data)
            
            n.data = None
            n = n.next

    # def sort(self):               # сортировка---------------------------
    #     n = self.start_node
    #     while n is not None:
            
    #         temp=n.data
    #         q=n.next
    #         while q is not None:
    #             if temp > q.data :
    #                 n.data=n.next
    #                 n.next = temp
    #             q=q.next
    #     n = n.next

        
l2 = List_2()
l2.delete_start()
l2.insert_start(2)
l2.insert_start(9)
l2.insert_start(8)
l2.insert_start(1)
l2.insert_end(3)
l2.insert_end(4)
l2.print_l()
l2.delete_start()
l2.delete_end()
l2.print_l()

l2.revers()
l2.print_l()
# l2.sort()
# l2.print_l()