
def check_num(funcc):
    
    def inner_funcc(*args,**kwargs):        
        if args[0]>args[1]:
            print(args)
            args=list(args)
            args[0],args[1]=args[1],args[0]
            args=tuple(args)
        print("child")
        return funcc(*args,**kwargs)
    
    return inner_funcc
    
    
@check_num
def num_div(a,b):
    print("base func")
    return a/b  

print(num_div(100,10))