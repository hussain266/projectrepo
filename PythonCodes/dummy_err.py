

class dog:
    
    def __init__(self,dog,breed,age,owner):
        self.name=dog
        self.breed=breed
        self.age=age
        self.owner=owner
        
        print(self.owner.conact_num)
        
class Owner:
    
    def __init__(self,name,age,contx_num):
        self.name=name
        self.age=age
        self.conact_num=contx_num
        
b1=Owner("Hussain",26,8618165598)
a1=dog("subbu","german",25,b1)


b2=Owner("Inamdar",26,123455878)
a2=dog("monti","japan",29,b2)

ad=a2.owner.conact_num

print(ad)
