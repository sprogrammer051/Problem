class Stack(object):
    def __init__(self):
        self.item=[]
    def push(self, item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    #def size(self):
    #    return len(self.item)
    def isEmpty(self):
        return self.item==[]
def reverse(str):
    TemStr =''
    stack=Stack()

    for i in range(len(str)):
        stack.push(str[i])

    while not stack.isEmpty():
        Tem=stack.pop()
        TemStr=TemStr+Tem
    return TemStr
print(reverse("SANDEEP kumar mishra"))
