# reference: I have discussed and got the idea of the code from Fatomate
class BSNode():
    def __init__(self, key, value, parent=None):
        self.key = key
        self.data = value
        self.right = None
        self.left = None
        #self.parent = parent
			

class BSTreeMap():  # implement the idea of the dictionary
    def __init__(self):
        self.root = None

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = BSNode(key,val)

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.left != None:
                self._put(key,val,currentNode.left)
            else:
                currentNode.left = BSNode(key,val)
        elif key > currentNode.key:
            if currentNode.right != None:
                self._put(key,val,currentNode.right)
            else:
                currentNode.right = BSNode(key,val)
        else: #for multiple values, build list directly 
            if isinstance(currentNode.data, list):
                currentNode.data.append(val)
            else:
                currentNode.data = [currentNode.data, val]
				
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
               return res.data
            else:
               return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.left)
        else:
            return self._get(key,currentNode.right)

        

posmap = BSTreeMap()
posmap.put('duck', 'verb')
posmap.put('duck', 'noun')
posmap.put('ducke', 'adj')
print(posmap.get('duck'))
