import random


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Name(self):
        print(f"его зовут {self.name}")
    def Age(self):
        print(f"возраст человека: {self.age}")

    def __repr__(self):
        return (f"{self.name} {self.age}")


class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self): #наличие элементов в очередери
        return self.items == []

    def size(self): #длина очереди
        return len(self.items)

    def enqueue(self, items): #добавляем
        self.items.insert(1, items)

    def without(self, human):
        a = random.randrange(len(self.items))
        print(self.items[a], human)
        return self.items.insert(a + 1, human)

    def smotrim_vseh(self):
        print(f"очередь состоит из {self.items}")

    def where(self):
        print('люди стоят в очереди в поликлинике')


human1 = Human('Timur', 16)
human2 = Human('Maria', 18)
human3 = Human('Artem', 40)
human4 = Human('Nika', 38)

queue = Queue()
print(queue.isEmpty())
queue.where()

queue.enqueue(human1)
queue.enqueue(human2)
queue.enqueue(human3)
queue.enqueue(human4)
queue.smotrim_vseh()
print(queue.size())
queue.smotrim_vseh()
queue.without(human4)
queue.smotrim_vseh()
print(queue.isEmpty())





