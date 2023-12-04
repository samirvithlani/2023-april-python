def getUserDetail(*args):
    print(args)


getUserDetail("Ahmedabad", "Gujarat", "India")    


def getUserDEtail1(tup):
    print(tup)

getUserDEtail1(("Ahmedabad", "Gujarat", "India"))    


def getEmpDetail(**kwargs):
    print(kwargs)


getEmpDetail(name="Jay", age=20, city="Ahmedabad")    
    
    