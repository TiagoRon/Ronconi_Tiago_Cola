class HeapMax:
    def __init__(self):
        self.elements = []
    
    def add(self, value):
        self.elements.append(value)
        self.float(len(self.elements)-1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements)-1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        father = (index-1) // 2
        while index > 0 and self.elements[index][0] > self.elements[father][0]:
            self.interchange(index, father)
            index = father
            father = (index-1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            max_index = left_child
            if right_child < len(self.elements):
                if self.elements[right_child][0] > self.elements[left_child][0]:
                    max_index = right_child
            if self.elements[index][0] < self.elements[max_index][0]:
                self.interchange(index, max_index)
                index = max_index
                left_child = (index * 2) + 1
            else:
                control = False

    def heapify(self, elements):
        self.elements = elements
        for i in range(len(self.elements) // 2 -1, -1, -1):
            self.sink(i)

    def sort(self):
        result = []
        amount_elements = len(self.elements)
        for i in range(amount_elements):
            value = self.remove()
            result.append(value)
        return result
    
    def arrive(self, value, priority):
        self.add([priority, value])

    def attend(self):
        return self.remove()

    def change_priority(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.float(index)
            elif new_priority < previous_priority:
                self.sink(index)

    def esta_vacio(self):
        return len(self.elements) == 0
