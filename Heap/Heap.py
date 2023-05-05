class Heap():
    def __init__(self, arr = []):
        self.arr = []
        self.size = 0
        for i in arr:
            self.insert(i)
        
    def __parent(self, i):
        return (i - 1) // 2
    
    def __heapify(self, i):
        if self.size == 0:
            return
        
        temp = self.arr[i]
        parent = self.__parent(i)
        data_parent = self.arr[parent]
        
        if temp > data_parent:
            self.arr[i] = data_parent
            self.arr[parent] = temp
        if parent > 0:
            self.__heapify(parent)    
            
    def insert(self, data):
        self.arr.append(data)
        self.size += 1
        self.__heapify(self.size - 1)


arr = [30, 12, 8, 90, 37, 50 ]

heap = Heap()
print(heap.arr)

for i in arr:
    heap.insert(i)
    
print("Heap sin usar el constructor:", end=" ")
print(heap.arr)

heap_init = Heap(arr)
print("Heap usando el constructor:", end=" ")
print(heap_init.arr)