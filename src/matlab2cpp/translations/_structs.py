from _variables import *

def Counter(node):
    return "%(name)s = %(value)s"

def Var(node):
 
    index = node.declare.parent.names.index("_size")
    number = node.declare.parent[index].value
    return node.name + "[" + number + "]"
