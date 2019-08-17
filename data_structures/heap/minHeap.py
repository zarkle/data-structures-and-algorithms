class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

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
        # for i in reversed(range(lowest_parent + 1)):
        for i in range(lowest_parent, -1, -1):
            self.sift_down(i, array)
        return array

    def sift_up(self, index):
        if index <= 0:
            return
        parent = (index - 1) // 2
        if self.heap[parent] > self.heap[index]:
            self.swap(parent, index, self.heap)
            self.sift_up(parent)

    def sift_down(self, index, heap):
        l_child = (2 * index + 1)
        r_child = (2 * index + 2)
        if l_child >= len(heap):
            return
        elif r_child >= len(heap) or heap[l_child] < heap[r_child]:
            smallest_child = l_child
        else:
            smallest_child = r_child
        if heap[index] > heap[smallest_child]:
            self.swap(index, smallest_child, heap)
            self.sift_down(smallest_child, heap)

    def swap(self, i, j, heap):
        temp = heap[i]
        heap[i] = heap[j]
        heap[j] = temp


# testing
test = MinHeap([75, 20, 3, 8, 32, 1])

print(test.heap)

print(test.peek())
print(test.remove())
print(test.remove())
print(test.insert(9))
print(test.remove())
print(test.peek())
