

def position_max_dist(patterns,R1,R2):
    
    
    
    R1_num=len(patterns)-R1+1
    R2_num=len(patterns)-R2+1
    
    
    
    def get_positions(num_moves,pattern):
        Robot_moves=[]
        for move in range(num_moves):
            mv_pat={'>':[1,0],'<':[-1,0],'^':[0,1],'v':[0,-1]}
            
            lst1=[0,0]
            lst=[0,0]
            # print('lst3 before update',lst1)
            
            moves=pattern[move:move+R2]
            print(moves)
            for j in ((moves)):
                
                lst2=mv_pat[j]
                print(lst1,lst2)

                # lst3=[lst3[0]+lst2[0],lst3[1]+lst2[1]]
                lst1 = [x + y for x, y in zip(lst1, lst2)]
                lst=list(map(lambda x,y:x+y,lst,lst2))
                
                # print(lst1)
                # print(lst)
                
                # print("lst3: ",lst3)
                # print("lst2: ",lst1)
            Robot_moves.append(lst1)
        
        return Robot_moves
    
    # R1_moves=get_positions(R1_num,patterns)  
    R2_moves=get_positions(R2_num,patterns)  
    
    
    # # print(R1_moves)
    print(R2_moves)
    # max_dst=[]
    # for i in ((R1_moves)):
        
    #     for j in (R2_moves):
            
    #         dst=abs(i[0]-j[0])+abs(i[1]+j[1])
            
    #         max_dst.append(dst)
     
    # return max(max_dst)            
     
print(position_max_dist("<><<^v",2,3))    
           