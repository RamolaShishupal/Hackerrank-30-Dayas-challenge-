def getHeight(self,root):
        if root == None:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
       
      
        
            
        
        
      
