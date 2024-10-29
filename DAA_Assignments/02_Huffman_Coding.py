# Huffman Encoding

from heapq import heappop, heappush

class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

        # tree direction (0/1)
        self.huff = ''  
    
    def __lt__(self, next):
        return self.freq < next.freq

# print Huffman Codes for all Symbols in newly created Huffman Tree
def printNodes(node, val=''):
    new_val = val + str(node.huff)
    
    if (node.left):
        printNodes(node.left, new_val)
    if (node.right):
        printNodes(node.right, new_val)
    else:
        print(f"{node.char} -> {new_val}")

chars = ['a', 'b', 'c', 'd', 'e', 'f'] 
freq = [50, 10, 30, 5, 3, 2] 

nodes = []

# converting characters and frequencies into huffman tree nodes 
for i in range(len(chars)): 
    heappush(nodes, Node(freq[i], chars[i])) 
  

while len(nodes) > 1: 
    # sort all the nodes in ascending order based on their frequency 
    left = heappop(nodes) 
    right = heappop(nodes) 
  
    # assign directional value to these nodes 
    left.huff = 0
    right.huff = 1
  
    # combine the 2 smallest nodes to create new node as their parent 
    newNode = Node(left.freq+right.freq, left.char+right.char, left, right) 
  
    heappush(nodes, newNode) 
  
printNodes(nodes[0]) 
