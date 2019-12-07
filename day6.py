class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None, parent=None):
        self.name = name
        self.children = []
        self.parent = parent
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

    def get_orbit_number(self, name, count):
        if self.name == name:
            return count
        else:
            for child in self.children:
                match = child.get_orbit_number(name, count+1)
                if match:
                    return match

lineList = [line.rstrip('\n') for line in open('input5.txt')]

orbit_list = []
for i in lineList:
    orbit_list.append((i.split(')')[0], i.split(')')[1]))

root = Tree('COM')
for i in orbit_list:
    if i[0] == 'COM':
        child = Tree(i[1], parent=root)
        root.add_child(child)
        orbit_list.remove(i)

current_node = root.children[0]
unique_object = set()
found = False
while len(orbit_list) > 0:
    found = False
    for i in orbit_list:
        if i[0] == current_node.name:
            unique_object.add(i[0])
            unique_object.add(i[1])
            new_node = Tree(i[1], parent=current_node)
            current_node.add_child(new_node)
            orbit_list.remove(i)
            current_node = new_node
            found = True
            break
    
    if not found:
        current_node = current_node.parent

sum_orbits = 0
for o in unique_object:
    sum_orbits += root.get_orbit_number(o, 0)
print(sum_orbits)