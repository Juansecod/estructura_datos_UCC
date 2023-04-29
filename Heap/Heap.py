class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Heap():
    def __init__(self):
        self.root = None

    def heapify(self, array):
        for i in array:
            self.__recursive_insert(i)
        print(self.root.data)

"""     def __recursive_insert(self, data, node):
        if self.root is None:
            self.root = Node(data)
        else: """
            

            
        



    




arr = [30, 12, 8, 90, 37, 50 ]

heap = Heap()
heap.heapify(arr)