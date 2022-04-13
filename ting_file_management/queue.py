class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        else:
            return None

    def search(self, index):
        if self.__len__() == 0:
            raise IndexError
        elif index < 0:
            raise IndexError
        elif index >= self.__len__():
            raise IndexError
        else:
            return self.data[index]
