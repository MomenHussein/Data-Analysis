import cmath
def LinearEq(equation): 
    
    # replacing all the x terms with j the imaginary part 
    s1 = equation.replace('x', 'j') 
      
    # shifting the equal sign to start  
    # an opening bracket 
    s2 = s1.replace('=', '-(') 
      
    # adding the closing bracket to form  
    # a complete expression 
    s = s2+')'
      
    # mapping the literal j to the complex j 
    z = eval(s, {'j': 1j}) 
    real, imag = z.real, -z.imag 
      
    # if the imaginary part is true return the 
    # answer 
    if imag: 
        return "x = %f" % (real/imag) 
    else: 
        if real: 
            return "No solution"
        else: 
            return "Infinite solutions"
    return equation
 
def QuadEq(a,b,c):
     
    # calculating  the discriminant
    dis = (b**2) - (4 * a*c)
     
    # find two results
    ans1 = (-b-cmath.sqrt(dis))/(2 * a)
    ans2 = (-b + cmath.sqrt(dis))/(2 * a)
     
    # printing the results
    print("The roots are:",ans1,",",ans2)

print(LinearEq("3x-7=0"))
