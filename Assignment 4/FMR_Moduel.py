from functools import reduce 
 

def filterX(Task,Elements):
    Result = [] 

    for no in Elements :
        Ret = Task(no)
        if (Ret == True):
            Result.append(no)
    return Result 

def mapX(Task,Elements):
    Result = []

    for no in Elements :
        Ret = Task(no)
        Result.append(Ret)
    return Result  

def reduceX(Task, Elements):
    if not Elements:
        return 0
    result = Elements[0]
    for no in Elements[1:]:
        result = Task(result, no)
    return result 

