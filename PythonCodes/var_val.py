from operator import add
def position_max_dist(pattern:str,R1:int,R2:int):
    R1_num=len(pattern)-R1+1
    R2_num=len(pattern)-R2+1
    
    moves={'^':[0,1],'v':[0,-1],'>':[1,0],'<':[-1,0]}
    R1_moves=[]
    R2_moves=[]
    for pat in range(R1_num):
        patrn=pattern[pat:pat+R1]
        lst1=[0,0]
        for i in range(len(patrn)):
            lst1=list(map(add,moves[patrn[i]],lst1))
        R1_moves.append(lst1)
    
    for pat in range(R2_num):
        patrn=pattern[pat:pat+R2]
        lst1=[0,0]
        for i in range(len(patrn)):
            lst1=list(map(add,moves[patrn[i]],lst1))
        R2_moves.append(lst1)
    # print(R1_moves)
    # print(R2_moves)
    max_dist=[]
    if len(R1_moves)>len(R2_moves):
        for j in range(len(R1_moves)):
            for i in range(len(R2_moves)):
                # print(R1_moves[j],R2_moves[i])
                dst=abs(R1_moves[j][0]-R2_moves[i][0])+abs(R1_moves[j][1]-R2_moves[i][1])
                max_dist.append(dst)
    else:
        for j in range(len(R2_moves)):
            for i in range(len(R1_moves)):
                dst=abs(R2_moves[j][0]-R1_moves[i][0])+abs(R2_moves[j][1]-R1_moves[i][1])
                max_dist.append(dst)
    
    # print(max_dist)
    print(max(max_dist))
            
    
position_max_dist("<><<^v",2,3) 



