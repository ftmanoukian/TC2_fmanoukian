import sympy as sp

s = sp.symbols('s',complex = True)

def T_R(R : sp.Rational, derivacion : bool = False):
    if derivacion == True:
        return sp.Matrix([[1,0],[1/R,1]])
    else:
        return sp.Matrix([[1,R],[0,1]])
    
def T_L(L : sp.Rational, derivacion : bool = False):
    if derivacion == True:
        return sp.Matrix([[1,0],[1/(s*L),1]])
    else:
        return sp.Matrix([[1,s*L],[0,1]])
    
def T_C(C : sp.Rational, derivacion : bool = False):
    if derivacion == True:
        return sp.Matrix([[1,0],[s*C,1]])
    else:
        return sp.Matrix([[1,1/(s*C)],[0,1]])
    
def T_tanque(R : sp.Rational, C : sp.Rational, derivacion : bool = False):
    if derivacion == True:
        return sp.Matrix([[1,0],[1/(s*C+1/R),1]])
    else:
        return sp.Matrix([[1,R+1/(s*C)],[0,1]])