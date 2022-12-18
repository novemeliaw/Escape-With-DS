class Node:
    def __init__(self, value, text: list, choice: list, nextVal : list) -> None:
        self.data = value
        self.gameData = []
        self.gameData.append(text)
        self.gameData.append(choice)
        self.gameData.append(nextVal)
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        # Merupakan kepala paling atas
        self.root = None

    def insert(self, value, text, choice, nextValue):
        #check if root is empty
        if self.root == None :
            self.root = Node
        else :
            self.root = DFS(self.root, value)
        
        #traverse
        def DFS(curr, value):
            if curr == None:
                return Node(value)

            #insert left
            if value < curr.data :
                curr.left = DFS(curr.left, value)
            #insert right
            elif value > curr.data:
                curr.right = DFS(curr.right, value)
            return curr
        

    def search(self, value):
        def DFS(curr, value):
            if curr.data == value or curr.data == None:
                return curr 
            
            #search left
            if value < curr.data:
                return DFS(curr.left, value)
            #search right
            elif value > curr.data:
                return DFS(curr.right,value)
        return DFS(self.root,value)
    
    def printIn(self):
        if self.left:
            self.left.printIn()
        print(self.data, end = " -> ")

        if self.right:
            self.right.printIn()

dialogueTree = BinaryTree()
# Root 
text = ['Wah ada dua jalan aku harus pilih yang mana ya?']
choice = ['Jalan kiri', 'Jalan kanan']
nextVal = [6,  63]
dialogueTree.insert(7,text,choice,nextVal)

dialogueTree.printIn()
