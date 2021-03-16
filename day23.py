def levelOrder(self,root):
        q = [ root ]
        
        #i = 0
        
        #while i < len( q ):
        #    current = q[i]
        #    i += 1
        
        for current in q:    
            if current:
                print(current.data, end=' ')

                q.append(current.left)
                q.append(current.right) 
        #Write your code here

