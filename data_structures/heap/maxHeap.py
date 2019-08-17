class MaxHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def __str__(self):
        return str(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, -1, self.heap)
        val = self.heap.pop()
        self.sift_down(0, self.heap)
        return val

    def build_heap(self, array):
        lowest_parent = ((len(array) - 2) // 2)
        for i in range(lowest_parent, -1, -1):
            self.sift_down(i, array)
        return array

    def sift_up(self, index):
        if index <= 0:
            return
        parent = (index - 1) // 2
        if self.heap[parent][0] < self.heap[index][0]:
            self.swap(parent, index, self.heap)
            self.sift_up(parent)
        elif self.heap[parent][0] == self.heap[index][0] and self.heap[parent][1] > self.heap[index][1]:
            self.swap(parent, index, self.heap)
            self.sift_up(parent)

    def sift_down(self, index, heap):
        l_child = (2 * index + 1)
        r_child = (2 * index + 2)
        if l_child >= len(heap):
            return
        elif r_child >= len(heap) or heap[l_child][0] > heap[r_child][0]:
            largest_child = l_child
        elif heap[l_child][0] == heap[r_child][0] and heap[l_child][1] < heap[r_child][1]:
            largest_child = l_child
        else:
            largest_child = r_child
        if heap[index][0] < heap[largest_child][0]:
            self.swap(index, largest_child, heap)
            self.sift_down(largest_child, heap)
        elif heap[index][0] == heap[largest_child][0] and heap[index][1] > heap[largest_child][1]:
            self.swap(index, largest_child, heap)
            self.sift_down(largest_child, heap)

    def swap(self, i, j, heap):
        temp = heap[i]
        heap[i] = heap[j]
        heap[j] = temp
