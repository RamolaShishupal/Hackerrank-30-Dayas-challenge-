       
class Student(Person): 
    def __init__(self,firstName, lastName , idNumber , scores): 
        Person.__init__(self,firstName,lastName,idNumber) 
        self.scores = scores
    def calculate(self):
        
        s = 0
        for score in self.scores:
            s += score
        average = s/len(self.scores)
        if (average < 40):
            return 'T'
        elif (average < 55):
            return 'D'
        elif average < 70 : 
            return 'P'
        elif average < 80 :
            return 'A'
        elif average < 90:
            return 'E'
        else:
            return 'O'