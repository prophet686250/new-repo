def fac(f):
    var=f
    fact=var*(fac(var-1))
    return fact

print(fac(int(input())))
    
