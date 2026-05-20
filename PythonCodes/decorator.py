def sub_func(func):
    
    def Inner_loop(*args,**kwargs):
        if args[0]>args[1]:
            print("Inner loop execution")
            args=list(args)
            args[0],args[1]=args[1],args[0]
            args=tuple(args)
            return func(*args,**kwargs)
    return Inner_loop

@sub_func
def dvision(x,y):
    print("devision")
    return x/y


dvision(100,10)

