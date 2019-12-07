class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    def findObjectByName(self, name):
        if self.name == name:
            return self
        else:
            for child in self.children:
                match = child.findObjectByName(name)
                if match:
                    return match


lineList = [line.rstrip('\n') for line in open('input5.txt')]

tuple_list = []
for i in lineList:
    tuple_list.append((i.split(')')[0], i.split(')')[1]))

root = Tree('COM')
for i in tuple_list:
    if i[0] == 'COM':
        child = Tree(i[1])
        root.add_child(child)
        tuple_list.remove(i)

current_node = root.children[0]
previous_node = current_node
stack = []
found = False
while len(tuple_list) > 0:
    #print(len(tuple_list))
    found = False
    print(stack)
    for i in tuple_list:
        if i[0] == current_node.name:
            print('match ' + i[0])
            new_node = Tree(i[1])
            current_node.add_child(new_node)
            tuple_list.remove(i)
            current_node = new_node
            stack.append(current_node)
            print(current_node)
            found = True
            break
    
    if not found:
        try:
            current_node = stack.pop()
        except:
            print(tuple_list)
            sys.exit()







