   
    def computeDifference(self):
        maximumDifference=[]
        
        a=range(len(self.__elements))
        
        for i in a:
            for j in a:
            
            
            

                maximumDifference.append(abs(int(self.__elements[i])-int(self.__elements[j])))
               
        
        self.maximumDifference=max(maximumDifference)
            