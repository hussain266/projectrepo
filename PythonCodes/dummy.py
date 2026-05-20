
from collections import OrderedDict

def positionuing(pattern,R1,R2):
    
    def return_moves(pattern:str,R):
        move={'<':(-1,0),'>':(1,0),'v':(0,-1),'^':(0,1)}
        R_moves=len(pattern)-R+1
        R_num_moves=[]
        for j in range(R_moves):
            m=pattern[j:j+R]
            lst=(0,0)
            for i in (m):
                lst=list(map(lambda x:x[0]+x[1],zip(lst,move[i])))
            R_num_moves.append(lst)
        return R_num_moves
    
    R1_m=return_moves(pattern,R1)
    R2_m=return_moves(pattern,R2)
    print(R1_m)
    print(R2_m)
    
    max_dst=[]
    for j in ((R1_m)):
        for i in R2_m:
            max_dstence=abs(i[0]+j[0])+abs(i[1]+j[1])
        max_dst.append(max_dstence)
    return max(max_dst)
    
        
     
patt=input("Enter the patter: ")
R1=int(input("Enter the R1 moves: "))
R2=int(input("Enter the R2 moves: "))

print(positionuing(patt,R1,R2))           