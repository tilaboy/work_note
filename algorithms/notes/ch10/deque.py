'''double-ended queue'''

class DoubleEndedQueue():
    def __init__(self, n):
        self.max_index = n - 1
        self.head = 0
        self.tail = 0
        self.queue = [0] * n
        self.not_empty = False

    def _empty(self):
        is_empty = False
        if self.head == self.tail:
            is_empty = True
        return is_empty

    def _full(self):
        is_full = False
        if self.tail + 1 == self.head or self.tail - self.head == self.max_index:
             is_full = True
        return is_full

    def enqueue(self, value):
        if self._full():
            raise ValueError('Reach limit {}'.format(self.max_index))
        else:
            self.queue[self.tail] = value
            if self.tail == self.max_index:
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self):
        if self._empty():
            raise ValueError('Empty queue, nothing to dequeue')
        else:
            value = self.queue[self.head]
            if self.head == self.max_index:
                self.head = 0
            else:
                self.head += 1
            return value

    def r_enqueue(self, value):
        if self._full():
            raise ValueError('Reach limit {}'.format(self.max_index))
        else:
            if self.head == 0:
                self.head = self.max_index
            else:
                self.head -= 1
            self.queue[self.head] = value

    def r_dequeue(self):
        if self._empty():
            raise ValueError('Empty queue, nothing to dequeue')
        else:
            if self.tail == 0:
                self.tail = self.max_index
            else:
                self.tail -= 1
            value = self.queue[self.tail]
            return value

    def ops(self, operation):
        if operation == '-':
            value = self.dequeue()
            print('dequeue {} ({} -> {}): {}'.format(value, self.head, self.tail, self.queue))
        elif operation == '--':
            value = self.r_dequeue()
            print('rdequeue {} ({} -> {}): {}'.format(value, self.head, self.tail, self.queue))

        elif operation.isdigit():
            self.enqueue(int(operation))
            print('queue      ({} -> {}): {}'.format(self.head, self.tail, self.queue))
        else:
            self.r_enqueue(abs(int(operation)))
            print('tail queue ({} -> {}): {}'.format(self.head, self.tail, self.queue))


deque = DoubleEndedQueue(6)
ops = ['1', '2', '3', '--','3', '-', '4', '-', '5', '6', '--', '7']
for op in ops:
    deque.ops(op)
